"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

import numpy as np


class TestDiffusion2D(TestCase):
    """
    Test suite for mathematical operations functions.
    """

    def setUp(self):
        # Fixture
        self.w = 5.
        self.h = 20.

        self.dx = 0.5
        self.dy = 0.5

        self.nx = 10
        self.ny = 40

        self.d = 2.
        self.T_cold = 200.
        self.T_hot = 500.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=self.w, h=self.h, dx=self.dx, dy=self.dy)

        expected_nx = 10
        expected_ny = 40
        actual_nx = solver.nx
        actual_ny = solver.ny

        self.assertEqual(actual_nx, expected_nx)
        self.assertEqual(actual_ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = self.dx
        solver.dy = self.dy

        solver.initialize_physical_parameters(d=self.d,
                                              T_cold=self.T_cold,
                                              T_hot=self.T_hot)

        expected_dt = 0.03125
        actual_dt = solver.dt

        self.assertEqual(actual_dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = self.T_cold
        solver.T_hot = self.T_hot
        solver.nx = self.nx
        solver.ny = self.ny
        solver.dx = self.dx
        solver.dy = self.dy

        expected_u = self.T_cold * np.ones((self.nx, self.ny))
        actual_u = solver.set_initial_condition()

        self.assertEqual(actual_u.all(), expected_u.all())
