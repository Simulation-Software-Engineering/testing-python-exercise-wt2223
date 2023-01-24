"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=20., dx=0.5, dy=0.5)
    solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

    expected_dt = 0.03125
    actual_dt = solver.dt

    assert (actual_dt == expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=20., dx=0.5, dy=0.5)
    solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)
    actual_u = solver.set_initial_condition()

    T_cold = 200.
    T_hot = 500.
    dx, dy = 0.5, 0.5
    nx, ny = 10, 40

    expected_u = T_cold * np.ones((nx, ny))
    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot

    assert actual_u.all() == expected_u.all()
