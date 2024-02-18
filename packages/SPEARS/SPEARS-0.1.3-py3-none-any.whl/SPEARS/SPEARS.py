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

# Variable Initializtion - *used to be done through seperate JSONS, but had errors shipping with package*
environment_variables = {
    "fetch_constraints": {
        "spectype": [
            "GALAXY"
        ],
        "datasetgroup": [
            "DESI"
        ]
    },
    "fetch_outfields": [
        "sparcl_id"
    ],
    "results_dataset": [
        "DESI-EDR"
    ],
    "results_include": [
        "wavelength",
        "redshift",
        "model"
    ],
    "flux_unit": "1 / (erg17 cm2 s Angstrom)",
    "spectrum_variability_function" : {
        "standard_deviation" : 0.260,
        "mean" : 0.376
    },
    "spectral_resolution_function" : {
        "slope" : -3.23e-5,
        "y-intercept" : 1.78
    }
}

spectral_line_info = {
    "Angstrom-Ion-Dict": {
        "770.409": "Ne-VIII",
        "780.324": "Ne-VIII",
        "937.814": "Ly-\u03b5",
        "949.742": "Ly-\u03b4",
        "977.03": "C-III",
        "989.79": "N-III",
        "991.514": "N-III",
        "991.579": "N-III",
        "1025.722": "Ly-\u03b2",
        "1031.912": "O-VI",
        "1037.613": "O-VI",
        "1066.66": "Ar-I",
        "1215.67": "Ly-\u03b1",
        "1238.821": "N-V",
        "1242.804": "N-V",
        "1260.422": "Si-II",
        "1264.73": "Si-II",
        "1302.168": "O-I",
        "1334.532": "C-II",
        "1335.708": "C-II",
        "1393.755": "Si-IV",
        "1397.232": "O-IV]",
        "1399.78": "O-IV]",
        "1402.77": "Si-IV",
        "1486.496": "N-IV]",
        "1548.187": "C-IV",
        "1550.772": "C-IV",
        "1640.42": "He-II",
        "1660.809": "O-III]",
        "1666.15": "O-III]",
        "1746.823": "N-III]",
        "1748.656": "N-III]",
        "1854.716": "Al-III",
        "1862.79": "Al-III",
        "1892.03": "Si-III]",
        "1908.734": "C-III]",
        "2142.78": "N-II]",
        "2320.951": "[O-III]",
        "2323.5": "C-II]",
        "2324.69": "C-II]",
        "2648.71": "[Fe-XI]",
        "2733.289": "He-II",
        "2782.7": "[Mg-V]",
        "2795.528": "Mg-II]",
        "2802.705": "Mg-II]",
        "2829.36": "[Fe-IV]",
        "2835.74": "[Fe-IV]",
        "2853.67": "[Ar-IV]",
        "2868.21": "[Ar-IV]",
        "2928.0": "[Mg-V]",
        "2945.106": "He-I",
        "3132.794": "O-III",
        "3187.745": "He-I",
        "3203.1": "He-II",
        "3312.329": "O-III",
        "3345.821": "[Ne-V]",
        "3425.881": "[Ne-V]",
        "3444.052": "O-III",
        "3466.497": "[N-I]",
        "3466.543": "[N-I]",
        "3487.727": "He-I",
        "3586.32": "[Fe-VII]",
        "3662.5": "[Fe-VI]",
        "3686.831": "H19",
        "3691.551": "H18",
        "3697.157": "H17",
        "3703.859": "H16",
        "3711.977": "H15",
        "3721.945": "H14",
        "3726.032": "[O-II]",
        "3728.815": "[O-II]",
        "3734.369": "H13",
        "3750.158": "H12",
        "3758.92": "[Fe-VII]",
        "3770.637": "H11",
        "3797.904": "H10",
        "3835.391": "H9",
        "3839.27": "[Fe-V]",
        "3868.76": "[Ne-III]",
        "3888.647": "He-I",
        "3889.064": "H8",
        "3891.28": "[Fe-V]",
        "3911.33": "[Fe-V]",
        "3967.47": "[Ne-III]",
        "3970.079": "H\u03b5",
        "4026.19": "He-I",
        "4068.6": "[S-II]",
        "4071.24": "[Fe-V]",
        "4076.349": "[S-II]",
        "4101.742": "H\u03b4",
        "4143.761": "He-I",
        "4178.862": "Fe-II",
        "4180.6": "[Fe-V]",
        "4233.172": "Fe-II",
        "4227.19": "[Fe-V]",
        "4287.394": "[Fe-II]",
        "4303.176": "Fe-II",
        "4317.139": "O-II",
        "4340.471": "H\u03b3",
        "4363.21": "[O-III]",
        "4412.3": "[Ar-XIV]",
        "4414.899": "O-II",
        "4416.83": "Fe-II",
        "4452.098": "[Fe-II]",
        "4471.479": "He-I",
        "4489.183": "Fe-II",
        "4491.405": "Fe-II",
        "4510.91": "N-III",
        "4522.634": "Fe-II",
        "4555.893": "Fe-II",
        "4582.835": "Fe-II",
        "4583.837": "Fe-II",
        "4629.339": "Fe-II",
        "4634.14": "N-III",
        "4640.64": "N-III",
        "4641.85": "N-III",
        "4647.42": "C-III",
        "4650.25": "C-III",
        "4651.47": "C-III",
        "4658.05": "[Fe-III]",
        "4685.71": "He-II",
        "4711.26": "[Ar-IV]",
        "4740.12": "[Ar-IV]",
        "4861.333": "H\u03b2",
        "4893.37": "[Fe-VII]",
        "4903.07": "[Fe-IV]",
        "4923.927": "Fe-II",
        "4958.911": "[O-III]",
        "5006.843": "[O-III]",
        "5018.44": "Fe-II",
        "5084.77": "[Fe-III]",
        "5145.75": "[Fe-VI]",
        "5158.89": "[Fe-VII]",
        "5169.033": "Fe-II",
        "5176.04": "[Fe-VI]",
        "5197.577": "Fe-II",
        "5200.257": "[N-I]",
        "5234.625": "Fe-II",
        "5236.06": "[Fe-IV]",
        "5270.4": "[Fe-III]",
        "5276.002": "Fe-II",
        "5276.38": "[Fe-VII]",
        "5302.86": "[Fe-XIV]",
        "5309.11": "[Ca-V]",
        "5316.615": "Fe-II",
        "5316.784": "Fe-II",
        "5335.18": "[Fe-VI]",
        "5424.22": "[Fe-VI]",
        "5517.709": "[Cl-III]",
        "5537.873": "[Cl-III]",
        "5637.6": "[Fe-VI]",
        "5677.0": "[Fe-VI]",
        "5695.92": "C-III",
        "5720.7": "[Fe-VII]",
        "5754.59": "[N-II]",
        "5801.33": "C-IV",
        "5811.98": "C-IV",
        "5875.624": "He-I",
        "6046.44": "O-I",
        "6087.0": "[Fe-VII]",
        "6300.304": "[O-I]",
        "6312.06": "[S-III]",
        "6347.1": "Si-II",
        "6363.776": "[O-I]",
        "6369.462": "Fe-II",
        "6374.51": "[Fe-X]",
        "6516.081": "Fe-II",
        "6548.05": "[N-II]",
        "6562.819": "H\u03b1",
        "6583.46": "[N-II]",
        "6716.44": "[S-II]",
        "6730.81": "[S-II]",
        "7002.23": "O-I",
        "7005.87": "[Ar-V]",
        "7065.196": "He-I",
        "7135.79": "[Ar-III]",
        "7155.157": "[Fe-II]",
        "7170.62": "[Ar-IV]",
        "7172.0": "[Fe-II]",
        "7236.42": "C-II",
        "7237.26": "[Ar-IV]",
        "7254.448": "O-I",
        "7262.76": "[Ar-IV]",
        "7281.349": "He-I",
        "7319.99": "[O-II]",
        "7330.73": "[O-II]",
        "7377.83": "[Ni-II]",
        "7411.16": "[Ni-II]",
        "7452.538": "[Fe-II]",
        "7468.31": "N-I",
        "7611.0": "[S-XII]",
        "7751.06": "[Ar-III]",
        "7816.136": "He-I",
        "7868.194": "Ar-I",
        "7889.9": "[Ni-III]",
        "7891.8": "[Fe-XI]",
        "8236.79": "He-II",
        "8392.397": "Pa20",
        "8413.318": "Pa19",
        "8437.956": "Pa18",
        "8446.359": "O-I",
        "8467.254": "Pa17",
        "8498.02": "Ca-II",
        "8502.483": "Pa16",
        "8542.09": "Ca-II",
        "8545.383": "Pa15",
        "8578.7": "[Cl-II]",
        "8598.392": "Pa14",
        "8616.95": "[Fe-II]",
        "8662.14": "Ca-II",
        "8665.019": "Pa13",
        "8680.282": "N-I",
        "8703.247": "N-I",
        "8711.703": "N-I",
        "8750.472": "Pa12",
        "8862.782": "Pa11",
        "8891.91": "[Fe-II]",
        "9014.909": "Pa10",
        "9068.6": "[S-III]",
        "9229.014": "Pa9",
        "9531.1": "[S-III]",
        "9545.969": "Pa\u03b5",
        "9824.13": "[C-I]",
        "9850.26": "[C-I]",
        "9913.0": "[S-VIII]",
        "10027.73": "He-I",
        "10031.16": "He-I",
        "10049.368": "Pa\u03b4",
        "10286.73": "[S-II]",
        "10320.49": "[S-II]",
        "10336.41": "[S-II]",
        "10746.8": "[Fe-XIII]",
        "10830.34": "He-I",
        "10938.086": "Pa\u03b3"
       },
    "Angstrom_Array": [
        770.409,
        780.324,
        937.814,
        949.742,
        977.03,
        989.79,
        991.514,
        991.579,
        1025.722,
        1031.912,
        1037.613,
        1066.66,
        1215.67,
        1238.821,
        1242.804,
        1260.422,
        1264.73,
        1302.168,
        1334.532,
        1335.708,
        1393.755,
        1397.232,
        1399.78,
        1402.77,
        1486.496,
        1548.187,
        1550.772,
        1640.42,
        1660.809,
        1666.15,
        1746.823,
        1748.656,
        1854.716,
        1862.79,
        1892.03,
        1908.734,
        2142.78,
        2320.951,
        2323.5,
        2324.69,
        2648.71,
        2733.289,
        2782.7,
        2795.528,
        2802.705,
        2829.36,
        2835.74,
        2853.67,
        2868.21,
        2928.0,
        2945.106,
        3132.794,
        3187.745,
        3203.1,
        3312.329,
        3345.821,
        3425.881,
        3444.052,
        3466.497,
        3466.543,
        3487.727,
        3586.32,
        3662.5,
        3686.831,
        3691.551,
        3697.157,
        3703.859,
        3711.977,
        3721.945,
        3726.032,
        3728.815,
        3734.369,
        3750.158,
        3758.92,
        3770.637,
        3797.904,
        3835.391,
        3839.27,
        3868.76,
        3888.647,
        3889.064,
        3891.28,
        3911.33,
        3967.47,
        3970.079,
        4026.19,
        4068.6,
        4071.24,
        4076.349,
        4101.742,
        4143.761,
        4178.862,
        4180.6,
        4233.172,
        4227.19,
        4287.394,
        4303.176,
        4317.139,
        4340.471,
        4363.21,
        4412.3,
        4414.899,
        4416.83,
        4452.098,
        4471.479,
        4489.183,
        4491.405,
        4510.91,
        4522.634,
        4555.893,
        4582.835,
        4583.837,
        4629.339,
        4634.14,
        4640.64,
        4641.85,
        4647.42,
        4650.25,
        4651.47,
        4658.05,
        4685.71,
        4711.26,
        4740.12,
        4861.333,
        4893.37,
        4903.07,
        4923.927,
        4958.911,
        5006.843,
        5018.44,
        5084.77,
        5145.75,
        5158.89,
        5169.033,
        5176.04,
        5197.577,
        5200.257,
        5234.625,
        5236.06,
        5270.4,
        5276.002,
        5276.38,
        5302.86,
        5309.11,
        5316.615,
        5316.784,
        5335.18,
        5424.22,
        5517.709,
        5537.873,
        5637.6,
        5677.0,
        5695.92,
        5720.7,
        5754.59,
        5801.33,
        5811.98,
        5875.624,
        6046.44,
        6087.0,
        6300.304,
        6312.06,
        6347.1,
        6363.776,
        6369.462,
        6374.51,
        6516.081,
        6548.05,
        6562.819,
        6583.46,
        6716.44,
        6730.81,
        7002.23,
        7005.87,
        7065.196,
        7135.79,
        7155.157,
        7170.62,
        7172.0,
        7236.42,
        7237.26,
        7254.448,
        7262.76,
        7281.349,
        7319.99,
        7330.73,
        7377.83,
        7411.16,
        7452.538,
        7468.31,
        7611.0,
        7751.06,
        7816.136,
        7868.194,
        7889.9,
        7891.8,
        8236.79,
        8392.397,
        8413.318,
        8437.956,
        8446.359,
        8467.254,
        8498.02,
        8502.483,
        8542.09,
        8545.383,
        8578.7,
        8598.392,
        8616.95,
        8662.14,
        8665.019,
        8680.282,
        8703.247,
        8711.703,
        8750.472,
        8862.782,
        8891.91,
        9014.909,
        9068.6,
        9229.014,
        9531.1,
        9545.969,
        9824.13,
        9850.26,
        9913.0,
        10027.73,
        10031.16,
        10049.368,
        10286.73,
        10320.49,
        10336.41,
        10746.8,
        10830.34,
        10938.086
    ],
    "Ion_Array": [
        "Ne-VIII",
        "Ne-VIII",
        "Ly-\u03b5",
        "Ly-\u03b4",
        "C-III",
        "N-III",
        "N-III",
        "N-III",
        "Ly-\u03b2",
        "O-VI",
        "O-VI",
        "Ar-I",
        "Ly-\u03b1",
        "N-V",
        "N-V",
        "Si-II",
        "Si-II",
        "O-I",
        "C-II",
        "C-II",
        "Si-IV",
        "O-IV]",
        "O-IV]",
        "Si-IV",
        "N-IV]",
        "C-IV",
        "C-IV",
        "He-II",
        "O-III]",
        "O-III]",
        "N-III]",
        "N-III]",
        "Al-III",
        "Al-III",
        "Si-III]",
        "C-III]",
        "N-II]",
        "[O-III]",
        "C-II]",
        "C-II]",
        "[Fe-XI]",
        "He-II",
        "[Mg-V]",
        "Mg-II]",
        "Mg-II]",
        "[Fe-IV]",
        "[Fe-IV]",
        "[Ar-IV]",
        "[Ar-IV]",
        "[Mg-V]",
        "He-I",
        "O-III",
        "He-I",
        "He-II",
        "O-III",
        "[Ne-V]",
        "[Ne-V]",
        "O-III",
        "[N-I]",
        "[N-I]",
        "He-I",
        "[Fe-VII]",
        "[Fe-VI]",
        "H19",
        "H18",
        "H17",
        "H16",
        "H15",
        "H14",
        "[O-II]",
        "[O-II]",
        "H13",
        "H12",
        "[Fe-VII]",
        "H11",
        "H10",
        "H9",
        "[Fe-V]",
        "[Ne-III]",
        "He-I",
        "H8",
        "[Fe-V]",
        "[Fe-V]",
        "[Ne-III]",
        "H\u03b5",
        "He-I",
        "[S-II]",
        "[Fe-V]",
        "[S-II]",
        "H\u03b4",
        "He-I",
        "Fe-II",
        "[Fe-V]",
        "Fe-II",
        "[Fe-V]",
        "[Fe-II]",
        "Fe-II",
        "O-II",
        "H\u03b3",
        "[O-III]",
        "[Ar-XIV]",
        "O-II",
        "Fe-II",
        "[Fe-II]",
        "He-I",
        "Fe-II",
        "Fe-II",
        "N-III",
        "Fe-II",
        "Fe-II",
        "Fe-II",
        "Fe-II",
        "Fe-II",
        "N-III",
        "N-III",
        "N-III",
        "C-III",
        "C-III",
        "C-III",
        "[Fe-III]",
        "He-II",
        "[Ar-IV]",
        "[Ar-IV]",
        "H\u03b2",
        "[Fe-VII]",
        "[Fe-IV]",
        "Fe-II",
        "[O-III]",
        "[O-III]",
        "Fe-II",
        "[Fe-III]",
        "[Fe-VI]",
        "[Fe-VII]",
        "Fe-II",
        "[Fe-VI]",
        "Fe-II",
        "[N-I]",
        "Fe-II",
        "[Fe-IV]",
        "[Fe-III]",
        "Fe-II",
        "[Fe-VII]",
        "[Fe-XIV]",
        "[Ca-V]",
        "Fe-II",
        "Fe-II",
        "[Fe-VI]",
        "[Fe-VI]",
        "[Cl-III]",
        "[Cl-III]",
        "[Fe-VI]",
        "[Fe-VI]",
        "C-III",
        "[Fe-VII]",
        "[N-II]",
        "C-IV",
        "C-IV",
        "He-I",
        "O-I",
        "[Fe-VII]",
        "[O-I]",
        "[S-III]",
        "Si-II",
        "[O-I]",
        "Fe-II",
        "[Fe-X]",
        "Fe-II",
        "[N-II]",
        "H\u03b1",
        "[N-II]",
        "[S-II]",
        "[S-II]",
        "O-I",
        "[Ar-V]",
        "He-I",
        "[Ar-III]",
        "[Fe-II]",
        "[Ar-IV]",
        "[Fe-II]",
        "C-II",
        "[Ar-IV]",
        "O-I",
        "[Ar-IV]",
        "He-I",
        "[O-II]",
        "[O-II]",
        "[Ni-II]",
        "[Ni-II]",
        "[Fe-II]",
        "N-I",
        "[S-XII]",
        "[Ar-III]",
        "He-I",
        "Ar-I",
        "[Ni-III]",
        "[Fe-XI]",
        "He-II",
        "Pa20",
        "Pa19",
        "Pa18",
        "O-I",
        "Pa17",
        "Ca-II",
        "Pa16",
        "Ca-II",
        "Pa15",
        "[Cl-II]",
        "Pa14",
        "[Fe-II]",
        "Ca-II",
        "Pa13",
        "N-I",
        "N-I",
        "N-I",
        "Pa12",
        "Pa11",
        "[Fe-II]",
        "Pa10",
        "[S-III]",
        "Pa9",
        "[S-III]",
        "Pa\u03b5",
        "[C-I]",
        "[C-I]",
        "[S-VIII]",
        "He-I",
        "He-I",
        "Pa\u03b4",
        "[S-II]",
        "[S-II]",
        "[S-II]",
        "[Fe-XIII]",
        "He-I",
        "Pa\u03b3"
    ]
}

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
        
        return 'Saved as .fits file: spectral_analysis_results.fits'

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
        return 'Saved as .fits file: spectral_analysis_results.fits'