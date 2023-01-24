# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
======================================================================== FAILURES =========================================================================
_________________________________________________________________ test_initialize_domain __________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=20., dx=0.5, dy=0.5)

        expected_nx = 10
        expected_ny = 40

        actual_nx = solver.nx
        actual_ny = solver.ny

>       assert (actual_nx == expected_nx)
E       assert 40 == 10

tests/unit/test_diffusion2d_functions.py:21: AssertionError

___________________________________________________________ test_initialize_physical_parameters ___________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.5
        solver.dy = 0.5

        solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

        actual_dt = solver.dt
        expected_dt = 0.03125

>       assert (actual_dt == expected_dt)
E       assert 0.375 == 0.03125

tests/unit/test_diffusion2d_functions.py:38: AssertionError

_______________________________________________________________ test_set_initial_condition ________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 200.
        solver.T_hot = 500.
        solver.nx = 10
        solver.ny = 10
        solver.dx = 0.5
        solver.dy = 0.5

        actual_u = solver.set_initial_condition()
        expected_u = 200 * np.ones((10, 10))

>       assert (actual_u.all() == expected_u.all())
E       assert False == True
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f849da767f0>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f849da767f0> = array([[  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],\n       [  0.,   0.,   0.,   0.,   0.,   0.,   0.,...   0.,   0.,   0.,   0.,   0., 500., 500., 500.],\n       [  0.,   0.,   0.,   0.,   0.,   0.,   0., 500., 500., 500.]]).all
E        +  and   True = <built-in method all of numpy.ndarray object at 0x7f849da76610>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f849da76610> = array([[200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200., 200., 200.,... 200., 200., 200., 200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.]]).all

tests/unit/test_diffusion2d_functions.py:55: AssertionError
================================================================= short test summary info =================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40 == 10
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.375 == 0.03125
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False == True
=============================================================== 3 failed, 2 passed in 0.28s ===============================================================
```

### unittest log
```
============================= test session starts ==============================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/bluzuk/kekw/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                             [100%]

=================================== FAILURES ===================================
____________________ TestDiffusion2D.test_initialize_domain ____________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=self.w, h=self.h, dx=self.dx, dy=self.dy)
    
        expected_nx = 10
        expected_ny = 40
        actual_nx = solver.nx
        actual_ny = solver.ny
    
>       self.assertEqual(actual_nx, expected_nx)
E       AssertionError: 40 != 10

tests/unit/test_diffusion2d_functions.py:42: AssertionError
_____________ TestDiffusion2D.test_initialize_physical_parameters ______________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = self.dx
        solver.dy = self.dy
    
        solver.initialize_physical_parameters(d=self.d, T_cold=self.T_cold, T_hot=self.T_hot)
    
        actual_dt = solver.dt
        expected_dt = 0.03125
    
>       self.assertEqual(actual_dt, expected_dt)
E       AssertionError: 0.375 != 0.03125

tests/unit/test_diffusion2d_functions.py:58: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.375
__________________ TestDiffusion2D.test_set_initial_condition __________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = self.T_cold
        solver.T_hot = self.T_hot
        solver.nx = self.nx
        solver.ny = self.ny
        solver.dx = self.dx
        solver.dy = self.dy
    
        actual_u = solver.set_initial_condition()
        expected_u = self.T_cold * np.ones((self.nx, self.ny))
    
>       self.assertEqual(actual_u.all(), expected_u.all())
E       AssertionError: False != True

tests/unit/test_diffusion2d_functions.py:75: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition
========================= 3 failed, 2 passed in 0.25s ==========================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
