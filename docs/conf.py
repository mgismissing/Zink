# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Zink'
copyright = '2025, magnesium'
author = 'magnesium'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_favicon = '_favicon.png'
html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "linear-gradient(180deg,rgba(77, 111, 102, 1) 0%, rgba(35, 88, 83, 1) 50%, rgba(18, 61, 66, 1) 100%)",
        "color-brand-content": "linear-gradient(180deg,rgba(77, 111, 102, 1) 0%, rgba(35, 88, 83, 1) 50%, rgba(18, 61, 66, 1) 100%)"
    },
    "dark_css_variables": {
        "color-brand-primary": "linear-gradient(180deg,rgba(107, 191, 132, 1) 0%, rgba(91, 189, 153, 1) 100%);",
        "color-brand-content": "linear-gradient(180deg,rgba(107, 191, 132, 1) 0%, rgba(91, 189, 153, 1) 100%);"
    }
}