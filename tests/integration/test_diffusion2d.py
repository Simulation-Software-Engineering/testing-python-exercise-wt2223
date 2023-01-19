"""
Tests for functionality checks in class SolveDiffusion2D
"""

import numpy as np
from ...diffusion2d import SolveDiffusion2D
import pytest


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 3.0
    h = 9.0
    dx = 0.4
    dy = 0.3
    d = 10.
    T_cold = 200.
    T_hot = 400.
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    exprected_dt = pytest.approx(0.00288, abs=0.00001)
    assert solver.dt == exprected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    T_cold = 200.
    T_hot = 400.
    w = 3.0
    h = 9.0
    nx = 7
    ny = 30
    d = 10.
    dx = 0.4
    dy = 0.3
    
    expected_u = T_cold * np.ones((nx, ny))
    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot

    solver = SolveDiffusion2D()
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_u = solver.set_initial_condition()
    assert np.allclose(actual_u, expected_u)
