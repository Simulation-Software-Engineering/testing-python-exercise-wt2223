"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import pytest


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    solver.initialize_domain(w=31., h=31., dx=0.1, dy=0.6)
    solver.initialize_physical_parameters(d=2.)
    expected_res = pytest.approx(0.002432, 0.0001)

    assert solver.dt == expected_res


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters()
    u = solver.set_initial_condition()
    expected_u = 300. * np.ones((100, 100))

    for i in range(100):
        for j in range(100):
            if (i * solver.dx - 5) ** 2 + (j * solver.dy - 5) ** 2 < 4:
                expected_u[i, j] = 700.

    assert np.array_equal(u, expected_u)

