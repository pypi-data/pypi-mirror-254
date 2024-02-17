# -*- coding: utf-8 -*-

"""CPU strain energy evaluator implementation.

"""

from json import loads
from logging import getLogger
from math import isclose
from multiprocessing import Pool, RawArray
from os import cpu_count
from time import time

import matplotlib.pyplot as plt
import numpy as np

from numlpa import config
from . import strainstress


logger = getLogger(__package__)

shared = {}


def evaluate(sample, **kwargs):
    """Return the strain energy evaluation.

    Parameters
    ----------
    sample : dict
        Dislocation sample data.

    Keyword Arguments
    -----------------
    z_uvw : tuple of int
        Direction of the line vector (uvw).
    b_uvw : tuple of int
        Direction of the Burgers vector (uvw).
    g_hkl : tuple of int
        Direction of the diffraction vector (hkl).
    cell : float
        Lattice constant (m).
    poisson : float
        Poisson number.
    shear : float
        Shear modulus (Pa).
    core : float
        Absolute or relative value of the core radius (1|m).
    absolute : bool
        If true, the core parameter becomes an absolute value.
    replicate : int
        Number of replications of the region of interest.
    points : int
        Number of random points.
    processes : int
        Number of parallel processes.
    check : bool
        Display random points and replicated dislocations.

    Returns
    -------
    dict
        Energy evaluation data.

    """
    settings = {}
    share = {}
    times = {}
    result = {}

    check_parameters(kwargs)
    prepare_settings(sample, kwargs, settings)
    prepare_shared_data(sample, settings, share)
    user_check(settings, share, kwargs)
    run_monte_carlo(settings, share, result, times)
    return assemble_data(sample, settings, kwargs, result, times)


def check_parameters(kwargs):
    """Set the default configuration value to missing parameters.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments passed to the main function.

    """
    logger.debug("retrieving parameters")
    kwargs.setdefault('z_uvw', loads(config.get(__package__, 'z_uvw')))
    kwargs.setdefault('b_uvw', loads(config.get(__package__, 'b_uvw')))
    kwargs.setdefault('g_hkl', loads(config.get(__package__, 'g_hkl')))
    kwargs.setdefault('cell', config.getfloat(__package__, 'cell'))
    kwargs.setdefault('poisson', config.getfloat(__package__, 'poisson'))
    kwargs.setdefault('shear', config.getfloat(__package__, 'shear'))
    kwargs.setdefault('core', config.getfloat(__package__, 'core'))
    kwargs.setdefault('absolute', config.getboolean(__package__, 'absolute'))
    kwargs.setdefault('replicate', config.getint(__package__, 'replicate'))
    kwargs.setdefault('points', config.getint(__package__, 'points'))
    kwargs.setdefault('processes', config.getint(__package__, 'processes'))
    kwargs.setdefault('check', config.getboolean(__package__, 'check'))
    if kwargs['processes'] < 1:
        kwargs['processes'] = cpu_count()


def unit_vector(vector):
    """Return the normalized vector.

    Parameters
    ----------
    vector : np.ndarray or list or tuple
        Vector to be normalized.

    Returns
    -------
    np.ndarray
        Normalized vector.

    """
    return np.array(vector) / np.linalg.norm(vector)


