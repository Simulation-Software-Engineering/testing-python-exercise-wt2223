"""
Tests for functionality checks in class SolveDiffusion2D
"""

from pytest import approx
import numpy as np

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=12.0, h=5.0, dx=0.12, dy=0.5)
    solver.initialize_physical_parameters(d=2.0, T_cold=350.0, T_hot=800.0)

    assert solver.dt == approx(0.0034039334341906197)

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=7.5, h=7.5, dx=1.25, dy=1.5)
    solver.initialize_physical_parameters(d=3.0, T_cold=200.0, T_hot=600.0)

    expected = 200.0 * np.ones((6, 5))
    for i in range(3, 6):
        for j in range(3, 5):
            expected[i][j] = 600.0

    result = solver.set_initial_condition()

    assert np.isclose(result, expected).all()
