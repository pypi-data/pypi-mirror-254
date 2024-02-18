# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HONyx'
copyright = '2023, Queiros, Artus, Queyroi'
author = 'Queiros, Artus, Queyroi'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autosummary",
        "sphinx.ext.autodoc",
        "sphinx.ext.doctest",
        "numpydoc",
        "sphinx.ext.mathjax"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_last_updated_fmt = "%b %d, %Y"


autosummary_generate = True


import sys
import os
print(os.path.abspath('../'))

                  
sys.path.insert(0, os.path.abspath('../honyx/algorithms/'))
sys.path.insert(0, os.path.abspath('../honyx/models/')) 
sys.path.insert(0, os.path.abspath('../honyx/')) 
sys.path.insert(0, os.path.abspath('../')) 
numpydoc_show_class_members = False 