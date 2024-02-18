from setuptools import setup, find_packages

setup(
    name='SPEARS',
    version='0.1.1',
    author='Justin Domagala-Tang',
    author_email='justindomagalatang@hotmail.com',
    packages=find_packages(include=['SPEARS']),
    package_data={
        'SPEARS': ['SPEARS\data\environment_varuibles.json', 'SPEARS\data\spectral_line_info.json']
    },
    include_package_data=True,
    url='https://github.com/JustinD-T',
    keywords='SPARCL spectroscopy astonomy DESI-EDR NOIRLAB',
    license='LICENSE.txt',
    description='SPEARS : SPARCL Pipeline for Emission-Absorption Line Retrieval and Spectroscopy',
    long_description=open('README.txt').read(),
    install_requires=[
        'astropy==6.0.0',
        'numpy==1.26.3',
        'scipy==1.12.0',
        'sparclclient==1.2.1',
        'specutils==1.12.0',
        'Unidecode==1.3.8'
    ]
)
