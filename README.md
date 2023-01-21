# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```console
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/torben/Documents/git/SSE/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 5 items                                                                                                                                                                            

tests/integration/test_diffusion2d.py ..                                                                                                                                               [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                           [100%]

========================================================================================== FAILURES ==========================================================================================
___________________________________________________________________________________ test_initialize_domain ___________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=40., h=30., dx=0.2, dy=0.2)
>       assert solver.nx == 200
E       assert 150 == 200
E        +  where 150 = <diffusion2d.SolveDiffusion2D object at 0x7f5785d34b20>.nx

tests/unit/test_diffusion2d_functions.py:14: AssertionError
____________________________________________________________________________ test_initialize_physical_parameters _____________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 1.
        solver.dy = 1.
        solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=700.)
>       assert solver.dt == 0.25
E       assert 0.125 == 0.25
E        +  where 0.125 = <diffusion2d.SolveDiffusion2D object at 0x7f5785d37ca0>.dt

tests/unit/test_diffusion2d_functions.py:25: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------
dt = 0.125
_________________________________________________________________________________ test_set_initial_condition _________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 2
        solver.ny = 2
        solver.T_hot = 400.
        solver.T_cold = 300.
        solver.dx = 1.
        solver.dy = 1.
        u = solver.set_initial_condition()
>       assert u[0, 0] == 300.
E       assert 1.0 == 300.0

tests/unit/test_diffusion2d_functions.py:42: AssertionError
================================================================================== short test summary info ===================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 150 == 200
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.125 == 0.25
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 1.0 == 300.0
================================================================================ 3 failed, 2 passed in 0.47s =================================================================================

```

### unittest log

```console
Fdt = 0.125
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestOperations)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/torben/Documents/git/SSE/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 21, in test_initialize_domain
    self.assertEqual(self.solver.nx, 200)
AssertionError: 150 != 200

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestOperations)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/torben/Documents/git/SSE/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 31, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, 0.25)
AssertionError: 0.125 != 0.25

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestOperations)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/torben/Documents/git/SSE/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 44, in test_set_initial_condition
    self.assertEqual(u[0, 0], 300.)
AssertionError: 1.0 != 300.0

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)

```

### integration log

```console
==================================================================================================================================== test session starts ====================================================================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/torben/Documents/git/SSE/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 5 items                                                                                                                                                                                                                                                                           

tests/integration/test_diffusion2d.py FF                                                                                                                                                                                                                                              [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                                                                                                                          [100%]

========================================================================================================================================= FAILURES ==========================================================================================================================================
____________________________________________________________________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=40., h=30., dx=1., dy=1.)
        solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=700.)
>       assert solver.dt == 0.25
E       assert 0.125 == 0.25
E        +  where 0.125 = <diffusion2d.SolveDiffusion2D object at 0x7f26eaa1d060>.dt

tests/integration/test_diffusion2d.py:15: AssertionError
----------------------------------------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------------------------------------
dt = 0.125
________________________________________________________________________________________________________________________________ test_set_initial_condition _________________________________________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=2., h=2., dx=1., dy=1.)
        solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=400.)
        u = solver.set_initial_condition()
>       assert u[0,0] == 300.
E       assert 1.0 == 300.0

tests/integration/test_diffusion2d.py:26: AssertionError
----------------------------------------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------------------------------------
dt = 0.125
___________________________________________________________________________________________________________________________ TestOperations.test_initialize_domain ___________________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=40., h=30., dx=0.2, dy=0.2)
>       self.assertEqual(self.solver.nx, 200)
E       AssertionError: 150 != 200

tests/unit/test_diffusion2d_functions.py:21: AssertionError
____________________________________________________________________________________________________________________ TestOperations.test_initialize_physical_parameters _____________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 1.
        self.solver.dy = 1.
        self.solver.initialize_physical_parameters(d=1., T_cold=300., T_hot=700.)
>       self.assertEqual(self.solver.dt, 0.25)
E       AssertionError: 0.125 != 0.25

tests/unit/test_diffusion2d_functions.py:31: AssertionError
----------------------------------------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------------------------------------
dt = 0.125
_________________________________________________________________________________________________________________________ TestOperations.test_set_initial_condition _________________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx = 2
        self.solver.ny = 2
        self.solver.T_hot = 400.
        self.solver.T_cold = 300.
        self.solver.dx = 1.
        self.solver.dy = 1.
        u = self.solver.set_initial_condition()
>       self.assertEqual(u[0, 0], 300.)
E       AssertionError: 1.0 != 300.0

tests/unit/test_diffusion2d_functions.py:44: AssertionError
================================================================================================================================== short test summary info ==================================================================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.125 == 0.25
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert 1.0 == 300.0
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_domain - AssertionError: 150 != 200
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters - AssertionError: 0.125 != 0.25
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_set_initial_condition - AssertionError: 1.0 != 300.0
===================================================================================================================================== 5 failed in 0.47s =====================================================================================================================================

```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).