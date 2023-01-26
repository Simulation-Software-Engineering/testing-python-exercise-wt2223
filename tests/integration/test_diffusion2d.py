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

    exp_h = 2.
    exp_w = 20.
    exp_dx = 0.1
    exp_dy = 0.1
    exp_d = 5.
    exp_t_cold = 400.
    exp_t_hot = 800.
    exp_dt = (exp_dx**2) * (exp_dy**2) / (2 * exp_d * ((exp_dx**2) + (exp_dy**2)))

    solver.initialize_domain(exp_h,exp_w,exp_dx,exp_dy)
    solver.initialize_physical_parameters(exp_d,exp_t_cold,exp_t_hot)
    assert solver.dt == exp_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    exp_w = 10.
    exp_h = 9.
    exp_dx = 5.
    exp_dy = 3.
    exp_nx = int(exp_w/exp_dx)
    exp_ny = int(exp_h/exp_dy)
    exp_d = 4.
    exp_t_cold = 300.
    exp_t_hot = 700.

    exp_u = exp_t_cold * np.ones((exp_nx, exp_ny))
    exp_r, exp_cx, exp_cy = 2, 5, 5
    exp_r2 = exp_r ** 2
    for i in range(exp_nx):
        for j in range(exp_ny):
            exp_p2 = (i * exp_dx - exp_cx) ** 2 + (j * exp_dy - exp_cy) ** 2
            if exp_p2 < exp_r2:
                exp_u[i, j] = exp_t_hot

    solver.initialize_domain(exp_w,exp_h,exp_dx,exp_dy)
    solver.initialize_physical_parameters(exp_d,exp_t_cold,exp_t_hot)
    assert (solver.set_initial_condition() == exp_u).all()
