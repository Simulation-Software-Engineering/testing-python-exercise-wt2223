"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=12., dx=0.1, dy=0.2)
    solver.initialize_physical_parameters(d=6., T_cold=200., T_hot=600.)

    assert solver.dt == 0.0006666666666666669


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=0.2, h=0.5, dx=0.2, dy=0.5)
    solver.initialize_physical_parameters(d=6., T_cold=440., T_hot=840.)

    assert solver.set_initial_condition() == [[440.]]
