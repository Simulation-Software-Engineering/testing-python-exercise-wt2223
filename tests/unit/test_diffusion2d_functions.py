"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestOperations(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=40., h=30., dx=0.2, dy=0.2)
        self.assertEqual(self.solver.nx, 200)
        self.assertEqual(self.solver.ny,150)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 1.
        self.solver.dy = 1.
        self.solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=700.)
        self.assertEqual(self.solver.dt, 0.25)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx = 2
        self.solver.ny = 2
        self.solver.T_hot = 400.
        self.solver.T_cold = 300.
        self.solver.dx = 1.
        self.solver.dy = 1.
        u = self.solver.set_initial_condition()
        self.assertEqual(u[0, 0], 300.)
        self.assertEqual(u[0, 1], 300.)
        self.assertEqual(u[1, 0], 300.)
        self.assertEqual(u[1, 1], 300.)