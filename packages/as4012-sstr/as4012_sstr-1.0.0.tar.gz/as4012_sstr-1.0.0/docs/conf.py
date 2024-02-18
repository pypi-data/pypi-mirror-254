# -- Project information -----------------------------------------------------
from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("as4012_sstr").version
except DistributionNotFound:
    __version__ = "unknown version"

# https://github.com/mgaitan/sphinxcontrib-mermaid/issues/72
import errno

import sphinx.util.osutil

sphinx.util.osutil.ENOENT = errno.ENOENT

project = "s4012_sstr"
copyright = "2024, Ian Czekala"
author = "Ian Czekala"

# The full version, including alpha/beta/rc tags
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_nb",
]

# add in additional files
source_suffix = {
    ".ipynb": "myst-nb",
    ".rst": "restructuredtext",
    ".myst": "myst-nb",
    ".md": "myst-nb",
}

myst_enable_extensions = ["dollarmath", "colon_fence", "amsmath"]

autodoc_member_order = "bysource"
# https://github.com/sphinx-doc/sphinx/issues/9709
# bug that if we set this here, we can't list individual members in the
# actual API doc
# autodoc_default_options = {"members": None}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/iancze/AS4012-MESA",
    "use_repository_button": True,
}

html_logo = "logo.png"
html_favicon = "favicon.ico"

master_doc = "index"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
html_js_files = ["https://buttons.github.io/buttons.js"]

nb_execution_mode = "cache"
nb_execution_timeout = -1
nb_execution_raise_on_error = True
# .ipynb are produced using Makefile on own terms,
# # both .md and executed .ipynb are kept in git repo
nb_execution_excludepatterns = ["**.ipynb_checkpoints"]
myst_heading_anchors = 3
