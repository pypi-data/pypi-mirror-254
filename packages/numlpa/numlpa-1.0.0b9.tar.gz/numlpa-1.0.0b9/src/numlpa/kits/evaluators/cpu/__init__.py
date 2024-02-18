# -*- coding: utf-8 -*-

"""CPU strain energy evaluator.

This implementation uses the Monte Carlo method to compute the strain
energy and is parallelized on the different cores of the CPU.

"""

from . import evaluation, parser


setup = parser.setup
evaluate = evaluation.evaluate
