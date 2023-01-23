"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
from unittest import TestCase

class TestDiffusion2D(TestCase):

    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()
        #self.w = 10.5
        #self.h = 7.3
        #self.dx = 0.2
        #self.dy = 0.2
        #self.d = 3
        #self.T_cold = 400
        #self.T_hot = 800
        #self.nx = 52
        #self.ny = 36

    #Unit test
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        # Fixture
        w =  10.5
        h = 7.3
        dx = 0.2
        dy = 0.2

        # Expected Results
        expected_nx = 52
        expected_ny = 36

        # Actual Results
        self.solver.initialize_domain(w,h,dx,dy)
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        # Tests
        self.assertEqual(expected_nx, actual_nx)
        self.assertEqual(expected_ny, actual_ny)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """


        #Fixture
        d = 3.
        self.solver.dx = 0.2
        self.solver.dy = 0.2


        #Expected Result
        dx2, dy2 = self.solver.dx * self.solver.dx, self.solver.dy * self.solver.dy
        expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

        #Actual Result
        self.solver.initialize_physical_parameters(d)
        actual_dt = self.solver.dt

        #Test
        self.assertEqual(expected_dt, actual_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        #Fixture
        self.solver.T_cold = 400.
        self.solver.T_hot = 800.
        self.solver.nx = 2
        self.solver.ny = 2
        self.solver.dx = 0.2
        self.solver.dy = 0.2

        #Expected Result
        expected_u = self.solver.T_cold * np.ones((self.solver.nx, self.solver.ny))

        #Actual Result
        actual_u = self.solver.set_initial_condition()

        #Test
        self.assertTrue((expected_u==actual_u).all())
