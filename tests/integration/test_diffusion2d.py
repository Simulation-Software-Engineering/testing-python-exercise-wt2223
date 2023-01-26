"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=50., h=1000., dx=0.1, dy=1.)
    solver.initialize_physical_parameters(d=2., T_cold=400., T_hot=600.)

    assert solver.dt == 0.0024752475247524757

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=1., h=1., dx=1., dy=1.)
    solver.initialize_physical_parameters(d=2., T_cold=350., T_hot=700.)

    assert solver.set_initial_condition() == [[350.]]
    
