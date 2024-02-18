# General Object-Handling
from specutils import Spectrum1D
import numpy as np
from astropy import units as u
from astropy.table import QTable
from astropy.io import fits
import json
import warnings
# Functional Libraries
from scipy.ndimage import median_filter
from specutils.fitting import find_lines_derivative
from sparcl.client import SparclClient
from importlib.resources import files
from unidecode import unidecode

# loading jsons from data subdirectory
package_name = "SPEARS"
data_json_file_names = ['environment_variables.json', 'spectral_line_info.json']


# Loads essential information (API_parameters, and spectrum coeffecients)
data_file_path = files(package_name) / 'data' / data_json_file_names[0]
with data_file_path.open('r', encoding='utf-8') as file:
    environment_variables = json.load(file)

# Contains the ion names and wavelengths of each spectral line
data_file_path = files(package_name) / 'data' / data_json_file_names[1]
with data_file_path.open('r', encoding='utf-8') as file:
    spectral_line_info = json.load(file)

# Describes all functions available
__all__ = ['fetch_sparcl_ids', 
           'sparcl_ids_to_spectra', 
           'normalize_spectra', 
           'norm_spectra_to_lines', 
           'spectro_analyze']

def fetch_sparcl_ids(limit):
    """
    Fetches spectrum ids from the SPARCL API

    Parameters:
        environment_variables (dict, optional): Includes the parameters which the API searches under
            defaults to library values

    Returns:
        sparcl_ids (list): List of sparcl_ids
    """

    # initialize SPARCL client
    Client = SparclClient()

    # The program currently only supports Galactic spectrum from the DESI-EDR
    # Retrieves target 
    sparcl_id_response = Client.find(constraints=environment_variables['fetch_constraints'],
                            outfields=environment_variables['fetch_outfields'],
                            limit=limit)

    sparcl_ids = ['%s' % (s.sparcl_id) for s in sparcl_id_response.records]

    return sparcl_ids

def sparcl_ids_to_spectra(sparcl_ids, environment_variables=environment_variables):
    """
    Fetches spectra information outlined in environment_parameters, stores into a specutils Spectrum1D object
    Applies red/blueshift to spectral axis

    Parameters:
        sparcl_ids (list): list of ids of spectra to retrieve, either user-created or inputted through fetch_sparcl_ids
        environment_parameters (dict, optional): A dictionary containing  parameters for fetching and processing spectra.
            defaults to library values

    Returns:
        model_spectra_array (list of Spectrum1d object(s)): A list of Spectrum1D objects representing the fetched spectra.
        sparcl_ids (list): List of all SPARCL id(s) included in search
    """    

    Client = SparclClient()

    # Queries SPARCL API for the spectral data based on ids provided, and pre-set parameters in environment_variables
    sparcl_info_response = Client.retrieve(uuid_list=sparcl_ids,
                                    dataset_list=environment_variables['results_dataset'],
                                    include=environment_variables['results_include'])
    
    # stores spectra into array of Spectrum1D objects, and applies redshift to model
    model_spectra_array = [Spectrum1D(spectral_axis= (sparcl_info_response.records[i].wavelength / (sparcl_info_response.records[i].redshift + 1)) * u.AA,
        flux=np.array(sparcl_info_response.records[i].model) * u.Unit(environment_variables['flux_unit']),
        meta={'sparcl_id' : sparcl_ids[i]})
    for i in np.arange(0, len(sparcl_info_response.records), 1)]
    
    return model_spectra_array

