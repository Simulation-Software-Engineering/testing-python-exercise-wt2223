"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    # w=3., h=2., dx=1, dy=0.5
    solver.initialize_domain(3., 2., 1., 0.5)

    # Expected results
    expected_nx = 3
    expected_ny = 4

    # Actual results
    actual_nx = solver.nx
    actual_ny = solver.ny

    assert expected_nx == actual_nx
    assert expected_ny == actual_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    # dx=1, dy=0.5
    # d=5., T_cold=200., T_hot=500.
    solver.dx, solver.dy = 1, 0.5
    solver.initialize_physical_parameters(5., 200., 500.)

    expected_dt = pytest.approx(0.02, abs=0.01)

    actual_dt = solver.dt

    assert expected_dt == actual_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    # nx=3, ny=4, T_cold=200
    solver.nx, solver.ny = 3, 4
    solver.dx, solver.dy = 1, 0.5
    solver.T_cold, solver.T_hot = 200, 500

    expected_u = 200 * np.ones((3,4))

    actual_u = solver.set_initial_condition()

    for i in range(3):
        for j in range(4):
            assert expected_u[i,j] == actual_u[i,j]
    