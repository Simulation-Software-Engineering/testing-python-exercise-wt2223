"""
Tests for functions in class SolveDiffusion2D
"""
from diffusion2d import SolveDiffusion2D
import unittest 


# creating a class TestDiffusion2D which is derived from the class unittest.TestCase
# Note that the parameter self needs to be used in the input parameters of all member functions and also while defining and using member variables.

class TestDiffusion2D(unittest.TestCase):
    """
    Tests for functions in class SolveDiffusion2D
    """
    def setUp(self) -> None:
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # solver = SolveDiffusion2D()
        self.solver.initialize_domain(w=50., h=1000., dx=0.2, dy=10.)

        self.assertEqual(self.solver.nx,250) 
        self.assertEqual(self.solver.ny,100) 
        
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # solver = SolveDiffusion2D()

        self.solver.dx = 0.1
        self.solver.dy = 1

        self.solver.initialize_physical_parameters(d=2., T_cold=400., T_hot=600.)

        self.assertEqual(self.solver.dt,0.0024752475247524757)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # solver = SolveDiffusion2D()
        
        self.solver.dx = 1.
        self.solver.dy = 1.
        self.solver.nx = 1
        self.solver.ny = 1
        self.solver.T_cold = 350.
        self.solver.T_hot = 700.
        
        self.solver.set_initial_condition()

        self.assertEqual(self.solver.set_initial_condition(),[[350.]])
        
# def test_initialize_domain():
#     """
#     Check function SolveDiffusion2D.initialize_domain
#     """
#     solver = SolveDiffusion2D()
#     solver.initialize_domain(w=50., h=1000., dx=0.2, dy=10.)

#     assert solver.nx == 250
#     assert solver.ny == 100


# def test_initialize_physical_parameters():
#     """
#     Checks function SolveDiffusion2D.initialize_domain
#     """
#     solver = SolveDiffusion2D()

#     solver.dx = 0.1
#     solver.dy = 1

#     solver.initialize_physical_parameters(d=2., T_cold=400., T_hot=600.)

#     assert solver.dt == 0.0024752475247524757

# def test_set_initial_condition():
#     """
#     Checks function SolveDiffusion2D.get_initial_function
#     """
#     solver = SolveDiffusion2D()
    
#     solver.dx = 1.
#     solver.dy = 1.
#     solver.nx = 1
#     solver.ny = 1
#     solver.T_cold = 350.
#     solver.T_hot = 700.
    
#     solver.set_initial_condition()

#     assert solver.set_initial_condition() == [[350.]]


