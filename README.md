# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
============================================================================================================================= FAILURES ==============================================================================================================================
______________________________________________________________________________________________________________________ test_initialize_domain _______________________________________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=15., h=12., dx=0.2, dy=0.5)
>       assert solver.nx==75
E       assert 60 == 75
E        +  where 60 = <diffusion2d.SolveDiffusion2D object at 0x13c3b63b0>.nx

tests/unit/test_diffusion2d_functions.py:14: AssertionError
________________________________________________________________________________________________________________ test_initialize_physical_parameters ________________________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 2
        solver.dy= 2
        solver.initialize_physical_parameters(d=2., T_cold=100., T_hot=300.)
>       assert solver.dt==0.5
E       assert 1.0 == 0.5
E        +  where 1.0 = <diffusion2d.SolveDiffusion2D object at 0x13c3b7d90>.dt

tests/unit/test_diffusion2d_functions.py:26: AssertionError
----------------------------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------------------------
dt = 1.0
____________________________________________________________________________________________________________________ test_set_initial_condition _____________________________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 1
        solver.ny = 1
        solver.dx = 1
        solver.dy = 1
        solver.T_cold = 100.
        solver.T_hot = 300.
        u = solver.set_initial_condition()
>       assert u[0, 0] == 100.
E       assert 300.0 == 100.0

tests/unit/test_diffusion2d_functions.py:42: AssertionError
====================================================================================================================== short test summary info ======================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 60 == 75
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 1.0 == 0.5
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 300.0 == 100.0
========================================================================================================================= 3 failed in 0.52s =========================================================================================================================
```
### unittest log

```
Fdt = 1.0
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vidushi/development/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 27, in test_initialize_domain
    self.assertEqual(solver.nx,75)
AssertionError: 60 != 75

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vidushi/development/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 39, in test_initialize_physical_parameters
    self.assertEqual(solver.dt,0.5)
AssertionError: 1.0 != 0.5

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vidushi/development/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 55, in test_set_initial_condition
    self.assertEqual(u[0, 0],100.)
AssertionError: 300.0 != 100.0

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
```
## Integration test log

```
====================================================================================================== test session starts ======================================================================================================
platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/vidushi/development/testing-python-exercise-wt2223
collected 2 items

tests/integration/test_diffusion2d.py FF                                                                                                                                                                                  [100%]

=========================================================================================================== FAILURES ============================================================================================================
______________________________________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        solver = SolveDiffusion2D()
        solver.initialize_domain(w=11.,h=12.,dx=2., dy=2.)
        solver.initialize_physical_parameters(d=2.,T_cold=100.,T_hot=300.)
>       assert solver.dt== 0.5
E       assert 1.0 == 0.5
E        +  where 1.0 = <diffusion2d.SolveDiffusion2D object at 0x11afb1f90>.dt

tests/integration/test_diffusion2d.py:16: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------
dt = 1.0
__________________________________________________________________________________________________ test_set_initial_condition ___________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=15.,h=13.,dx=1., dy=1.)
        solver.initialize_physical_parameters(d=3.,T_cold=300.,T_hot=200.)
        u= solver.set_initial_condition()
>       assert u[0][0]==300.
E       assert 200.0 == 300.0

tests/integration/test_diffusion2d.py:27: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------------------------------
dt = 0.16666666666666666
==================================================================================================== short test summary info ====================================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 1.0 == 0.5
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert 200.0 == 300.0
======================================================================================================= 2 failed in 0.33s =======================================================================================================
```
## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
