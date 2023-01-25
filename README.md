# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
=========================================================================== test session starts ============================================================================
platform linux -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /media/yasser/D24622B1462295EF/CS/Stuttgart/Simulation Software Engineering/exercise week9/testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 5 items                                                                                                                                                          

tests/integration/test_diffusion2d.py ..                                                                                                                             [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                         [100%]

================================================================================= FAILURES =================================================================================
__________________________________________________________________________ test_initialize_domain __________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=50., h=50., dx=0.05, dy=0.05)
>       assert solver.nx == 10000 , "Wrong value for nx"
E       AssertionError: Wrong value for nx
E       assert 1000 == 10000
E        +  where 1000 = <diffusion2d.SolveDiffusion2D object at 0x7f39137cbfd0>.nx

tests/unit/test_diffusion2d_functions.py:14: AssertionError
___________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.1
        solver.dy = 0.1
        solver.initialize_physical_parameters(d=8., T_cold=200., T_hot=400.)
    
>       assert solver.dt == pytest.approx(0.00003125, abs = 0.000001), "The value of dt is wrong"
E       AssertionError: The value of dt is wrong
E       assert 0.00031250000000000006 == 3.125e-05 ± 1.0e-06
E         comparison failed
E         Obtained: 0.00031250000000000006
E         Expected: 3.125e-05 ± 1.0e-06

tests/unit/test_diffusion2d_functions.py:27: AssertionError
--------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
dt = 0.00031250000000000006
________________________________________________________________________ test_set_initial_condition ________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 300
        solver.T_hot = 700
        solver.dx = 0.1
        solver.dy = 0.1
        solver.nx = 100
        solver.ny = 100
        u = solver.set_initial_condition()
>       assert u.shape == (solver.T_cold, solver.ny), "The shape of the output is not correct"
E       AssertionError: The shape of the output is not correct
E       assert (100, 100) == (300, 100)
E         At index 0 diff: 100 != 300
E         Use -v to get more diff

tests/unit/test_diffusion2d_functions.py:42: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: Wrong value for nx
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - AssertionError: The value of dt is wrong
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError: The shape of the output is not correct
======================================================================= 3 failed, 2 passed in 0.80s ========================================================================
```

### unittest log

```
Fdt = 0.00031250000000000006
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/media/yasser/D24622B1462295EF/CS/Stuttgart/Simulation Software Engineering/exercise week9/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 19, in test_initialize_domain
    self.assertEqual(self.solver.nx, 10000 )
AssertionError: 1000 != 10000

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/media/yasser/D24622B1462295EF/CS/Stuttgart/Simulation Software Engineering/exercise week9/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 30, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.003125)
AssertionError: 0.00031250000000000006 != 0.003125 within 7 places (0.0028125 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/media/yasser/D24622B1462295EF/CS/Stuttgart/Simulation Software Engineering/exercise week9/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 44, in test_set_initial_condition
    self.assertEqual(u.shape, (self.solver.T_cold, self.solver.ny))
AssertionError: Tuples differ: (100, 100) != (300, 100)

First differing element 0:
100
300

- (100, 100)
?  ^

+ (300, 100)
?  ^


----------------------------------------------------------------------
Ran 3 tests in 0.005s

FAILED (failures=3)
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
