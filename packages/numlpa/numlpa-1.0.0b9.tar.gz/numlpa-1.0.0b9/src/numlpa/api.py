# -*- coding: utf-8 -*-

"""NumLPA application programming interface.

This module allows the user to launch the main features of the package
from a Python script.

"""

from numlpa import config
from numlpa.main.analyze import main as analyze
from numlpa.main.diffract import main as diffract
from numlpa.main.draw import main as draw
from numlpa.main.evaluate import main as evaluate
from numlpa.main.export import main as export
from numlpa.main.extract import main as extract
from numlpa.main.fit import main as fit
from numlpa.main.merge import main as merge

__all__ = [
    'analyze',
    'diffract',
    'draw',
    'evaluate',
    'export',
    'extract',
    'fit',
    'merge',
    'load_config',
]


def load_config(path):
    """Load a configuration file.

    Parameters
    ----------
    path : str
        Path to the configuration file.

    """
    with open(path, encoding='utf-8') as file:
        config.read_file(file)
