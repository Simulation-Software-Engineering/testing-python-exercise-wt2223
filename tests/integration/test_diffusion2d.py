"""
Tests for functionality checks in class SolveDiffusion2D
"""
import random
import sys

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

    T_hot = float(random.randint(0, 1000))
    T_cold = float(random.randrange(T_hot))

    solver = SolveDiffusion2D()
    size = float(100)
    resolution = float(.1)
    solver.initialize_domain(size, size, resolution, resolution)

    solver.initialize_physical_parameters(4., T_cold, T_hot)

    actual_u = solver.set_initial_condition()

    assert np.max(actual_u) == T_hot
    assert np.min(actual_u) == T_cold

    hot_or_cold = np.bitwise_or(actual_u == T_hot, actual_u == T_cold)
    assert np.all(hot_or_cold)

    # check if the corners are cold
    assert actual_u[0, 0] == T_cold
    assert actual_u[0, -1] == T_cold
    assert actual_u[-1, 0] == T_cold
    assert actual_u[-1, -1] == T_cold
