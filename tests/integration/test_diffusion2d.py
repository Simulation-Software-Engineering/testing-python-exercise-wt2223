"""
Tests for functionality checks in class SolveDiffusion2D
"""
import pytest
import numpy
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w = 1.0
    h = 20.0
    dx = 0.1
    dy = 0.5

    d = 11.
    T_cold = 3.
    T_hot = 1700.

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert solver.dt == pytest.approx(0.00043, abs = 1e-5)

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    w = 1.0
    h = 20.0
    dx = 0.1
    dy = 0.5

    nx = 10
    ny = 40

    d = 11.
    T_cold = 3.
    T_hot = 1700.

    u_expected = T_cold * numpy.ones((nx, ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u_expected[i, j] = T_hot

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    u_current = solver.set_initial_condition()

    assert numpy.allclose(u_current, u_expected)