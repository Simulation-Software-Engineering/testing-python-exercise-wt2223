"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
from unittest import TestCase

class TestDiffusion2D(TestCase):
    
    def setUp(self):
        self.solver = SolveDiffusion2D()
  
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=50., h=50., dx=0.05, dy=0.05)
        self.assertEqual(self.solver.nx, 1000 )
        self.assertEqual(self.solver.ny, 1000 )

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters(d=8., T_cold=200., T_hot=400.)
        
        self.assertAlmostEqual(self.solver.dt, 0.0003125)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 300
        self.solver.T_hot = 700
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100
        u = self.solver.set_initial_condition()
        self.assertEqual(u.shape, (self.solver.nx, self.solver.ny))
        
        
