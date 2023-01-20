"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase
#import pytest
import numpy as np

class TestDiffusion2d(TestCase):
   
    def setUp(self):
        
        self.solver = SolveDiffusion2D()
    
    
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 200
        expected_ny = 100
        self.solver.initialize_domain(w=20.,h=10.,dx=0.1,dy=0.1)
        
        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)
        

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
    
        self.solver.dx=0.2
        self.solver.dy=0.1
        #expected_dt = pytest.approx(0.0008, abs=0.0001)
        self.solver.initialize_physical_parameters(d=5., T_cold=400., T_hot=800.)
        self.assertAlmostEqual(self.solver.dt, 0.0008)
    

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx = 10
        self.solver.ny = 10
        self.solver.d = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
        self.solver.dx=0.1
        self.solver.dy=0.1
        u = self.solver.set_initial_condition()
        expected_u = self.solver.T_cold * np.ones((self.solver.nx, self.solver.ny))
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 4, 10, 10
        r2 = r ** 2
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = self.solver.T_hot
                    
        self.assertTrue((u == expected_u).all())
        
