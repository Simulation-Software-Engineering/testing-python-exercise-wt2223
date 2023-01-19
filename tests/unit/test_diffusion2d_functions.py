"""
Tests for functions in class SolveDiffusion2D
"""
import numpy as np
from diffusion2d import SolveDiffusion2D
import unittest

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()
        self.solver.dx = 0.5
        self.solver.dy = 0.2
    
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=20., h=12., dx=0.5, dy=0.2)
        excepted_nx, excepted_ny = 40, 60
        # assert self.solver.nx == excepted_nx, f'nx value should be {excepted_nx} but got {self.solver.nx}'
        # assert self.solver.ny == excepted_ny, f'nx value should be {excepted_ny} but got {self.solver.ny}'
        self.assertEqual(self.solver.nx, excepted_nx)
        self.assertEqual(self.solver.ny, excepted_ny)
        
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
        calculated_dt = 0.00574
        # expected_dt = pytest.approx(calculated_dt, abs=0.01)
        # assert expected_dt == self.solver.dt , 'Assertion error'
        self.assertAlmostEqual(self.solver.dt, calculated_dt, 4)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver = SolveDiffusion2D()
        self.solver.nx = 5
        self.solver.ny = 5
        self.solver.D = 3.0
        self.solver.dx = 0.25
        self.solver.dy = 0.1
        self.solver.T_cold = 200.0
        self.solver.T_hot = 500.0
        #  According to the algorithm if I pass these values to the function it should give me numpy array with all the values equal to 200
        excepted_u = np.ones((5, 5)) * 200.0
        calculated_u = self.solver.set_initial_condition()
        self.assertEqual(calculated_u.shape,excepted_u.shape)
        assert np.array_equal(excepted_u,calculated_u), f'calculated u/initial condition should fe {excepted_u} but the function returned {calculated_u}'