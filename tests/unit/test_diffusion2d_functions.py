"""
Tests for functions in class SolveDiffusion2D
"""
import numpy
import unittest

from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):

        self.solver.initialize_domain(w = 10., h = 20., dx = 0.1, dy = 0.1)

        expected_val_nx = 100
        expected_val_ny = 200

        self.assertEqual(self.solver.nx, expected_val_nx)
        self.assertEqual(self.solver.ny, expected_val_ny)

    def test_initialize_physical_parameters(self):

        solver = SolveDiffusion2D()

        expected_value = 0.00062

        self.solver.initialize_domain(w = 10., h = 10., dx = 0.1, dy = 0.1)
        self.solver.initialize_physical_parameters(d = 4., T_cold = 300., T_hot = 700.)

        self.assertAlmostEqual(self.solver.dt, expected_value, 4)

    def test_set_initial_condition(self):

        self.solver.initialize_domain(w=0.5, h=0.5, dx=0.1, dy=0.1)
        self.solver.initialize_physical_parameters(d = 4., T_cold = 300., T_hot = 700.)
        u_current = self.solver.set_initial_condition()
        u_expected = numpy.array([[300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.]])

        self.assertTrue(numpy.allclose(u_expected, u_current))