"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=54846., h=546., dx=0.3, dy=0.5)
    solver.initialize_physical_parameters(d=6., T_cold=400., T_hot=420.)

    expected = pytest.approx(0.00551, 0.001)
    assert solver.dt == expected


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(100., 100., 0.1, .1)
    solver.initialize_physical_parameters(4., 1., 1.)

    actual_u = solver.set_initial_condition()
    expected_u = np.ones((1000, 1000))
    assert np.array_equal(expected_u, actual_u)
