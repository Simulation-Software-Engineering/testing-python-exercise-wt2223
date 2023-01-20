"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import unittest


class TestDiffusion2D(unittest.TestCase):

    def setUp(self) -> None:
        self.solver = SolveDiffusion2D()

        return super().setUp()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        for i in range(10):
            w = np.random.rand() * 100
            h = np.random.rand() * 100
            dx = np.random.rand()
            dy = np.random.rand()
            self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
            self.assertEqual(self.solver.nx, w // dx)
            self.assertEqual(self.solver.ny, h // dy)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100

        dx2, dy2 = self.solver.dx ** 2, self.solver.dy**2

        for i in range(10):
            d = np.random.rand() * 100
            T_cold = np.random.rand() * 10000
            T_hot = np.random.rand() * 10000
            self.solver.initialize_physical_parameters(
                d=d, T_cold=T_cold, T_hot=T_hot)

            self.assertEqual(self.solver.D, d)
            self.assertEqual(self.solver.T_cold, T_cold)
            self.assertEqual(self.solver.T_hot, T_hot)

            dt = dx2 * dy2 / (2 * self.solver.D * (dx2 + dy2))
            self.assertAlmostEqual(self.solver.dt, dt, 5)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100
        self.solver.D = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
        self.solver.dt = 0.000625

        u = self.solver.set_initial_condition()
        self.assertEqual(u.shape, (100, 100))
        self.assertEqual(u.min(), self.solver.T_cold)
        self.assertEqual(u.max(), self.solver.T_hot)
