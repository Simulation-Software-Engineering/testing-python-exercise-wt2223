"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=4., dx=0.2, dy=0.2)

        self.assertEqual(self.solver.w, 5.)
        self.assertEqual(self.solver.h, 4.)
        self.assertEqual(self.solver.dx, 0.2)
        self.assertEqual(self.solver.dy, 0.2)
        self.assertEqual(self.solver.nx, 25)
        self.assertEqual(self.solver.ny, 20)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain()
        self.solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

        self.assertEqual(self.solver.D, 2.)
        self.assertEqual(self.solver.T_cold, 200.)
        self.assertEqual(self.solver.T_hot, 500.)
        self.assertAlmostEqual(self.solver.dt, 0.00125, 4)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.initialize_domain()
        self.solver.initialize_physical_parameters()
        u = self.solver.set_initial_condition()

        self.assertEqual(u[0, 0], 300)
        self.assertEqual(u[99, 99], 300)
        self.assertEqual(u[50, 50], 700)
