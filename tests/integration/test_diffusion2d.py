"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D

import pytest

import numpy as np
from numpy.testing import assert_almost_equal


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    # Default params
    solver.initialize_domain()
    solver.initialize_physical_parameters()

    assert solver.dt == pytest.approx(0.0006250, abs=0.0000001)

    # Some different params
    solver.initialize_domain(20., 40., 0.08, 0.1)
    solver.initialize_physical_parameters(10., 200., 800.)

    assert solver.dt == pytest.approx(0.0001951, abs=0.0000001)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.initialize_domain(10., 10., 1., 2.)
    solver.initialize_physical_parameters(1., 300., 700.)

    expected_result = np.ones((10, 5))*300
    for i in range(4, 7):
        for j in range(2, 4):
            expected_result[i][j] = 700

    actual_result = solver.set_initial_condition()

    assert_almost_equal(actual_result, expected_result)
