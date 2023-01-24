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

    w = 12.
    h = 14.
    dx = 0.3
    dy = 0.4
    d = 2.
    T_cold = 200.
    T_hot = 700.

    solver.initialize_domain(w, h, dx, dy)

    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_dt = pytest.approx(0.0144, abs=0.001)

    assert expected_dt == solver.dt



def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    w = 12.
    h = 14.
    dx = 4.
    dy = 7.
    d = 2.
    T_cold = 200.
    T_hot = 700.

    solver.initialize_domain(w, h, dx, dy)

    solver.initialize_physical_parameters(d, T_cold, T_hot)

    u = solver.set_initial_condition()

    x = 2
    y = 3
    expected_u = np.array([[200. for i in range(x)] for j in range(y)])

    assert np.allclose(expected_u, u)
