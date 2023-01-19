"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 1.0, 2.0, 2.0, 2.0
    solver.initialize_domain(
        w=w, h=h, dx=dx, dy=dy
    )

    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy

    assert solver.nx == int(w / dx) + 1
    assert solver.ny == int(h / dy)


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = .1
    solver.dy = .1

    d, T_cold, T_hot = 4., 300., 700.
    solver.initialize_physical_parameters(
        d=d, T_cold=T_cold, T_hot=T_hot
    )

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.w = 10.
    solver.h = 10.
    solver.dx = 10.
    solver.dy = 10.
    solver.nx = int(solver.w / solver.dx)
    solver.ny = int(solver.h / solver.dy)

    solver.d = 4.
    solver.T_cold = 300.
    solver.T_hot = 700.

    res = solver.set_initial_condition()
    _res = np.full((1, 1), 300.)
    assert (res == _res).all()