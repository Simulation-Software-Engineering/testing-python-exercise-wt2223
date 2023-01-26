"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from pytest import approx
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain( w=20., h=12., dx=0.5, dy=0.2)
    solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
    expected_dt = 0.00574
    assert expected_dt == approx(solver.dt, abs=1e-5)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain( w=20., h=12., dx=0.5, dy=0.2)
    T_cold = 200.
    solver.initialize_physical_parameters(d=3., T_cold=T_cold, T_hot=500.)
    u = solver.set_initial_condition()
    print(np.sum(u))
    excepted_u = np.ones((40, 60)) * T_cold
    assert u[0][0] == excepted_u[0][0], f'calculated u/initial condition should fe {excepted_u} but the function returned {u}'
