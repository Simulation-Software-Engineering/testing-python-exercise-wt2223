"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase
def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=15., h=12., dx=0.2, dy=0.5)
    assert solver.nx==75
    assert solver.ny==24
def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 2
    solver.dy= 2
    solver.initialize_physical_parameters(d=2., T_cold=100., T_hot=300.)
    assert solver.dt==0.5
def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.nx = 1
    solver.ny = 1
    solver.dx = 1
    solver.dy = 1
    solver.T_cold = 100.
    solver.T_hot = 300.
    u = solver.set_initial_condition()
    assert u[0, 0] == 100.
