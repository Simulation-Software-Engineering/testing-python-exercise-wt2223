# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
Initialize domain
```
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py ..F                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
___________________________________________________________________ test_set_initial_condition ____________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 3
        solver.ny = 2
        solver.dx = 0.3
        solver.dy = 0.4
        solver.T_cold = 200.
        solver.T_hot = 700.
        actual_u = solver.set_initial_condition()
        expected_u = pytest.approx(500.0, 0.001)
>       assert expected_u == actual_u
E       assert 500.0 ± 5.0e-01 == array([[200.,...[200., 200.]])
E         comparison failed
E         Obtained: [[200. 200.]\n [200. 200.]\n [200. 200.]]
E         Expected: 500.0 ± 5.0e-01

tests\unit\test_diffusion2d_functions.py:60: AssertionError
===================================================================== short test summary info ===================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 500.0 ± 5.0e-01 == array([[200.,...[200., 200.]])
=================================================================== 1 failed, 4 passed in 0.83s =================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py ...                                                                                                                 [100%] 

======================================================================== 5 passed in 0.74s ======================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py F..                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
_____________________________________________________________________ test_initialize_domain ______________________________________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 12.
        h = 14.
        dx = 0.3
        dy = 0.4

        solver = SolveDiffusion2D()
        solver.initialize_domain(w, h, dx, dy)

        expected_nx = pytest.approx(40., abs=0.001)
        expected_ny = pytest.approx(35., abs=0.001)

>       assert expected_nx == solver.nx
E       assert 40.0 ± 1.0e-03 == 46
E         comparison failed
E         Obtained: 46
E         Expected: 40.0 ± 1.0e-03

tests\unit\test_diffusion2d_functions.py:24: AssertionError
```
Initialize physical parameters
```
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py ..F                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
___________________________________________________________________ test_set_initial_condition ____________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 3
        solver.ny = 2
        solver.dx = 0.3
        solver.dy = 0.4
        solver.T_cold = 200.
        solver.T_hot = 700.
        actual_u = solver.set_initial_condition()
        expected_u = pytest.approx(500.0, 0.001)
>       assert expected_u == actual_u
E       assert 500.0 ± 5.0e-01 == array([[200.,...[200., 200.]])
E         comparison failed
E         Obtained: [[200. 200.]\n [200. 200.]\n [200. 200.]]
E         Expected: 500.0 ± 5.0e-01

tests\unit\test_diffusion2d_functions.py:60: AssertionError
===================================================================== short test summary info ===================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 500.0 ± 5.0e-01 == array([[200.,...[200., 200.]])
=================================================================== 1 failed, 4 passed in 0.83s =================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py ...                                                                                                                 [100%] 

======================================================================== 5 passed in 0.74s ======================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py F..                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
_____________________________________________________________________ test_initialize_domain ______________________________________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 12.
        h = 14.
        dx = 0.3
        dy = 0.4

        solver = SolveDiffusion2D()
        solver.initialize_domain(w, h, dx, dy)

        expected_nx = pytest.approx(40., abs=0.001)
        expected_ny = pytest.approx(35., abs=0.001)

>       assert expected_nx == solver.nx
E       assert 40.0 ± 1.0e-03 == 46
E         comparison failed
E         Obtained: 46
E         Expected: 40.0 ± 1.0e-03

tests\unit\test_diffusion2d_functions.py:24: AssertionError
===================================================================== short test summary info ===================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40.0 ± 1.0e-03 == 46
=================================================================== 1 failed, 4 passed in 0.94s =================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%] 
tests\unit\test_diffusion2d_functions.py .F.                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
_______________________________________________________________ test_initialize_physical_parameters _______________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        d = 2.
        T_cold = 200.
        T_hot = 700.

        solver = SolveDiffusion2D()
        solver.dx = 0.3
        solver.dy = 0.4
        solver.initialize_physical_parameters(d, T_cold, T_hot)

        expected_dt = pytest.approx(0.0144, abs=0.0001)
>       assert expected_dt == solver.dt
E       assert 0.0144 ± 1.0e-04 == 0.017142857142857144
E         comparison failed
E         Obtained: 0.017142857142857144
E         Expected: 0.0144 ± 1.0e-04

tests\unit\test_diffusion2d_functions.py:43: AssertionError
---------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------- 
dt = 0.017142857142857144
===================================================================== short test summary info ===================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0144 ± 1.0e-04 == 0.017142857142857144

```

