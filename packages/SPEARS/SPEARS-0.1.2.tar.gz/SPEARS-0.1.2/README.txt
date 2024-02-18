===================================
 SPEARS - README
===================================

SPEARS - Sparcl Pipeline for Emission-Absorption Line Retrieval and Spectroscopy
--------------------------------------------------------------------------------

This library aims to provide users with a quick, and easily scalable pipeline for spectroscopic analysis of spectra from the DESI-EDR accessed through the SPARCL API at NOIRLAB. Provides a list of spectral lines present in a given spectrum, along with other information outlined in spectro_analyze header. Specific usage of each function can be found under Features.

Features
========

Main Functionality
------------------

- ``spectro_analyze(limit, save_as_fits=False)``: 
  Returns a list of QTables (or .fits file if specified) with the following headers:
  
    - 'Ion' (str): The ion type present
    - 'Ion Line Wavelength' (float64, angstrom): The wavelength of the present spectral line
    - 'Spectral Flux at Line' (float64, 1 / (erg17 cm2 s Angstrom)): The model-spectral flux at the given spectral line wavelength
    - 'Observed Deviation' (float64, angstrom): The distance from the observed spectral line and the actual line
    - 'Normalized Deviation' (float64, dimensionless): The observed deviation divided by the spectral resolution at that given wavelength
    - meta={'id'}: id of spectrum, identical to dict key

Sub-modules
-----------

- ``fetch_sparcl_ids(limit)``: Fetches the first n SPARCL ids, based on the limit provided.
- ``sparcl_ids_to_spectra(sparcl_ids)``: Takes SPARCL ids and returns a list of Spectrum1D objects with each spectra's flux, redshifted-accounted wavelength, and SPARCL id.
- ``normalize_spectra(model_spectra)``: Takes an array of Spectrum1D object(s) and returns the continuum normalized spectra for each (continuum derived by median-filter smoothing original spectrum).
- ``norm_spectra_to_lines(normalized_spectra, save_as_fits=False)``: Takes an array of normalized spectra, and returns the present spectral lines (and other info specified in spectro_analyze) in each in a list of QTables, or .fits file if specified.

Requirements
============

As listed in ``setup.py``:

- specutils
- numpy
- astropy
- json
- warnings
- scipy
- sparcl.client
- importlib
- pytest

Installation
============

.. code-block:: bash

    $ [sudo] pip install SPEARS

Usage
=====

Retrieving spectral analysis info from the first 5 spectra in the database:

.. code-block:: python

    from SPEARS import SPEARS

    sparcl_ids = SPEARS.fetch_sparcl_ids(limit=5)

    info = SPEARS.spectro_analyze(sparcl_ids)

Documentation
=============

Full documentation will be later uploaded to my `GitHub <https://github.com/JustinD-T>`_.

License
=======

See LICENSE.txt file.

Acknowledgments
===============

- Full accreditation can be found on my `GitHub <https://github.com/JustinD-T>`_.
- Thanks to NOIRLAB for supplying their vast spectral data for free through SPARCL API.

Contact
=======

Email: justindomagalatang@hotmail.com