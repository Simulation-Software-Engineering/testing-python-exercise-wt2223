# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
tests/unit/test_diffusion2d_functions.py F                                [100%]

=================================== FAILURES ====================================
____________________________ test_initialize_domain _____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=50., h=1000., dx=0.2, dy=10.)
    
>       assert solver.nx == 250
E       assert 5000 == 250
E        +  where 5000 = <diffusion2d.SolveDiffusion2D object at 0x7fb4bc627fd0>.nx

tests/unit/test_diffusion2d_functions.py:15: AssertionError
============================ short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 5000 == 250
=============================== 1 failed in 0.84s ===============================
```
```
tests/unit/test_diffusion2d_functions.py F                                                         [100%]

================================================ FAILURES ================================================
__________________________________ test_initialize_physical_parameters ___________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 0.1
        solver.dy = 1
    
        solver.initialize_physical_parameters(d=2., T_cold=400., T_hot=600.)
    
>       assert solver.dt == 0.0024752475247524757
E       assert 0.002487562189054727 == 0.0024752475247524757
E        +  where 0.002487562189054727 = <diffusion2d.SolveDiffusion2D object at 0x7fe086cf8ac0>.dt

tests/unit/test_diffusion2d_functions.py:30: AssertionError
------------------------------------------ Captured stdout call ------------------------------------------
dt = 0.002487562189054727
======================================== short test summary info =========================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.002487562189054727 == 0.0024752475247524757
```
```
tests/unit/test_diffusion2d_functions.py F                                                                          [100%]

======================================================== FAILURES =========================================================
_______________________________________________ test_set_initial_condition ________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 1.
        solver.dy = 1.
        solver.nx = 1
        solver.ny = 1
        solver.T_cold = 350.
        solver.T_hot = 700.
    
        solver.set_initial_condition()
    
>       assert solver.set_initial_condition() == [[350.]]
E       assert array([[700.]]) == [[350.0]]
E         Use -v to get more diff

tests/unit/test_diffusion2d_functions.py:47: AssertionError
================================================= short test summary info =================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert array([[700.]]) == [[350.0]]
==================================================== 1 failed in 0.59s ====================================================
```
### unittest log
```
Fdt = 0.002487562189054727
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/SenaTirpan/Desktop/repos/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 25, in test_initialize_domain
    self.assertEqual(self.solver.nx,250)
AssertionError: 5000 != 250

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/SenaTirpan/Desktop/repos/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 39, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt,0.0024752475247524757)
AssertionError: 0.002487562189054727 != 0.0024752475247524757

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/SenaTirpan/Desktop/repos/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 56, in test_set_initial_condition
    self.assertEqual(self.solver.set_initial_condition(),[[350.]])
AssertionError: array([[700.]]) != [[350.0]]

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
```
### Integration test log
```
collected 2 items                                                                                                                               

tests/integration/test_diffusion2d.py FF                                                                                                  [100%]

=================================================================== FAILURES ====================================================================
______________________________________________________ test_initialize_physical_parameters ______________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=50., h=1000., dx=0.1, dy=1.)
        solver.initialize_physical_parameters(d=2., T_cold=400., T_hot=600.)
    
>       assert solver.dt == 0.0024752475247524757
E       assert 0.002487562189054727 == 0.0024752475247524757
E        +  where 0.002487562189054727 = <diffusion2d.SolveDiffusion2D object at 0x7f9b5f44c4f0>.dt

tests/integration/test_diffusion2d.py:16: AssertionError
------------------------------------------------------------- Captured stdout call --------------------------------------------------------------
dt = 0.002487562189054727
__________________________________________________________ test_set_initial_condition ___________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=1., h=1., dx=1., dy=1.)
        solver.initialize_physical_parameters(d=2., T_cold=350., T_hot=700.)
    
>       assert solver.set_initial_condition() == [[350.]]
E       assert array([[700.]]) == [[350.0]]
E         Use -v to get more diff

tests/integration/test_diffusion2d.py:26: AssertionError
------------------------------------------------------------- Captured stdout call --------------------------------------------------------------
dt = 0.16666666666666666
============================================================ short test summary info ============================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.002487562189054727 == 0.0024752475247524757
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert array([[700.]]) == [[350.0]]
=============================================================== 2 failed in 0.82s ===============================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
