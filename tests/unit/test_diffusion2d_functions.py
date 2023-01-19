"""
Tests for functions in class SolveDiffusion2D
"""

from ...diffusion2d import SolveDiffusion2D
import pytest
from unittest import TestCase
class TestDiffusion2D(TestCase):
    """
    Tests for functions in class SolveDiffusion2D
    """

    def setUp(self) -> None:
        self.w = 3.0
        self.h = 9.0
        self.dx = 0.4
        self.dy = 0.3
        self.d = 10.
        self.T_cold = 200.
        self.T_hot = 400.
    
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(self.w, self.h, self.dx, self.dy)
        self.assertEqual(solver.nx, 7)
        self.assertEqual(solver.ny, 30)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = self.dx
        solver.dy = self.dy
        solver.initialize_physical_parameters(self.d, self.T_cold, self.T_hot)
        exprected_dt = pytest.approx(0.00288, abs=0.00001)
        self.assertEqual(solver.dt, exprected_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 1
        solver.ny = 1
        solver.dx = 1
        solver.dy = 1
        solver.T_cold = self.T_cold
        solver.T_hot = self.T_hot
        u = solver.set_initial_condition()
        self.assertEqual(u[0, 0], self.T_cold)