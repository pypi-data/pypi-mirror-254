# -*- coding: utf-8 -*-

"""CPU strain energy evaluator argument parser.

"""

from logging import getLogger


logger = getLogger(__package__)


def setup(parser):
    """Configure the parser for the module.

    Parameters
    ----------
    parser : ArgumentParser
        Parser dedicated to the module.

    """
    logger.debug("defining command-line arguments")
    parser.add_argument(
        '--z_uvw',
        help="direction of the line vector (uvw)",
        type=int,
        nargs=3,
        metavar='int',
    )
    parser.add_argument(
        '--b_uvw',
        help="direction of the Burgers vector (uvw)",
        type=int,
        nargs=3,
        metavar='int',
    )
    parser.add_argument(
        '--g_hkl',
        help="direction of the diffraction vector (hkl)",
        type=int,
        nargs=3,
        metavar='int',
    )
    parser.add_argument(
        '--cell',
        help="lattice constant (m)",
        type=float,
        metavar='float',
    )
    parser.add_argument(
        '--poisson',
        help="Poisson number",
        type=float,
        metavar='float',
    )
    parser.add_argument(
        '--shear',
        help="shear modulus (Pa)",
        type=float,
        metavar='float',
    )
    parser.add_argument(
        '--core',
        help="absolute or relative value of the core radius (1|m)",
        type=float,
        metavar='float',
    )
    parser.add_argument(
        '--absolute',
        action='store_true',
        help="if true, the core parameter becomes an absolute value",
    )
    parser.add_argument(
        '--replicate',
        help="number of replications of the region of interest",
        type=int,
        metavar='int',
    )
    parser.add_argument(
        '--points',
        help="number of random points",
        type=int,
        metavar='int',
    )
    parser.add_argument(
        '--processes',
        help="number of parallel processes",
        type=int,
        metavar='int',
    )
    parser.add_argument(
        '--check',
        action='store_const',
        const=True,
        help="display random points and replicated dislocations",
    )
