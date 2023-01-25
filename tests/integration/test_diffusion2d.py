"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=20., dx=5., dy=20.)
    solver.initialize_physical_parameters(d=1., T_cold=3., T_hot=2.)
    expected_dt = pytest.approx(11.76,abs=0.01)
    assert solver.dt == expected_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=20., dx=5., dy=20.)
    solver.initialize_physical_parameters(d=1., T_cold=3., T_hot=2.)
    expected_u = [[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,]]
    actual_u = solver.set_initial_condition()

    assert (expected_u == actual_u).all()