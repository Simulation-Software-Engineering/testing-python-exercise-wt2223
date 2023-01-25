"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest
import numpy as np


class TestDiffusion2D(unittest.TestCase):

    def setUp(self) -> None:
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=31., h=35., dx=0.1, dy=0.5)

        self.assertEqual(self.solver.nx, 310)
        self.assertEqual(self.solver.ny, 70)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=31., h=50., dx=0.1, dy=0.3)
        self.solver.initialize_physical_parameters(d=2.)
        expected_res = 0.00225

        self.assertAlmostEqual(self.solver.dt, expected_res)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.initialize_domain()
        self.solver.initialize_physical_parameters()
        u = self.solver.set_initial_condition()
        expected_u = 300. * np.ones((100, 100))

        for i in range(100):
            for j in range(100):
                if (i * self.solver.dx - 5) ** 2 + (j * self.solver.dy - 5) ** 2 < 4:
                    expected_u[i, j] = 700.

        self.assertTrue((u.all() == expected_u.all()))
