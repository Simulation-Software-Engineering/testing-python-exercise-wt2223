"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np

from diffusion2d import SolveDiffusion2D

from unittest import TestCase


class TestDiffusion2D(TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()


    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=20., h=15., dx=0.1, dy=0.2)

        self.assertEqual(self.solver.nx, 200)
        self.assertEqual(self.solver.ny, 75)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.2
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters(d=5., T_cold=400.0, T_hot=600.0)

        self.assertAlmostEqual(self.solver.dt, 0.0008)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.T_cold = 400.0
        self.solver.T_hot = 600.0

        # this results in a 6x5 grid with the lower-most cell containing the center
        # of the circle
        self.solver.nx = 6
        self.solver.ny = 5
        self.solver.dx = 1.25
        self.solver.dy = 1.5

        expected = 400.0 * np.ones((6, 5))
        for i in range(3, 6):
            for j in range(3, 5):
                expected[i][j] = 600.0

        result = self.solver.set_initial_condition()

        self.assertTrue(np.isclose(result, expected).all())
