"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

class TestDiffusion2D:
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        expected_nx = 1
        expected_ny = 1
        solver.initialize_domain( w=5., h=20., dx=5., dy=20.)
        assert solver.nx == expected_nx and solver.ny == expected_ny

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 5.
        solver.dy = 20.
        expected_dx2, expected_dy2 = 25., 400.
        expected_dt = pytest.approx(11.76,abs=0.01)

        solver.initialize_physical_parameters(d=1., T_cold=3., T_hot=2.)

        assert expected_dt == solver.dt


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx, solver.ny = 5, 5
        solver.dx, solver.dy = 5., 20.
        solver.T_cold, solver.T_hot = 3., 2.

        expected_u = [[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,]]

        actual_u = solver.set_initial_condition()

        assert (expected_u == actual_u).all()
