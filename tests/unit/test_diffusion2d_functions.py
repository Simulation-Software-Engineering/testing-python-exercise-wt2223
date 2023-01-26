"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest


class TestDiffusion2D(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        self.solver.initialize_domain(w=12., h=15., dx=0.2, dy=0.3)

        self.assertEqual(self.solver.nx, 60)
        self.assertEqual(self.solver.ny, 50)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        self.solver.dx = 0.2
        self.solver.dy = 0.5
        self.solver.initialize_physical_parameters(d=6., T_cold=100., T_hot=700.)

        self.assertEqual(self.solver.dt, 0.002873563218390805)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.dx = 0.2
        self.solver.dy = 0.5
        self.solver.nx = 1
        self.solver.ny = 1
        self.solver.T_cold = 440.
        self.solver.T_hot = 840.

        self.solver.set_initial_condition()

        self.assertEqual(self.solver.set_initial_condition(), [[440.]])
