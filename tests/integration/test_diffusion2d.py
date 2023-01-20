"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    d = 1.0
    dx = 1.0
    dy = 2.0
    w = 1.0
    h = 2.0
    T_cold = 100
    T_hot = 500

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_value = 0.4
    assert expected_value == solver.dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    d = 1.0
    dx = 1.0
    dy = 2.0
    w = 1.0
    h = 4.0
    T_cold = 100
    T_hot = 500

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    actual_result = solver.set_initial_condition()

    expected_result = [[100.0, 100.0]]

    # numpy already has a suitable function to compare multi-dimensional arrays
    assert np.array_equal(expected_result, actual_result)