def prepare_settings(sample, kwargs, settings):
    """Prepare the evaluation variables.

    Parameters
    ----------
    sample : dict
        Dislocation sample data.
    kwargs : dict
        Keyword arguments passed to the main function.
    settings : dict
        Evaluation variables.

    """
    logger.debug("defining the number of dislocations")
    settings['n_roi'] = len(sample['dislocations']['senses'])
    settings['n_all'] = settings['n_roi'] * (2*kwargs['replicate'] + 1)**2

    logger.debug("drawing random points")
    settings['n_p'] = kwargs['points']
    settings['m_x'], settings['m_y'] = random_points(sample, settings['n_p'])

    logger.debug("adding some parameters")
    settings['replicate'] = kwargs['replicate']
    settings['b_len'] = np.linalg.norm(kwargs['b_uvw']) * kwargs['cell']/2
    settings['poisson'] = kwargs['poisson']
    settings['shear'] = kwargs['shear']
    settings['processes'] = kwargs['processes']
    settings['density'] = sample['distribution']['density']
    settings['core'] = kwargs['core']
    if not kwargs['absolute']:
        settings['core'] *= settings['b_len']
    settings['factor'] = (
        4 * np.pi /
        settings['shear'] /
        settings['b_len']**2 /
        settings['density']
    )
    settings['cst_stress'] = settings['shear']*settings['b_len'] / (2*np.pi)
    settings['cst_strain'] = settings['b_len'] / (4*np.pi)

    logger.debug("retrieving vector in crystal lattice frame")
    settings['z_uni_rf2'] = unit_vector(kwargs['z_uvw'])
    settings['b_uni_rf2'] = unit_vector(kwargs['b_uvw'])
    settings['g_uni_rf2'] = unit_vector(kwargs['g_hkl'])

    logger.debug("identifying dislocation type")
    settings['abs_ang_z_b'] = np.abs(np.arccos(np.dot(
        settings['z_uni_rf2'],
        settings['b_uni_rf2'],
    )))
    if isclose(settings['abs_ang_z_b'], np.pi/2, abs_tol=1e-4):
        settings['type'] = 'edge'
        settings['x_uni_rf2'] = settings['b_uni_rf2']
        settings['cst_stress'] /= 1 - settings['poisson']
        settings['cst_strain'] /= 1 - settings['poisson']
        settings['factor'] *= 1 - settings['poisson']
        settings['function'] = fields_edge
    elif isclose(settings['abs_ang_z_b'], 0, abs_tol=1e-4):
        settings['type'] = 'screw'
        settings['x_uni_rf2'] = unit_vector(np.cross(
            settings['z_uni_rf2'],
            settings['g_uni_rf2'],
        ))
        settings['function'] = fields_screw
    else:
        raise NotImplementedError("mixed dislocations")

    logger.debug("preparing the change of reference frame")
    settings['y_uni_rf2'] = np.cross(
        settings['z_uni_rf2'],
        settings['x_uni_rf2'],
    )
    settings['transition'] = np.array((
        settings['x_uni_rf2'],
        settings['y_uni_rf2'],
        settings['z_uni_rf2'],
    ))

    logger.debug("defining vectors in dislocation frame")
    settings['g_uni_rf1'] = settings['transition'].dot(settings['g_uni_rf2'])


def prepare_shared_data(sample, settings, share):
    """Initialize and fill the shared containers.

    Parameters
    ----------
    sample : dict
        Dislocation sample data.
    settings : dict
        Evaluation variables.
    share : dict
        Shared data.

    """
    wrap = {}

    logger.debug("declaring shared data")
    share['poisson'] = settings['poisson']
    share['core'] = settings['core']
    share['cst_stress'] = settings['cst_stress']
    share['cst_strain'] = settings['cst_strain']
    share['d_x'] = RawArray('d', settings['n_all'])
    share['d_y'] = RawArray('d', settings['n_all'])
    share['d_s'] = RawArray('b', settings['n_all'])
    share['m_x'] = RawArray('d', settings['n_p'])
    share['m_y'] = RawArray('d', settings['n_p'])
    share['keep'] = RawArray('b', settings['n_p'])
    for sub in ('xx', 'yy', 'zz', 'xy', 'yz', 'zx'):
        for tensor in ('strain', 'stress'):
            share[f'{tensor}_{sub}'] = RawArray('d', settings['n_p'])

    logger.debug("wrapping shared data")
    wrap['d_x'] = np.frombuffer(share['d_x'], dtype=np.float64)
    wrap['d_y'] = np.frombuffer(share['d_y'], dtype=np.float64)
    wrap['d_s'] = np.frombuffer(share['d_s'], dtype=np.int8)
    wrap['m_x'] = np.frombuffer(share['m_x'], dtype=np.float64)
    wrap['m_y'] = np.frombuffer(share['m_y'], dtype=np.float64)
    wrap['keep'] = np.frombuffer(share['keep'], dtype=np.int8)
    for sub in ('xx', 'yy', 'zz', 'xy', 'yz', 'zx'):
        for tensor in ('strain', 'stress'):
            wrap[f'{tensor}_{sub}'] = np.frombuffer(
                share[f'{tensor}_{sub}'],
                dtype=np.float64,
            )

    logger.debug("defining shared data")
    wrap['d_x'][0:settings['n_roi']] = sample['dislocations']['positions'][0]
    wrap['d_y'][0:settings['n_roi']] = sample['dislocations']['positions'][1]
    wrap['d_s'][0:settings['n_roi']] = sample['dislocations']['senses']
    if settings['replicate'] > 0:
        if sample['region']['type'] != 'square':
            raise TypeError("can only apply replication on a square region")
        for i, (k_x, k_y) in enumerate(shift_indexes(settings['replicate'])):
            j = (i+1) * settings['n_roi']
            k = (i+2) * settings['n_roi']
            wrap['d_x'][j:k] = k_x * sample['region']['side']
            wrap['d_y'][j:k] = k_y * sample['region']['side']
            wrap['d_x'][j:k] += wrap['d_x'][0:settings['n_roi']]
            wrap['d_y'][j:k] += wrap['d_y'][0:settings['n_roi']]
            wrap['d_s'][j:k] = wrap['d_s'][0:settings['n_roi']]
    wrap['m_x'][:] = settings['m_x']
    wrap['m_y'][:] = settings['m_y']
    wrap['keep'][:] = 0
    for sub in ('xx', 'yy', 'zz', 'xy', 'yz', 'zx'):
        for tensor in ('strain', 'stress'):
            wrap[f'{tensor}_{sub}'][:] = 0


