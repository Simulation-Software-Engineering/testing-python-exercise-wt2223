"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import pytest


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=10.,dx=0.1,dy=0.2)
    solver.initialize_physical_parameters(d=5., T_cold=400., T_hot=800.)
    assert solver.dt == pytest.approx(0.0008)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5.,h=10.,dx=1.,dy=2.)
    solver.initialize_physical_parameters(d=5., T_cold=400., T_hot=800.)
    solver.nx = 5
    solver.ny = 5
    solver.d = 5.
    solver.T_cold = 400.
    solver.T_hot = 800.
    solver.dx=1
    solver.dy=2
    u = solver.set_initial_condition()
    expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = solver.T_hot
    assert(u == expected_u).all()