def normalize_spectra(spectra, environment_variables=environment_variables):
    """
    Normalize spectrum1d list against the continuum derived by over-smoothing the original flux using median filtering.

    Parameters:
        spectra (list): List of Spectrum1D objects representing the spectra.
            Contains: Spectral axis, Flux, Meta={'sparcl_id' : id}
        environment_variables (dict, optional): provides variables to describe the spectrum variability extrapolation/interpolation function
            defaults to library values

    Returns:
        normalized_spectra_array (list): A list of Spectrum1D objects containing the normalized spectra
            Contains: Spectral axis, Flux, Meta={'sparcl_id' : id}
    """

    normalized_flux_array = []
    spectral_axis_array = []

    for i in np.arange(0, len(spectra), 1):

        # matches kernel size to spectrum variability
        flux_standard_deviation = np.std(spectra[i].flux.value)
        z_score = abs( (flux_standard_deviation - environment_variables['spectrum_variability_function']['mean']) / (environment_variables['spectrum_variability_function']['standard_deviation']) )
        kernel_size = 45*(1 / z_score)

        # normalizes spectrum
        continuum = median_filter(spectra[i].flux, size=int(kernel_size))
        #To avoid divide by zero error, zero-intercepts are replace by 1 in division
        continuum[continuum == 0] = 1
        spectral_axis_array.append(spectra[i].spectral_axis)
        normalized_flux_array.append(spectra[i].flux / continuum)

    # Stores normalized spectrum
        normalized_spectra = [
        Spectrum1D(
            spectral_axis=spectral_axis_array[r],
            flux=normalized_flux_array[r] * u.Unit(environment_variables['flux_unit']),
            meta={'sparcl_id': spectra[r].meta['sparcl_id']}
        )
        for r in np.arange(0, len(normalized_flux_array), 1)
    ]
    
    return normalized_spectra

def norm_spectra_to_lines(normalized_spectra, model_spectra = None, spectral_lines_info=spectral_line_info, save_as_fits=False):
    """
    Detects the present spectral lines (with relevant info) within the provided spectra

    Parameters:
        normalized_spectra (list):
            Contains: Spectral axis, Flux, Meta={'sparcl_id' : id}
        model_spectra (list, optional): initial unnormalized spectra, if included point-flux at line will be returned as part of qtable
            Contains: Spectral axis, Flux, Meta={'sparcl_id' : id}
        save_as_fits (boolean, optional): Option to return qtable as a .fits file
            defaults to False
        spectral_lines_info(dict, optional)
            defaults to library values

    Returns:
        qtable_dict (dict of QTables): results from each spectrum keyed through its sparcl_id, containing the following columns:
            'Ion' (str): The ion type present
            'Ion Line Wavelength' (float64, angstrom): The wavelength of the present spectral line
            'Spectral Flux at Line' (float64, 1 / (erg17 cm2 s Angstrom)): The model-spectral flux at the given spectral line wavelength
                If model_spectra is supplied
            'Observed Deviation' (float64, angstrom): The distance from the observed spectral line and the actual line
            'Normalized Deviation' (float64, dimensionless): The observed deviation divided by the spectral resolution at that given wavelength
            meta={'id'} : id of spectrum, iddentical to dict key
    """

    qtable_dict = {}
    defined_spectral_lines = spectral_lines_info['Angstrom_Array']
    defined_spectrum_median = np.median(defined_spectral_lines)

    for spec_index in np.arange(0, len(normalized_spectra), 1):
        # Ignores high SNR warnings from find_lines_derivative
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            potential_spectral_lines = find_lines_derivative(normalized_spectra[spec_index], flux_threshold=None)['line_center'].value

        matched_lines = []
        if model_spectra != None:
            matched_flux_column = []

                # spectral line sorting and filtration
        for defined_line in defined_spectral_lines: # returns matched_lines array with defined flux, followed by valid adjacent deviations
            spectral_resolution = (defined_line * environment_variables['spectral_resolution_function']['slope']) + environment_variables['spectral_resolution_function']['y-intercept']

            if defined_line >= defined_spectrum_median:
                
                for i in np.arange(potential_spectral_lines.shape[0]-2, 1, -1): 
                    if potential_spectral_lines[i] <= defined_line: 

                        adjacent_line_deviations = [(potential_spectral_lines[i] - defined_line), (potential_spectral_lines[i+1] - defined_line)]
                        
                        for linear_deviation in adjacent_line_deviations: 
                            if abs(linear_deviation) <= spectral_resolution:
                                matched_lines.append((defined_line, linear_deviation))
                                if model_spectra != None:
                                    matched_flux_column.append(model_spectra[spec_index].flux[i])
                        break
            else:
                for i in np.arange(1, potential_spectral_lines.shape[0]-1, 1):
                    if potential_spectral_lines[i] >= defined_line:
                        adjacent_line_deviations = [(potential_spectral_lines[i] - defined_line), (potential_spectral_lines[i-1] - defined_line)]

                        for linear_deviation in adjacent_line_deviations: 
                            if abs(linear_deviation) <= spectral_resolution:
                                matched_lines.append((defined_line, linear_deviation))
                                if model_spectra != None:
                                    matched_flux_column.append(model_spectra[spec_index].flux[i])
                        break     
            
        # data packaging
        ion_column = [unidecode(spectral_lines_info["Angstrom-Ion-Dict"][str(element[0])]) for element in matched_lines]
        wavelength_column = [element[0] * u.Angstrom for element in matched_lines] 
        observed_deviation_column = [element[1] * u.Angstrom for element in matched_lines] 
        normalized_deviation_column = [(element[1] / ((element[0]) * environment_variables['spectral_resolution_function']['slope']) + environment_variables['spectral_resolution_function']['y-intercept']) * u.dimensionless_unscaled for element in matched_lines]

        # qtable creation
        if model_spectra != None:
            qtable_dict[normalized_spectra[spec_index].meta['sparcl_id']] = (QTable([ion_column, wavelength_column, matched_flux_column, observed_deviation_column, normalized_deviation_column],
                                names=['Ion', 'Ion Line Wavelength', 'Spectral Flux at Line', 'Observed Deviation', 'Normalized Deviation'],
                                dtype=['str', 'float64', 'float64', 'float64', 'float64'],
                                meta={'id': [normalized_spectra[spec_index].meta['sparcl_id']]}))
        else:
            qtable_dict[normalized_spectra[spec_index].meta['sparcl_id']] = (QTable([ion_column, wavelength_column, observed_deviation_column, normalized_deviation_column],
                                names=['Ion', 'Ion Line Wavelength', 'Observed Deviation', 'Normalized Deviation'],
                                dtype=['str', 'float64', 'float64', 'float64'],
                                meta={'id': [normalized_spectra[spec_index].meta['sparcl_id']]}))
    
    if save_as_fits == False:
        # Returns as a dictionary of qtables
        return qtable_dict
    
    else:
        # Saves as a .FITS file
        hdul = fits.HDUList([fits.PrimaryHDU()])

        for key, qtable in qtable_dict.items():
            # Convert QTable to FITS BinTableHDU
            hdu = fits.table_to_hdu(qtable)
            hdu.header[key[-8:]] = key[-8:]
            
            # Append the HDU to the HDUList
            hdul.append(hdu)

        # Save the HDUList to a FITS file
        hdul.writeto('spectral_analysis_results.fits', overwrite=True)
        
        return

