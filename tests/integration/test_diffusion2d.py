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
    w = 12.0
    h = 14.0
    dx = 0.3
    dy = 0.4
    d = 2.0
    T_cold = 250.0
    T_hot = 800.0

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    expected_dt = pytest.approx(0.0144, 0.01)

    assert solver.dt == expected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 0.6
    h = 12.0
    T_cold = 222.0
    T_hot = 555.0
    dx = 0.3
    dy = 4.0
    d = 5.0

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    expected_u = np.array([[222., 222., 222.], [222., 222., 222.]])

    actual_u = solver.set_initial_condition()

    assert np.array_equal(actual_u, expected_u)
