from pathlib import Path
from setuptools import setup, find_packages
from typing import List

def get_install_requires(filepath=None):
    if filepath is None:
        filepath = "./"
    """Returns requirements.txt parsed to a list"""
    fname = Path(filepath).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
            
    targets += get_links()
    return targets

def get_links():
    return [
        #"datasci_tools @ git+https://github.com/bacelii/datasci_tools.git'"
    ]

def get_long_description(filepath='README.md'):
    try:
        import pypandoc
        long_description = pypandoc.convert_file(filepath, 'rst') 
    except:
        print("\n\n\n****Need to install pypandoc (and if havent done so install apt-get install pandoc) to make long description clean****\n\n\n")
        
        long_description = Path("README.md").read_text()
        
    return long_description


setup(
    name='mesh_processing_tools', # the name of the package, which can be different than the folder when using pip instal
    version='1.0.4',
    description='Utility functions for mesh representation objects (like trimesh) and manipulations using 3rd party packages (CGAL, Meshlab, etc.)',
    #long_description=get_long_description(),
	project_urls={
	    'Source':"https://github.com/reimerlab/mesh_tools",
	    'Documentation':"https://reimerlab.github.io/mesh_tools/",
	},
	author='Brendan Celii',
	author_email='brendanacelii@gmail.com',
    packages=find_packages(),  #teslls what packages to be included for the install
    install_requires=get_install_requires(), #external packages as dependencies
    # dependency_links = get_links(),
    # if wanted to install with the extra requirements use pip install -e ".[interactive]"
    extras_require={
        #'interactive': ['matplotlib>=2.2.0', 'jupyter'],
    },
    
    # if have a python script that wants to be run from the command line
    entry_points={
        #'console_scripts': ['pipeline_download=Applications.Eleox_Data_Fetch.Eleox_Data_Fetcher_vp1:main']
    },
    scripts=[], 
    
)


