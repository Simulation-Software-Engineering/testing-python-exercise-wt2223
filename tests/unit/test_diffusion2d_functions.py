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
    nx = 30
    ny = 50
    solver.initialize_domain(w = 15.0, h = 20.0, dx = 0.5, dy = 0.4)
    assert solver.nx == nx
    assert solver.ny == ny

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    dx2, dy2 = 1, 4
    solver.dx, solver.dy = 1, 2
    dt = pytest.approx(0.1333, abs = 0.0001)
    solver.initialize_physical_parameters(d=3., T_cold=350., T_hot = 650.)
    assert solver.dt == dt
    assert solver.dx * solver.dx == dx2
    assert solver.dy * solver.dy == dy2

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.T_cold = 300. 
    solver.T_hot = 700.
    solver.nx = 5
    solver.ny = 5
    solver.dx = 2.
    solver.dy = 2.
    test_op = [[300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.],
                [300., 300., 700., 700., 300.], [300., 300., 700., 700., 300.],
                [300., 300., 300., 300., 300.]]
    main_op = solver.set_initial_condition()
    assert (main_op == test_op).all()