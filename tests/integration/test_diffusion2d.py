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
    solver.initialize_domain(w=11.,h=12.,dx=2., dy=2.)
    solver.initialize_physical_parameters(d=2.,T_cold=100.,T_hot=300.)
    assert solver.dt== 0.5


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=15.,h=13.,dx=1., dy=1.)
    solver.initialize_physical_parameters(d=3.,T_cold=300.,T_hot=200.)
    u= solver.set_initial_condition()
    assert u[0][0]==300.