"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D
import unittest


class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()
        self.solver.dx = .1
        self.solver.dy = .1

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w, h, dx, dy = 1.0, 2.0, .1, .1
        self.solver.initialize_domain(
            w=w, h=h, dx=dx, dy=dy
        )

        assert self.solver.w == w
        assert self.solver.h == h
        assert self.solver.dx == dx
        assert self.solver.dy == dy

        assert self.solver.nx == int(w / dx)
        assert self.solver.ny == int(h / dy)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        d, T_cold, T_hot = 4., 300., 700.
        self.solver.initialize_physical_parameters(
            d=d, T_cold=T_cold, T_hot=T_hot
        )

        assert self.solver.D == d
        assert self.solver.T_cold == T_cold
        assert self.solver.T_hot == T_hot

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # could move all this to the setUp, true...
        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 10.
        self.solver.dy = 10.
        self.solver.nx = int(self.solver.w / self.solver.dx)
        self.solver.ny = int(self.solver.h / self.solver.dy)

        self.solver.d = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.

        res = self.solver.set_initial_condition()
        _res = np.full((1, 1), 299.)
        assert (res == _res).all()
