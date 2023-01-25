"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 12.
    h = 14.
    dx = 0.3
    dy = 0.4    
    d = 2.
    T_cold = 250.
    T_hot = 800.

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    # Expected result
    expected_dt = pytest.approx(0.0144, abs=0.01) 

    # Actual result
    actual_dt = solver.dt

    # Test
    assert actual_dt == expected_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 0.6
    h = 12.
    dx = 0.3
    dy = 4.
    T_cold = 222.
    T_hot = 555.
    d = 2.

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    # Expected result
    expected_u = ([[222., 222., 222.], [222., 222., 222.]])

    # Actual result
    actual_u = solver.set_initial_condition()

    # Test
    assert np.array_equal(actual_u, expected_u)
