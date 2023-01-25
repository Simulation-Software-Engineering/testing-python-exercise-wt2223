"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=15.,dx=2., dy=3.)
    solver.initialize_physical_parameters(d=3.,T_cold=350.,T_hot=650.)
    assert solver.dt== 0.46153846153846156

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=15.,dx=2., dy=3.)
    solver.initialize_physical_parameters(d=3.,T_cold=300.,T_hot=700.)
    test_op = [[300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.]]
    generated_op = solver.set_initial_condition()
    assert (test_op == generated_op).all()
