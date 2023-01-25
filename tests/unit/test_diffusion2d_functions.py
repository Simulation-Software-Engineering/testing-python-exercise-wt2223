"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import unittest
import numpy as np

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()
        self.solver.dx = 2.
        self.solver.dy = 3.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        nx = 10
        ny = 5
        dx = 2.
        dy = 3.
        w = 20.0
        h = 15.0
        self.solver.initialize_domain(w = w, h = h, dx = dx, dy = dy)
        self.assertEqual(self.solver.nx, nx)
        self.assertEqual(self.solver.ny, ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        dx2, dy2 = 1, 4
        self.solver.dx, self.solver.dy = 1, 2
        d = 3.
        T_cold = 350.
        T_hot = 650.

        dt = pytest.approx(0.1333, abs = 0.0001)
        self.solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot = T_hot)
        self.assertEqual(self.solver.dt, dt)
        self.assertEqual(self.solver.dx * self.solver.dx, dx2)
        self.assertEqual(self.solver.dy * self.solver.dy, dy2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 300. 
        self.solver.T_hot = 700.
        self.solver.nx = 10
        self.solver.ny = 5
        test_op = [[300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.]]
        main_op = self.solver.set_initial_condition()
        self.assertTrue(np.array_equal(test_op, main_op))