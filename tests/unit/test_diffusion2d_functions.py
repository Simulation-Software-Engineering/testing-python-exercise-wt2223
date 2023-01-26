"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase
import numpy as np

class TestDiffusion2D(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()


    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(2.,20.,0.1,0.1)
        self.assertEqual(self.solver.nx, 20)
        self.assertEqual(self.solver.ny, 200)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        expected_value = 0.0008000000000000001

        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(5.,400.,800.)
        self.assertEqual(self.solver.D, 5.)
        self.assertEqual(self.solver.T_cold, 400.)
        self.assertEqual(self.solver.T_hot, 800.)
        self.assertEqual(self.solver.dt, expected_value)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_value = np.array([[300., 300., 300.],[300., 300., 700.]])

        self.solver.dx = 5
        self.solver.dy = 3
        self.solver.nx = 2
        self.solver.ny = 3
        self.solver.T_cold = 300
        self.solver.T_hot = 700

        self.assertTrue((self.solver.set_initial_condition() == expected_value).all())


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(2.,20.,0.1,0.1)
    assert solver.nx == 20.
    assert solver.ny == 200.


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    expected_value = 0.0005000000000000001

    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.1
    solver.initialize_physical_parameters(5.,400.,800.)
    assert solver.D == 5.
    assert solver.T_cold == 400.
    assert solver.T_hot == 800.
    assert solver.dt == expected_value


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    expected_value = np.array([[300., 300., 300.],[300., 300., 700.]])

    solver = SolveDiffusion2D()
    solver.dx = 5
    solver.dy = 3
    solver.nx = 2
    solver.ny = 3
    solver.T_cold = 300
    solver.T_hot = 700

    assert (solver.set_initial_condition() == expected_value).all()
