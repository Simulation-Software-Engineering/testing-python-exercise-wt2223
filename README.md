# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
================================================================================================================================= test session starts ==================================================================================================================================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/julius/Documents/SSE/tests/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 5 items                                                                                                                                                                                                                                                                      

tests/integration/test_diffusion2d.py ..                                                                                                                                                                                                                                         [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                                                                                                                     [100%]

======================================================================================================================================= FAILURES =======================================================================================================================================
________________________________________________________________________________________________________________________________ test_initialize_domain ________________________________________________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 20.
        h = 30.
        dx = 0.6
        dy = 0.7
    
        # Expected results
        nx_correct = 33
        ny_correct = 42
    
        # Actual result
        solver.initialize_domain(w, h, dx, dy)
    
        # Tests
        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy
>       assert solver.nx == nx_correct
E       assert 50 == 33
E        +  where 50 = <diffusion2d.SolveDiffusion2D object at 0x7f9a9141b7f0>.nx

tests/unit/test_diffusion2d_functions.py:33: AssertionError
_________________________________________________________________________________________________________________________ test_initialize_physical_parameters __________________________________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        d = 5.
        T_cold = 400.0
        T_hot = 600.0
        solver.dx = 0.6
        solver.dy = 0.7
    
        # Expected result
        dt_correct = 0.02075294117647059
    
        # Actual result
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        # Test
>       assert solver.dt == pytest.approx(dt_correct, 1e-8)
E       assert 0.3748499999999999 == 0.02075294117647059 ± 2.1e-10
E         comparison failed
E         Obtained: 0.3748499999999999
E         Expected: 0.02075294117647059 ± 2.1e-10

tests/unit/test_diffusion2d_functions.py:55: AssertionError
--------------------------------------------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------------------------------------------
dt = 0.3748499999999999
______________________________________________________________________________________________________________________________ test_set_initial_condition ______________________________________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 2
        solver.ny = 3
        solver.dx = 0.6
        solver.dy = 0.7
        solver.T_cold = 400.0
        u = solver.set_initial_condition()
    
        # Test
        assert isinstance(u, np.ndarray)
        assert u.ndim == 2
        assert u.shape[0] == 2
>       assert u.shape[1] == 3
E       assert 2 == 3

tests/unit/test_diffusion2d_functions.py:74: AssertionError
=============================================================================================================================== short test summary info ================================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 50 == 33
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.3748499999999999 == 0.02075294117647059 ± 2.1e-10
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 2 == 3
============================================================================================================================= 3 failed, 2 passed in 0.29s ==============================================================================================================================
```

### unittest log

```
Fdt = 0.3748499999999999
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julius/Documents/SSE/tests/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 41, in test_initialize_domain
    self.assertEqual(self.solver.nx, nx_correct)
AssertionError: 50 != 33

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julius/Documents/SSE/tests/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 62, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, dt_correct)
AssertionError: 0.3748499999999999 != 0.02075294117647059 within 7 places (0.3540970588235293 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julius/Documents/SSE/tests/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 80, in test_set_initial_condition
    self.assertEqual(u.shape[1], 3)
AssertionError: 2 != 3

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
```

## integration test log

```
================================================================================================== test session starts ==================================================================================================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/julius/Documents/SSE/tests/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 2 items                                                                                                                                                                                                       

tests/integration/test_diffusion2d.py FF                                                                                                                                                                          [100%]

======================================================================================================= FAILURES ========================================================================================================
__________________________________________________________________________________________ test_initialize_physical_parameters __________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        solver = SolveDiffusion2D()
        d = 5.
        T_cold = 400.0
        T_hot = 600.0
        w = 20.
        h = 30.
        dx = 0.6
        dy = 0.7
    
        # Expected result
        dt_correct = 0.02075294117647059
    
        # Actual result
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        # Test
>       assert solver.dt == pytest.approx(dt_correct, 1e-8)
E       assert 0.3748499999999999 == 0.02075294117647059 ± 2.1e-10
E         comparison failed
E         Obtained: 0.3748499999999999
E         Expected: 0.02075294117647059 ± 2.1e-10

tests/integration/test_diffusion2d.py:32: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------
dt = 0.3748499999999999
______________________________________________________________________________________________ test_set_initial_condition _______________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Fixture
        solver = SolveDiffusion2D()
        d = 5.
        T_cold = 400.0
        T_hot = 600.0
        w = 1.2
        h = 2.1
        dx = 0.6
        dy = 0.7
    
        # Actual result
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        u = solver.set_initial_condition()
    
        # Test
        assert isinstance(u, np.ndarray)
        assert u.ndim == 2
>       assert u.shape[0] == 2
E       assert 3 == 2

tests/integration/test_diffusion2d.py:57: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------
dt = 0.3748499999999999
================================================================================================ short test summary info ================================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.3748499999999999 == 0.02075294117647059 ± 2.1e-10
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert 3 == 2
=================================================================================================== 2 failed in 0.27s ===================================================================================================
```


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
