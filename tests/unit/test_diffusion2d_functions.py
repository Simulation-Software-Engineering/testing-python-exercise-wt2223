"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=50., h=50., dx=0.05, dy=0.05)
    assert solver.nx == 1000 , "Wrong value for nx"
    assert solver.ny == 1000 , "Wrong value for ny"


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.1
    solver.initialize_physical_parameters(d=8., T_cold=200., T_hot=400.)
    
    assert solver.dt == pytest.approx(0.0003125, abs = 0.000001), "The value of dt is wrong"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.T_cold = 300
    solver.T_hot = 700
    solver.dx = 0.1
    solver.dy = 0.1
    solver.nx = 100
    solver.ny = 100
    u = solver.set_initial_condition()
    assert u.shape == (solver.nx, solver.ny), "The shape of the output is not correct"
    
    