Set initial condition
```
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 5 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [ 40%]
tests\unit\test_diffusion2d_functions.py ..F                                                                                                                 [100%]

============================================================================ FAILURES ============================================================================= 
___________________________________________________________________ test_set_initial_condition ____________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 3
        solver.ny = 2
        solver.dx = 0.3
        solver.dy = 0.4
        solver.T_cold = 200.
        solver.T_hot = 700.

        actual_u = solver.set_initial_condition()
        expected_u = np.array([[200., 200.], [200., 200.], [200., 200.]])
>       assert np.allclose(expected_u, actual_u)
E       assert False
E        +  where False = <function allclose at 0x00000197748FD5A0>(array([[200., 200.],\n       [200., 200.],\n       [200., 200.]]), array([[700., 700.],\n       [700., 700.],\n       [700., 700.]]))
E        +    where <function allclose at 0x00000197748FD5A0> = np.allclose

tests\unit\test_diffusion2d_functions.py:62: AssertionError
===================================================================== short test summary info ===================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False

```

### unittest log

Initialize domain
```
C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py:28: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(dx, self.solver.dx)
Fdt = 0.014400000000000003
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 30, in test_initialize_domain
    self.assertAlmostEqual(expected_nx, self.solver.nx)
AssertionError: 40.0 != 46 within 7 places (6.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m unittest discover tests/unit
Fdt = 0.014400000000000003
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 30, in test_initialize_domain
    self.assertAlmostEqual(expected_nx, self.solver.nx)
AssertionError: 40.0 != 46 within 7 places (6.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
```

Initialize physical parameters
```

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m unittest discover tests/unit
.dt = 0.014400000000000003
..
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m unittest discover tests/unit
.dt = 0.014400000000000003
..
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m unittest discover tests/unit
C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py:28: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(dx, self.solver.dx)
Fdt = 0.014400000000000003
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 30, in test_initialize_domain
    self.assertAlmostEqual(expected_nx, self.solver.nx)
AssertionError: 40.0 != 46 within 7 places (6.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m unittest discover tests/unit
Fdt = 0.014400000000000003
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 30, in test_initialize_domain
    self.assertAlmostEqual(expected_nx, self.solver.nx)
AssertionError: 40.0 != 46 within 7 places (6.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
```

Set initial condition
```
.dt = 0.014400000000000003
.F
======================================================================
FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\maxim\Documents\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 65, in test_set_initial_condition
    self.assertTrue(np.allclose(expected_u, actual_u))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
```

### integration test log

```
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 2 items                                                                                                                                                  

tests\integration\test_diffusion2d.py ..                                                                                                                     [100%] 

======================================================================== 2 passed in 0.95s ======================================================================== 
(ex_testing) PS C:\Users\maxim\Documents\testing-python-exercise-wt2223> python -m pytest tests/integration
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\maxim\Documents\testing-python-exercise-wt2223
collected 2 items                                                                                                                                                  

tests\integration\test_diffusion2d.py FF                                                                                                                     [100%]

============================================================================ FAILURES ============================================================================= 
_______________________________________________________________ test_initialize_physical_parameters _______________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        w = 12.
        h = 14.
        dx = 0.3
        dy = 0.4
        d = 2.
        T_cold = 200.
        T_hot = 700.

        solver.initialize_domain(w, h, dx, dy)

        solver.initialize_physical_parameters(d, T_cold, T_hot)

        expected_dt = pytest.approx(0.0144, abs=0.001)

>       assert expected_dt == solver.dt
E       assert 0.0144 ± 1.0e-03 == 0.01125
E         comparison failed
E         Obtained: 0.01125
E         Expected: 0.0144 ± 1.0e-03

tests\integration\test_diffusion2d.py:30: AssertionError
---------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------- 
dt = 0.01125
___________________________________________________________________ test_set_initial_condition ____________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        w = 12.
        h = 14.
        dx = 4.
        dy = 7.
        d = 2.
        T_cold = 200.
        T_hot = 700.

        solver.initialize_domain(w, h, dx, dy)

        solver.initialize_physical_parameters(d, T_cold, T_hot)

        u = solver.set_initial_condition()

        x = 2
        y = 3
        expected_u = np.array([[200. for i in range(x)] for j in range(y)])

>       assert np.allclose(expected_u, u)
E       assert False
E        +  where False = <function allclose at 0x000001727FB49630>(array([[200., 200.],\n       [200., 200.],\n       [200., 200.]]), array([[200., 200.],\n       [200., 700.],\n       [200., 200.]]))
E        +    where <function allclose at 0x000001727FB49630> = np.allclose

tests\integration\test_diffusion2d.py:58: AssertionError
---------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------- 
dt = 2.0
===================================================================== short test summary info ===================================================================== 
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0144 ± 1.0e-03 == 0.01125
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
======================================================================== 2 failed in 1.04s ========================================================================
```


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
