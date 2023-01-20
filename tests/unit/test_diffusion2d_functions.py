"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest
import numpy as np

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()
        self.w = 3.
        self.h = 2.
        self.dx = 1.
        self.dy = 0.5
        self.nx = 3
        self.ny = 4
        self.T_cold = 200.
        self.T_hot = 500.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(3., 2., 1., 0.5)

        # Expected results
        expected_nx = self.nx
        expected_ny = self.ny

        # Actual results
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        self.assertEqual(expected_nx, actual_nx)
        self.assertEqual(expected_ny, actual_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx, self.solver.dy = self.dx, self.dy
        self.solver.initialize_physical_parameters(5., 200., 500.)

        expected_dt = 0.02

        actual_dt = self.solver.dt

        self.assertAlmostEqual(expected_dt, actual_dt, 2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.nx, self.solver.ny = self.nx, self.ny
        self.solver.dx, self.solver.dy = self.dx, self.dy
        self.solver.T_cold, self.solver.T_hot = self.T_cold, self.T_hot

        expected_u = self.T_cold * np.ones((self.nx, self.ny))

        actual_u = self.solver.set_initial_condition()

        for i in range(self.nx):
            for j in range(self.ny):
                self.assertEqual(expected_u[i,j], actual_u[i,j])
        
if __name__ == '__main__':
    unittest.main()