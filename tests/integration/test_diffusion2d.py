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
    w=40.
    h=20.
    dx=0.1
    dy=0.2
    D = 3.
    T_cold = 200.
    T_hot = 600.

    expected_dt = 1/750

    solver = SolveDiffusion2D()
    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    
    assert expected_dt == pytest.approx(solver.dt, abs=0.01)

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """

    w=40.
    h=20.
    dx=10.
    dy=10.
    D = 3.
    T_cold = 200.
    T_hot = 600.

    solver = SolveDiffusion2D()
    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    solver_u = solver.set_initial_condition()

    expected_u = T_cold * np.ones((solver.nx, solver.ny))
    
    assert np.array_equal(expected_u, solver_u)
