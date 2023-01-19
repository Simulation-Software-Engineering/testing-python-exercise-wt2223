"""
Tests for functions in class SolveDiffusion2D
"""

from pytest import approx
import numpy as np

from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20., h=15., dx=0.1, dy=0.2)

    assert solver.nx == 200
    assert solver.ny == 75


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.2
    solver.dy = 0.1
    solver.initialize_physical_parameters(d=5., T_cold=400.0, T_hot=600.0)

    assert solver.dt == approx(0.0008)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.T_cold = 400.0
    solver.T_hot = 600.0

    # this results in a 6x5 grid with the lower-most cell containing the center
    # of the circle
    solver.nx = 6
    solver.ny = 5
    solver.dx = 1.25
    solver.dy = 1.5

    expected = 400.0 * np.ones((6, 5))
    for i in range(3, 6):
        for j in range(3, 5):
            expected[i][j] = 600.0

    result = solver.set_initial_condition()

    assert np.isclose(result, expected).all()
