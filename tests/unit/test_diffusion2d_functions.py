"""
Tests for functions in class SolveDiffusion2D
"""
import unittest

from diffusion2d import SolveDiffusion2D
import numpy as np


class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        solver = SolveDiffusion2D()
        self.solver = solver
        # note that more functionality could be moved into setup but this would make understanding
        # of the tests more difficult. We want the parameters relevant for a test to be within the test itself

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # arrange
        solver = self.solver
        solver.dx = 1.0
        solver.dy = 2.0

        d = 1.
        T_cold = 100
        T_hot = 500

        # act
        solver.initialize_physical_parameters(d, T_cold, T_hot)

        # assert
        dx2, dy2 = 1.0, 4.0
        expected_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))

        self.assertEqual(expected_dt, solver.dt)

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # arrange
        solver = self.solver
        w = 1.0
        h = 2.0
        dx = 1.0
        dy = 2.0

        # act
        solver.initialize_domain(w, h, dx, dy)

        # assert
        self.assertEqual(solver.nx, 1)
        self.assertEqual(solver.ny, 1)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Arrange
        solver = self.solver
        solver.T_cold = 100
        solver.T_hot = 500
        solver.nx = 1
        solver.ny = 4
        solver.dx = 1.0
        solver.dy = 2.0

        # Act
        actual_result = solver.set_initial_condition()

        # Assert
        # based on my extensive physics knowledge, I have computed that with the given input, the result must be this
        expected_result = [[100.0, 100.0, 100.0, 100.0]]

        # numpy already has a suitable function to compare multi-dimensional arrays
        self.assertTrue(np.array_equal(expected_result, actual_result))
