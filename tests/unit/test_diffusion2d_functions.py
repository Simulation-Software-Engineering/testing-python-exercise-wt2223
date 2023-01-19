"""
Tests for functions in class SolveDiffusion2D
"""
import pytest
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=4., dx=0.2, dy=0.2)

    assert solver.w == 5.
    assert solver.h == 4.
    assert solver.dx == 0.2
    assert solver.dy == 0.2
    assert solver.nx == 25
    assert solver.ny == 20
    


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

    assert solver.D == 2.
    assert solver.T_cold == 200.
    assert solver.T_hot == 500.
    assert  pytest.approx(solver.dt, 0.0001) == 0.00125


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters()
    actual = solver.set_initial_condition()

    assert actual[0, 0] == 300.