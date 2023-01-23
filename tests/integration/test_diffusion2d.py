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

    #Fixture
    w =  10.5
    h = 7.3
    dx = 0.2
    dy = 0.2
    d = 3.
    T_cold = 400.
    T_hot = 800.

    #Expected Result
    expected_dt = pytest.approx(0.003, 0.2)

    #Actual Result
    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_dt = solver.dt

    #Tests
    assert expected_dt == actual_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    #Fixture
    w =  10.5
    h = 7.3
    dx = 0.2
    dy = 0.2
    d = 3.
    T_cold = 400.
    T_hot = 800.

    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    #Expected Result
    expected_u = T_cold * np.ones((solver.nx, solver.ny))

    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = 800.

    #Actual Result
    actual_u = solver.set_initial_condition()

    #Tests
    assert (expected_u==actual_u).all()
