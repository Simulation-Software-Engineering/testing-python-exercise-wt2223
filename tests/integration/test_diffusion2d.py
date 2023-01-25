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
    # Fixture
    solver = SolveDiffusion2D()
    d = 5.
    T_cold = 400.0
    T_hot = 600.0
    w = 20.
    h = 30.
    dx = 0.6
    dy = 0.7

    # Expected result
    dt_correct = 0.02075294117647059

    # Actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    # Test
    assert solver.dt == pytest.approx(dt_correct, 1e-8)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # Fixture
    solver = SolveDiffusion2D()
    d = 5.
    T_cold = 400.0
    T_hot = 600.0
    w = 1.2
    h = 2.1
    dx = 0.6
    dy = 0.7

    # Actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    u = solver.set_initial_condition()

    # Test
    assert isinstance(u, np.ndarray)
    assert u.ndim == 2
    assert u.shape[0] == 2
    assert u.shape[1] == 3
    for i in range(2):
        for j in range(3):
            assert u[i, j] == 400.0
