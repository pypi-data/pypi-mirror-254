"""
TiaC Systems Network (TSN) theme for Sphinx

From https://github.com/tiacsys/sphinx-tsn-theme
 and https://github.com/nrfconnect/doc-sphinx-ncs-theme
"""

import os

from sphinx.locale import _

try:
    # Avaliable from Sphinx 1.6
    from sphinx.util.logging import getLogger
except ImportError:
    from logging import getLogger


__version__ = "2024.1.0"
__version_full__ = __version__

logger = getLogger(__name__)


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def config_initiated(app, config):
    theme_options = config.html_theme_options or {}
    if not theme_options.get('default_docset'):
        logger.error(
            _('The default_docset option is not set.')
        )

def setup(app):
    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme(
        "sphinx_tsn_theme", os.path.abspath(os.path.dirname(__file__))
    )

    app.connect('config-inited', config_initiated)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
