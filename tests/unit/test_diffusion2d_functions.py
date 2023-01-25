"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest
import numpy as np

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 1
        expected_ny = 1
        self.solver.initialize_domain( w=5., h=20., dx=5., dy=20.)
        self.assertEqual(self.solver.nx,expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 5.
        self.solver.dy = 20.
        expected_dx2, expected_dy2 = 25., 400.
        expected_dt = 11.76

        self.solver.initialize_physical_parameters(d=1., T_cold=3., T_hot=2.)

        self.assertAlmostEqual(expected_dt, self.solver.dt,2)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx, self.solver.ny = 5, 5
        self.solver.dx, self.solver.dy = 5., 20.
        self.solver.T_cold, self.solver.T_hot = 3., 2.

        expected_u = [[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,]]

        actual_u = self.solver.set_initial_condition()

        self.assertTrue(np.array_equal(expected_u, actual_u))