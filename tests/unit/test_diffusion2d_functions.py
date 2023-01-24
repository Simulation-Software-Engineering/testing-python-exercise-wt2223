"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np
import unittest


class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 12.0
        h = 14.0
        dx = 0.3
        dy = 0.4

        expected_result_nx = 40.0
        expected_result_ny = 35.0
        self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

        self.assertEqual(self.solver.nx, expected_result_nx)
        self.assertEqual(self.solver.ny, expected_result_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 12.0
        self.solver.h = 14.0
        self.solver.dx = 0.3
        self.solver.dy = 0.4
        d = 2.0
        T_cold = 250.0
        T_hot = 800.0

        expected_dt = 0.0144
        self.solver.initialize_physical_parameters(
            d=d, T_cold=T_cold, T_hot=T_hot)

        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
        self.assertAlmostEqual(self.solver.dt, expected_dt, 1)

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

        expected_u = np.array([[222., 222., 222.], [222., 222., 222.]])

        actual_u = self.solver.set_initial_condition()

        self.assertTrue(np.array_equal(actual_u, expected_u))
