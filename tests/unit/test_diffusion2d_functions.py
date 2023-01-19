"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import pytest


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    for i in range(1000):
        w = np.random.rand() * 100
        h = np.random.rand() * 100
        dx = np.random.rand()
        dy = np.random.rand()
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        assert solver.nx == w // dx
        assert solver.ny == h // dy


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    solver.w = 10.
    solver.h = 10.
    solver.dx = 0.1
    solver.dy = 0.1
    solver.nx = 100
    solver.ny = 100

    dx2, dy2 = solver.dx ** 2, solver.dy**2

    for i in range(1000):
        d = np.random.rand() * 100
        T_cold = np.random.rand() * 10000
        T_hot = np.random.rand() * 10000
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
        assert solver.D == d
        assert solver.T_cold == T_cold
        assert solver.T_hot == T_hot

        dt = pytest.approx(dx2 * dy2 / (2 * solver.D * (dx2 + dy2)), 0.01)
        assert solver.dt == dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.w = 10.
    solver.h = 10.
    solver.dx = 0.1
    solver.dy = 0.1
    solver.nx = 100
    solver.ny = 100

    solver.D = 4.
    solver.T_cold = 300.
    solver.T_hot = 700.
    solver.dt = 0.000625

    u = solver.set_initial_condition()
    assert u.shape == (100, 100)
    assert u.min() == solver.T_cold
    assert u.max() == solver.T_hot
    print(u)
