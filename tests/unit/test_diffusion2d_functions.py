"""
Tests for functions in class SolveDiffusion2D
"""

from ...diffusion2d import SolveDiffusion2D
import pytest


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
    solver.dx = 0.4
    solver.dy = 0.3
    d = 10.
    T_cold = 200.
    T_hot = 400.
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    exprected_dt = pytest.approx(0.00288, abs=0.00001)
    assert solver.dt == exprected_dt



def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.nx = 1
    solver.ny = 1
    solver.dx = 1
    solver.dy = 1
    solver.T_cold = 200.
    solver.T_hot = 400.
    u = solver.set_initial_condition()
    assert u[0, 0] == 200.