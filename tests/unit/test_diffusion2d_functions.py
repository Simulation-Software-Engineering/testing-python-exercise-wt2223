"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase
import numpy as np

class TestDiffusion2D(TestCase):

    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 12.
        h = 14.
        dx = 0.3
        dy = 0.4

        # Expected result
        expected_nx = 40. 
        expected_ny = 35. 

        self.solver.initialize_domain(w, h, dx, dy)

        # Actual result
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        # Test
        self.assertAlmostEqual(actual_nx, expected_nx, 2)
        self.assertAlmostEqual(actual_ny, expected_ny, 2)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.3
        self.solver.dy = 0.4
        d = 2.
        T_cold = 250.
        T_hot = 800.

        # Expected result
        expected_dt = 0.0144 

        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # Actual result
        actual_dt = self.solver.dt

        # Test
        self.assertAlmostEqual(actual_dt, expected_dt, 2)
        self.assertEqual(self.solver.D, d)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx = 2
        self.solver.ny = 3
        self.solver.T_cold = 222.
        self.solver.T_hot = 555.
        self.solver.dx = 0.3
        self.solver.dy = 0.4

        # Expected result
        expected_u = np.array([[222., 222., 222.], [222., 222., 222.]])

        # Actual result
        actual_u = self.solver.set_initial_condition()

        # Test
        self.assertTrue(np.array_equal(expected_u, actual_u))
