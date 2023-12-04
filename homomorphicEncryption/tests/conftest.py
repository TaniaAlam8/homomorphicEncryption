"""Unit tests configuration file."""

import logging 

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def pytest_configure(config):
    """Disable verbose output when running tests."""
    log.init(debug=True)

    terminal = config.pluginmanager.getplugin('terminal')
    terminal.TerminalReporter.showfspath = False