def user_check(settings, share, kwargs):
    """Display random points and replications if requested by the user.

    Parameters
    ----------
    settings : dict
        Evaluation variables.
    share : dict
        Shared data.
    kwargs : dict
        Keyword arguments passed to the main function.

    """
    logger.debug("checking random points and replicated dislocations")
    if kwargs['check']:
        fig, axes = plt.subplots()
        axes.scatter(share['d_x'], share['d_y'], label='dislocations')
        axes.scatter(*settings['points'].T, label='random points')
        axes.set_aspect(1)
        axes.set_xlabel("$x$ (m)")
        axes.set_ylabel("$y$ (m)")
        axes.legend()
        plt.show()
        plt.close(fig)


def assemble_data(sample, settings, kwargs, result, times):
    """Return the energy evaluation data.

    Parameters
    ----------
    sample : dict
        Dislocation sample data.
    settings : dict
        Evaluation variables.
    kwargs : dict
        Keyword arguments passed to the main function.
    results : dict
        Energy evaluation results.
    times : dict
        Time measurements.

    Returns
    -------
    dict
        Energy evaluation data.

    """
    logger.debug("assembling data")
    data = {
        'distribution': sample['distribution'],
        'region': sample['region'],
        'evaluation': {
            'module': __package__,
            'z_uvw': kwargs['z_uvw'],
            'b_uvw': kwargs['b_uvw'],
            'g_hkl': kwargs['g_hkl'],
            'type': settings['type'],
            'cell': kwargs['cell'],
            'b_len': settings['b_len'],
            'poisson': kwargs['poisson'],
            'shear': kwargs['shear'],
            'core': settings['core'],
            'energy_mean': result['energy_mean'],
            'energy_deviation': result['energy_deviation'],
            'square_strain': result['eps0'],
            'factor': settings['factor'],
            'cutoff': result['cutoff'],
            'samples': 1,
            'replicate': kwargs['replicate'],
            'duration': times['1'] - times['0'],
            'points': kwargs['points'],
            'processes': kwargs['processes'],
            'hidden': kwargs['points'] - int(result['kept']),
        },
    }
    return data


