"""
Tests for functions in class SolveDiffusion2D
"""

from ...diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 3.0
    h = 9.0
    dx = 0.4
    dy = 0.3
    solver.initialize_domain(w, h, dx, dy)
    assert solver.nx == 7
    assert solver.ny == 30



def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
