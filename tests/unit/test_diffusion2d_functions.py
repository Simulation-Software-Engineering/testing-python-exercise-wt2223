"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestDiffusion(TestCase):
    """
        Test suite for diffusion2D functions.
    """
    def setUp(self):
        self.w=15.
        self.h=12.
        self.dx=0.2
        self.dy=0.5
        self.d=2.
        self.T_cold= 100.
        self.T_hot= 300.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(self.w, self.h, self.dx, self.dy)
        self.assertEqual(solver.nx,75)
        self.assertEqual(solver.ny,24)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 2.
        solver.dy= 2.
        solver.initialize_physical_parameters(self.d, self.T_cold, self.T_hot)
        self.assertEqual(solver.dt,0.5)



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
        self.assertEqual(u[0, 0],100.)