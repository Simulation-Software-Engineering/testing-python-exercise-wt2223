"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    solver.initialize_domain(w=50.,h=50.,dx=0.05, dy=0.05)
    solver.initialize_physical_parameters(d=4.,T_cold=200.,T_hot=400.)
    assert solver.dt == pytest.approx(0.00015625, abs = 0.00001), "Wrong value for dt"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=50.,h=50.,dx=10., dy=10.)
    solver.initialize_physical_parameters(d=4.,T_cold=200.,T_hot=400.)
    
    u0 = [[200., 200., 200., 200., 200.],
            [200., 200., 200., 200., 200.],
            [200., 200., 200., 200., 200.],
            [200. ,200. ,200. ,200. ,200.],
            [200. ,200. ,200., 200. ,200.]]
    u = solver.set_initial_condition()
    assert (u == u0).all(), "wrong values for u"