def spectro_analyze(sparcl_ids, save_as_fits = False):
    """
    Streamlined concatenation of all other functions, returns the qtable of detected line info from specified sparcl_ids

    Parameters:
        sparcl_ids (list): List containing one or more sparcl ids to run spectral analysis upon
        save_as_fits (boolean): If the function should save the final table as a .FITS file instead of returning it as a list of qtables
            defaults to False

    Returns
        qtable_dict (dict of QTables): results from each spectrum keyed through its sparcl_id, containing the following columns:
            'Ion' (str): The ion type present
            'Ion Line Wavelength' (float64, angstrom): The wavelength of the present spectral line
            'Spectral Flux at Line' (float64, 1 / (erg17 cm2 s Angstrom)): The model-spectral flux at the given spectral line wavelength
            'Observed Deviation' (float64, angstrom): The distance from the observed spectral line and the actual line
            'Normalized Deviation' (float64, dimensionless): The observed deviation divided by the spectral resolution at that given wavelength
            meta={'sparcl_id'} : id of spectrum, iddentical to dict key
    """

    # Fetches spectrums corresponding to sparcl_ids provided
    model_spectra = sparcl_ids_to_spectra(sparcl_ids)
    normalized_spectra = normalize_spectra(model_spectra)
    qtable_dict = norm_spectra_to_lines(normalized_spectra, save_as_fits=save_as_fits)

    if save_as_fits == False:
        return qtable_dict

    else:
        return