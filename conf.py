project = 'deathbeds'
copyright = '2020, deathbeds'
author = 'deathbeds'
release = '0.0.0'
extensions = [
    "recommonmark",
    "nbsphinx"
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
source_suffix = [".rst", ".md", ".ipynb"]

nbsphinx_execute = 'never'
master_doc = 'readme'
def setup(app):
    app.add_css_file("css/custom.css")