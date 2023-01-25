"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D

from pytest import approx
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
    solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)

    expected_result = approx(0.000005714, abs=1e-7)

    assert solver.dt == expected_result


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=6., h=2., dx=2., dy=1.)
    solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
    u_actual = solver.set_initial_condition()

    u_expected = 300.0 * np.ones((3, 2))

    assert np.isclose(u_actual, u_expected).all()
