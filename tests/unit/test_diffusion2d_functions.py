"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np
from unittest import TestCase

class TestDiffusion2D(TestCase):
    
    def setUp(self):
        self.w=40.
        self.h=20.
        self.dx=0.1
        self.dy=0.2
        self.D = 3.
        self.T_cold = 200.
        self.T_hot = 600.
        self.nx = 400
        self.ny = 100

        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = self.nx
        expected_ny = self.ny

        self.solver.initialize_domain(self.w,self.h,self.dx,self.dy)

        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        expected_dt = 1/750
        self.solver.dx = self.dx
        self.solver.dy = self.dy
        
        self.solver.initialize_physical_parameters(self.D, self.T_cold, self.T_hot)

        self.assertAlmostEqual(expected_dt, self.solver.dt,  2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.dx=10.
        self.dy=10.
        self.solver.dx = self.dx
        self.solver.dy = self.dy
        self.solver.nx = self.nx
        self.solver.ny = self.ny
        self.solver.T_cold = self.T_cold
        
        expected_u = self.T_cold * np.ones((self.solver.nx, self.solver.ny))
    
        solver_u = self.solver.set_initial_condition()
      
        self.assertTrue((expected_u==solver_u).all())