def run_monte_carlo(settings, share, result, times):
    """Run the Monte Carlo method.

    Parameters
    ----------
    settings : dict
        Evaluation variables.
    share : dict
        Shared data.
    results : dict
        Evaluation results.
    times : dict
        Time measurements.

    """
    logger.debug("computing strain and stress fields")
    times['0'] = time()
    with Pool(
        settings['processes'],
        initializer=initializer,
        initargs=(share,),
    ) as pool:
        pool.map(settings['function'], range(settings['n_p']))
    times['1'] = time()

    logger.debug("processing output")
    result['kept'] = sum(share['keep'])
    result['keep'] = np.frombuffer(share['keep'], dtype=np.uint8).astype(bool)
    for sub in ('xx', 'yy', 'zz', 'xy', 'yz', 'zx'):
        for tensor in ('strain', 'stress'):
            result[f'{tensor}_{sub}'] = np.frombuffer(
                share[f'{tensor}_{sub}'],
                dtype=np.float64,
            )[result['keep']]
    result['energy_all'] = (
        result['stress_xx'] * result['strain_xx'] +
        result['stress_yy'] * result['strain_yy'] +
        result['stress_zz'] * result['strain_zz'] +
        result['stress_xy'] * result['strain_xy'] * 2 +
        result['stress_yz'] * result['strain_yz'] * 2 +
        result['stress_zx'] * result['strain_zx'] * 2
    ) / 2
    result['energy_mean'] = np.mean(result['energy_all'])
    result['energy_deviation'] = np.std(result['energy_all'])
    result['cutoff'] = settings['core'] * np.exp(
        settings['factor'] * result['energy_mean']
    )
    result['g'] = settings['g_uni_rf1']
    result['eps0'] = np.square(
        result['g'][0] * result['strain_xx'] * result['g'][0] +
        result['g'][1] * result['strain_yy'] * result['g'][1] +
        result['g'][2] * result['strain_zz'] * result['g'][2] +
        result['g'][0] * result['strain_xy'] * result['g'][1] * 2 +
        result['g'][1] * result['strain_yz'] * result['g'][2] * 2 +
        result['g'][2] * result['strain_zx'] * result['g'][0] * 2
    ).mean()


def initializer(share):
    """Initialize a worker.

    Parameters
    ----------
    share : dict
        Shared data to be passed to the worker.

    """
    shared.update(share)


def shift_indexes(replications):
    """Return the indexes for the replications of the roi.

    Parameters
    ----------
    replications : int
        Number of replications around the region of interest.

    Returns
    -------
    list of tuple
        Replications indexes.

    """
    indexes = []
    for i in range(1, replications+1):
        for j in range(2*i):
            for k in (1, -1):
                indexes.append((-i*k, (i-j)*k))
                indexes.append(((i-j)*k,  i*k))
    return indexes


def random_points(sample, number):
    """Return the position of the random points.

    Parameters
    ----------
    sample : dict
        Dislocation sample data.
    number : int
        Number of random points in the region of interest.

    Returns
    -------
    np.array
        Position of the random points.

    """
    rng = np.random.default_rng(sample['distribution']['seed'])
    if sample['region']['type'] == 'square':
        side = sample['region']['side']
        positions = rng.random((number, 2), np.float64) * side
    elif sample['region']['type'] == 'disk':
        phi = 2 * np.pi * rng.random(number)
        rad = sample['region']['radius'] * np.sqrt(rng.random(number))
        return np.stack((rad*np.cos(phi), rad*np.sin(phi)), axis=1)
    else:
        raise NotImplementedError("unknown region type")
    return positions.T


def fields_screw(index):
    """Compute the strain and stress fields at the given point.

    Parameters
    ----------
    index : int
        Index of the random point.

    """
    strainstress.screw(
        shared['core'],
        shared['cst_stress'],
        shared['cst_strain'],
        shared['d_x'],
        shared['d_y'],
        shared['d_s'],
        shared['m_x'],
        shared['m_y'],
        shared['keep'],
        shared['stress_xx'],
        shared['stress_yy'],
        shared['stress_zz'],
        shared['stress_xy'],
        shared['stress_yz'],
        shared['stress_zx'],
        shared['strain_xx'],
        shared['strain_yy'],
        shared['strain_zz'],
        shared['strain_xy'],
        shared['strain_yz'],
        shared['strain_zx'],
        index,
    )


def fields_edge(index):
    """Compute the strain and stress fields at the given point.

    Parameters
    ----------
    index : int
        Index of the random point.

    """
    strainstress.edge(
        shared['poisson'],
        shared['core'],
        shared['cst_stress'],
        shared['cst_strain'],
        shared['d_x'],
        shared['d_y'],
        shared['d_s'],
        shared['m_x'],
        shared['m_y'],
        shared['keep'],
        shared['stress_xx'],
        shared['stress_yy'],
        shared['stress_zz'],
        shared['stress_xy'],
        shared['stress_yz'],
        shared['stress_zx'],
        shared['strain_xx'],
        shared['strain_yy'],
        shared['strain_zz'],
        shared['strain_xy'],
        shared['strain_yz'],
        shared['strain_zx'],
        index,
    )
