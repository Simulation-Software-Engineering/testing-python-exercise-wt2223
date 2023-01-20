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
    w, h, dx, dy = 3., 2., 1., 0.5
    d, T_cold, T_hot = 5., 200., 500.

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_dt = pytest.approx(0.02, 0.01)
    actual_dt = solver.dt
    assert expected_dt == actual_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    
    w, h, dx, dy = 3., 2., 1., 0.5
    d, T_cold, T_hot = 5., 200., 500.

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_u = T_cold * np.ones((solver.nx, solver.ny))

    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(3):
        for j in range(4):
            p2 = (i * 1 - cx) ** 2 + (j * 0.5 - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = 500.

    actual_u = solver.set_initial_condition()

    for i in range(3):
        for j in range(4):
            assert expected_u[i,j] == actual_u[i,j]