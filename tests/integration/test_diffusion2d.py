"""
Tests for functionality checks in class SolveDiffusion2D
"""

from pytest import approx
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(
        w=10., h=10., dx=10., dy=10.
    )
    solver.initialize_physical_parameters(
        d=3., T_cold=300., T_hot=700.
    )
    expected_dt = 8.33333
    assert expected_dt == approx(solver.dt, abs=1e-5)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    T_cold = 300.

    solver = SolveDiffusion2D()
    solver.initialize_domain(
        w=10., h=10., dx=10., dy=10.
    )
    solver.initialize_physical_parameters(
        d=3., T_cold=T_cold, T_hot=700.
    )
    u = solver.set_initial_condition()

    assert u[0][0] == T_cold
