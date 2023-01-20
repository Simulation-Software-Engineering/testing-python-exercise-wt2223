"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    w=20.
    h=20.
    dx=0.1
    dy=0.1
    expected_nx = 200
    expected_ny = 200
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=20.,dx=0.1,dy=0.1)
        
    assert expected_nx == solver.nx
    assert expected_ny == solver.ny

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    d=5. 
    T_cold=400. 
    T_hot=800.
    solver = SolveDiffusion2D()
    solver.dx=0.2
    solver.dy=0.2
    expected_dt = pytest.approx(0.002, abs=0.001)
    solver.initialize_physical_parameters(d=5., T_cold=400., T_hot=800.)
    assert expected_dt == solver.dt
    

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.nx = 10
    solver.ny = 10
    solver.d = 4.
    solver.T_cold = 300.
    solver.T_hot = 700.
    solver.dx=0.1
    solver.dy=0.1
    u = solver.set_initial_condition()
    expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 4, 10, 10
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = solver.T_hot
                    
    assert(u == expected_u).all()
        
