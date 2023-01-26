# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
tests/unit/test_diffusion2d_functions.py F                                                                                                                           [100%]

================================================================================= FAILURES =================================================================================
__________________________________________________________________________ test_initialize_domain __________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.initialize_domain(w=12., h=15., dx=0.2, dy=0.3)
>       assert solver.nx == 60
E       assert 75 == 60
E        +  where 75 = <diffusion2d.SolveDiffusion2D object at 0x7fadd98ef070>.nx

tests/unit/test_diffusion2d_functions.py:15: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 75 == 60
============================================================================ 1 failed in 0.46s =============================================================================
```

```
tests/unit/test_diffusion2d_functions.py F                                                                                                                           [100%]

================================================================================= FAILURES =================================================================================
___________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 0.2
        solver.dy = 0.5
        solver.initialize_physical_parameters(d=6., T_cold=100., T_hot=700.)
    
>       assert solver.dt == 0.002873563218390805
E       assert 0.00574712643678161 == 0.002873563218390805
E        +  where 0.00574712643678161 = <diffusion2d.SolveDiffusion2D object at 0x7fc5408180d0>.dt

tests/unit/test_diffusion2d_functions.py:29: AssertionError
--------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
dt = 0.00574712643678161
========================================================================= short test summary info ==========================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.00574712643678161 == 0.002873563218390805
============================================================================ 1 failed in 0.43s =============================================================================
```

```
tests/unit/test_diffusion2d_functions.py F                                                                                                                           [100%]

================================================================================= FAILURES =================================================================================
________________________________________________________________________ test_set_initial_condition ________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 0.2
        solver.dy = 0.5
        solver.nx = 1
        solver.ny = 1
        solver.T_cold = 440.
        solver.T_hot = 840.
    
        solver.set_initial_condition()
    
>       assert solver.set_initial_condition() == [[440.]]
E       assert array([[840.]]) == [[440.0]]
E         Use -v to get more diff

tests/unit/test_diffusion2d_functions.py:47: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert array([[840.]]) == [[440.0]]
============================================================================ 1 failed in 0.43s =============================================================================
```

### unittest log

```
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mustafacevik/PycharmProjects/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 20, in test_initialize_domain
    self.assertEqual(self.solver.nx, 60)
AssertionError: 75 != 60
```

```
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mustafacevik/PycharmProjects/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 32, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, 0.002873563218390805)
AssertionError: 0.00574712643678161 != 0.002873563218390805
```

```
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mustafacevik/PycharmProjects/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 48, in test_set_initial_condition
    self.assertEqual(self.solver.set_initial_condition(), [[440.]])
AssertionError: array([[840.]]) != [[440.0]]

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
```

### integration test log

```
tests/integration/test_diffusion2d.py FF                                                                                                                             [100%]

================================================================================= FAILURES =================================================================================
___________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=12., dx=0.1, dy=0.2)
        solver.initialize_physical_parameters(d=6., T_cold=200., T_hot=600.)
    
>       assert solver.dt == 0.0006666666666666669
E       assert 0.0013333333333333337 == 0.0006666666666666669
E        +  where 0.0013333333333333337 = <diffusion2d.SolveDiffusion2D object at 0x7f8eb8febee0>.dt

tests/integration/test_diffusion2d.py:16: AssertionError
--------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
dt = 0.0013333333333333337

```

```
________________________________________________________________________ test_set_initial_condition ________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=0.2, h=0.5, dx=0.2, dy=0.5)
        solver.initialize_physical_parameters(d=6., T_cold=440., T_hot=840.)
    
>       assert solver.set_initial_condition() == [[440.]]
E       ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

tests/integration/test_diffusion2d.py:27: ValueError
--------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
dt = 0.00574712643678161
========================================================================= short test summary info ==========================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0013333333333333337 == 0.0006666666666666669
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
============================================================================ 2 failed in 0.34s =============================================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
