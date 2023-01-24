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
        w = 12.
        h = 14.
        dx = 0.3
        dy = 0.4

        self.solver.initialize_domain(w, h, dx, dy)

        expected_nx = 40.
        expected_ny = 35.

        self.assertEqual(dx, self.solver.dx)
        self.assertEqual(dy, self.solver.dy)
        self.assertAlmostEqual(expected_nx, self.solver.nx)
        self.assertAlmostEqual(expected_ny, self.solver.ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        d = 2.
        T_cold = 200.
        T_hot = 700.

        self.solver.dx = 0.3
        self.solver.dy = 0.4
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        expected_dt = 0.0144
        self.assertAlmostEqual(expected_dt, self.solver.dt)
        self.assertEqual(T_cold, self.solver.T_cold)
        self.assertEqual(T_hot, self.solver.T_hot)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.nx = 3
        self.solver.ny = 2
        self.solver.dx = 0.3
        self.solver.dy = 0.4
        self.solver.T_cold = 200.
        self.solver.T_hot = 700.

        actual_u = self.solver.set_initial_condition()
        expected_u = np.array([[200., 200.], [200., 200.], [200., 200.]])
        self.assertTrue(np.allclose(expected_u, actual_u))
