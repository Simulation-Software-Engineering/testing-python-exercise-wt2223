"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D

from unittest import TestCase

import numpy as np
from numpy.testing import assert_almost_equal


class TestDiffusion2D(TestCase):
    """
    TestSuite for the TestDiffusion2D module
    """

    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        # Default params
        self.solver.initialize_domain()
        self.assertEqual(self.solver.w, 10.)
        self.assertEqual(self.solver.h, 10.)
        self.assertEqual(self.solver.dx, 0.1)
        self.assertEqual(self.solver.dy, 0.1)
        self.assertEqual(self.solver.nx, 100)
        self.assertEqual(self.solver.ny, 100)

        # Some different params
        self.solver.initialize_domain(20., 40., 0.08, 0.1)
        self.assertEqual(self.solver.w, 20.)
        self.assertEqual(self.solver.h, 40.)
        self.assertEqual(self.solver.dx, 0.08)
        self.assertEqual(self.solver.dy, 0.1)
        self.assertEqual(self.solver.nx, 250)
        self.assertEqual(self.solver.ny, 400)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        # Default params
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters()
        self.assertEqual(self.solver.D, 4.)
        self.assertEqual(self.solver.T_cold, 300.)
        self.assertEqual(self.solver.T_hot, 700.)
        self.assertAlmostEqual(self.solver.dt, 0.0006250, 7)

        # Some different params
        self.solver.dx = 0.08
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters(10., 200., 800.)
        self.assertEqual(self.solver.D, 10.)
        self.assertEqual(self.solver.T_cold, 200.)
        self.assertEqual(self.solver.T_hot, 800.)
        self.assertAlmostEqual(self.solver.dt, 0.0001951, 7)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.dx = 1
        self.solver.dy = 2
        self.solver.nx = 10
        self.solver.ny = 5
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.

        expected_result = np.ones((10, 5))*300
        for i in range(4, 7):
            for j in range(2, 4):
                expected_result[i][j] = 700

        actual_result = self.solver.set_initial_condition()

        assert_almost_equal(actual_result, expected_result)
