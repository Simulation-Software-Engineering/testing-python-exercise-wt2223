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
    solver.initialize_domain(w=20., h=5., dx=0.5, dy=0.5)

    assert solver.w == 20
    assert solver.h == 5
    assert solver.dx == 0.5
    assert solver.dy == 0.5
    assert solver.nx == 40
    assert solver.ny == 10
    

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters(d=5., T_cold=200., T_hot=600.)

    assert solver.D == 5
    assert solver.T_cold == 200
    assert solver.T_hot == 600
    assert pytest.approx(solver.dt, abs=0.0001) == 0.0005


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters()
    u = solver.set_initial_condition()

    assert u[0,0] == 300
    assert u[99,99] == 300
    assert u[50,50] == 700

