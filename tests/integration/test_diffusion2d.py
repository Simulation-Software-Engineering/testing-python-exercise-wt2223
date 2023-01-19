"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=40., h=30., dx=1., dy=1.)
    solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=700.)
    assert solver.dt == 0.25


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=2., h=2., dx=1., dy=1.)
    solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=400.)
    u = solver.set_initial_condition()
    assert u[0,0] == 300.
    assert u[0,1] == 300.
    assert u[1,0] == 300.
    assert u[1,1] == 300.