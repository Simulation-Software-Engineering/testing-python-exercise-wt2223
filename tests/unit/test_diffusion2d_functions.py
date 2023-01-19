"""
Tests for functions in class SolveDiffusion2D
"""
import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20., h=12., dx=0.5, dy=0.2)
    excepted_nx, excepted_ny = 40, 60    
    assert solver.nx == excepted_nx, f'nx value should be {excepted_nx} but got {solver.nx}'
    assert solver.ny == excepted_ny, f'nx value should be {excepted_ny} but got {solver.ny}'
    
    


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.5
    solver.dy = 0.2
    solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
    calculated_dt = 0.0011
    expected_dt = pytest.approx(calculated_dt, abs=0.01)
    assert expected_dt == solver.dt , 'Assertion error'

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.nx = 5
    solver.ny = 5
    solver.D = 3.0
    solver.dx = 0.25
    solver.dy = 0.1
    solver.T_cold = 200.0
    solver.T_hot = 500.0
    #  According to the algorithm if I pass these values to the function it should give me numpy array with all the values equal to 200
    excepted_u = np.ones((5, 5)) * 200.0
    calculated_u = solver.set_initial_condition()
    assert calculated_u.shape == excepted_u.shape, f'output shape should be {calculated_u.shape} but got {excepted_u.shape}'
    assert np.array_equal(excepted_u,calculated_u), f'calculated u/initial condition should fe {excepted_u} but the function returned {calculated_u}'

    
    
