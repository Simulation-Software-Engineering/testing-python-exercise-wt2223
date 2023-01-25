"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
from unittest import TestCase, main

class TestDiffusion2D(TestCase):
    """
    Test suite for functions in SolveDiffusion2D-class
    """

    def setUp(self):
        self.solver = SolveDiffusion2D()



    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)

        expected_ny = 200
        expected_nx = 250

        self.assertEqual(self.solver.ny, expected_ny)
        self.assertEqual(self.solver.nx, expected_nx)



    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
        self.solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)

        expected_result = 0.000005714

        self.assertAlmostEqual(self.solver.dt, expected_result, 7)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.initialize_domain(w=6., h=2., dx=2., dy=1.)
        self.solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
        u_actual = self.solver.set_initial_condition()

        u_expected = np.array([[300., 300.], [300., 300.], [300., 300.]])

        self.assertTrue(np.allclose(u_expected, u_actual))

