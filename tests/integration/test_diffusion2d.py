"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
import pytest

from diffusion2d import SolveDiffusion2D


@pytest.fixture
def solver():
    return SolveDiffusion2D()


def test_initialize_physical_parameters(solver):
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver.initialize_domain(12., 18., 0.4, 0.4)
    solver.initialize_physical_parameters(8., 400., 800.)

    actual = solver.dt
    expected = 0.005
    assert actual == pytest.approx(expected, rel=0.000001)


def test_set_initial_condition(solver):
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver.initialize_domain(12., 18., 0.4, 0.4)
    solver.initialize_physical_parameters(8., 400., 800.)
    actual = solver.set_initial_condition()
    idx = np.array([8,  8,  8,  8,  9,  9,  9,  9,  9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
                    11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
                    14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16,
                    16, 17, 17, 17, 17])
    idy = np.array([11, 12, 13, 14,  9, 10, 11, 12, 13, 14, 15, 16,  9, 10, 11, 12, 13, 14, 15, 16,  8,  9, 10, 11, 12,
                    13, 14, 15, 16, 17,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
                    8, 9, 10, 11, 12, 13, 14, 15, 16, 17,  9, 10, 11, 12, 13, 14, 15, 16, 9, 10, 11, 12, 13, 14, 15, 16,
                    11, 12, 13, 14])
    expected = np.ones((30, 45))
    expected[:, :] = 400.
    expected[idx, idy] = 800.
    assert (actual == expected).all()
