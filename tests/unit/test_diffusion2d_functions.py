"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
from unittest import TestCase
import numpy as np


class TestDiffusion2D(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

    # Unit test
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        w = 20.
        h = 30.
        dx = 0.6
        dy = 0.7

        # Expected results
        nx_correct = 33
        ny_correct = 42

        # Actual result
        self.solver.initialize_domain(w, h, dx, dy)

        # Tests
        self.assertEqual(self.solver.w, w)
        self.assertEqual(self.solver.h, h)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)
        self.assertEqual(self.solver.nx, nx_correct)
        self.assertEqual(self.solver.ny, ny_correct)

    # Unit test
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        d = 5.
        T_cold = 400.0
        T_hot = 600.0
        self.solver.dx = 0.6
        self.solver.dy = 0.7

        # Expected result
        dt_correct = 0.02075294117647059

        # Actual result
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # Test
        self.assertAlmostEqual(self.solver.dt, dt_correct)

    # Unit test
    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Fixture
        self.solver.nx = 2
        self.solver.ny = 3
        self.solver.dx = 0.6
        self.solver.dy = 0.7
        self.solver.T_cold = 400.0
        u = self.solver.set_initial_condition()

        # Test
        self.assertIsInstance(u, np.ndarray)
        self.assertEqual(u.ndim, 2)
        self.assertEqual(u.shape[0], 2)
        self.assertEqual(u.shape[1], 3)
        for i in range(2):
            for j in range(3):
                self.assertEqual(u[i, j], 400.0)


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    # Fixture
    solver = SolveDiffusion2D()
    w = 20.
    h = 30.
    dx = 0.6
    dy = 0.7

    # Expected results
    nx_correct = 33
    ny_correct = 42

    # Actual result
    solver.initialize_domain(w, h, dx, dy)

    # Tests
    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy
    assert solver.nx == nx_correct
    assert solver.ny == ny_correct


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # Fixture
    solver = SolveDiffusion2D()
    d = 5.
    T_cold = 400.0
    T_hot = 600.0
    solver.dx = 0.6
    solver.dy = 0.7

    # Expected result
    dt_correct = 0.02075294117647059

    # Actual result
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    # Test
    assert solver.dt == pytest.approx(dt_correct, 1e-8)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # Fixture
    solver = SolveDiffusion2D()
    solver.nx = 2
    solver.ny = 3
    solver.dx = 0.6
    solver.dy = 0.7
    solver.T_cold = 400.0
    u = solver.set_initial_condition()

    # Test
    assert isinstance(u, np.ndarray)
    assert u.ndim == 2
    assert u.shape[0] == 2
    assert u.shape[1] == 3
    for i in range(2):
        for j in range(3):
            assert u[i, j] == 400.0
