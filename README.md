# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

================================================================ test session starts =================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/strack/git-workspace/testing-python-exercise-wt2223
collected 5 items                                                                                                                                    

tests/integration/test_diffusion2d.py ..                                                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                   [100%]

====================================================================== FAILURES ======================================================================
_______________________________________________________________ test_initialize_domain _______________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # Fixture
        w = 10.5
        h = 7.3
        dx = 0.2
        dy = 0.2
    
        # Expected Results
        expected_nx = 52
        expected_ny = 36
    
        # Actual Results
        solver.initialize_domain(w,h,dx,dy)
        actual_nx = solver.nx
        actual_ny = solver.ny
    
        # Tests
>       assert expected_nx == actual_nx
E       assert 52 == 36

tests/unit/test_diffusion2d_functions.py:30: AssertionError
________________________________________________________ test_initialize_physical_parameters _________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        #Fixture
        d = 3.
        solver.dx = 0.2
        solver.dy = 0.2
    
    
        #Expected Result
        dx2, dy2 = solver.dx * solver.dx, solver.dy * solver.dy
        expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
    
        #Actual Result
        solver.initialize_physical_parameters(d)
        actual_dt = solver.dt
    
        #Test
>       assert expected_dt == actual_dt
E       assert 0.0033333333333333344 == 0.0016666666666666672

tests/unit/test_diffusion2d_functions.py:55: AssertionError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
dt = 0.0016666666666666672
_____________________________________________________________ test_set_initial_condition _____________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
    
        solver = SolveDiffusion2D()
    
        #Fixture
        solver.T_cold = 400
        solver.T_hot = 800
        solver.nx = 52
        solver.ny = 36
        solver.dx = 0.2
        solver.dy = 0.2
    
        #Expected Result
        expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    
        #Actual Result
        actual_u = solver.set_initial_condition()
    
        #Test
>       assert (expected_u==actual_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7fc909a01fb0>()
E        +    where <built-in method all of numpy.ndarray object at 0x7fc909a01fb0> = array([[400.,... 400., 400.]]) == array([[800.,... 800., 800.]])
E             Use -v to get more diff.all

tests/unit/test_diffusion2d_functions.py:79: AssertionError
============================================================== short test summary info ===============================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 52 == 36
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0033333333333333344 == 0.0016666666666666672
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
============================================================ 3 failed, 2 passed in 0.42s =============================================================

### unittest log

Fdt = 0.0016666666666666672
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/strack/git-workspace/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 45, in test_initialize_domain
    self.assertEqual(expected_nx, actual_nx)
AssertionError: 52 != 36

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/strack/git-workspace/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 70, in test_initialize_physical_parameters
    self.assertEqual(expected_dt, actual_dt)
AssertionError: 0.0033333333333333344 != 0.0016666666666666672

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/strack/git-workspace/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 92, in test_set_initial_condition
    self.assertTrue((expected_u==actual_u).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)

### Integrationtest log 
================================================================ test session starts =================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/strack/git-workspace/testing-python-exercise-wt2223
collected 2 items                                                                                                                                    

tests/integration/test_diffusion2d.py::test_initialize_physical_parameters FAILED                                                              [ 50%]
tests/integration/test_diffusion2d.py::test_set_initial_condition FAILED                                                                       [100%]

====================================================================== FAILURES ======================================================================
________________________________________________________ test_initialize_physical_parameters _________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        #Fixture
        w =  10.5
        h = 7.3
        dx = 0.2
        dy = 0.2
        d = 3.
        T_cold = 400
        T_hot = 800
    
        #Expected Result
        expected_dt = pytest.approx(0.003, 0.2)
    
        #Actual Result
        solver.initialize_domain(w,h,dx,dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        actual_dt = solver.dt
    
        #Tests
>       assert expected_dt == actual_dt
E       assert 0.003 ± 6.0e-04 == 0.0016666666666666672
E         comparison failed
E         Obtained: 0.0016666666666666672
E         Expected: 0.003 ± 6.0e-04

tests/integration/test_diffusion2d.py:33: AssertionError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
dt = 0.0016666666666666672
_____________________________________________________________ test_set_initial_condition _____________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        #Fixture
        w =  10.5
        h = 7.3
        dx = 0.2
        dy = 0.2
        d = 3.
        T_cold = 400
        T_hot = 800
    
        solver.initialize_domain(w,h,dx,dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        #Expected Result
        expected_u = T_cold * np.ones((solver.nx, solver.ny))
    
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = 800.
    
        #Actual Result
        actual_u = solver.set_initial_condition()
    
        #Tests
>       assert (expected_u==actual_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f11112b16b0>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f11112b16b0> = array([[400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]]) == array([[400., 400., 400., ..., 800., 800., 800.],\n       [400., 400., 400., ..., 800., 800., 800.],\n       [400., 400., 400., ..., 800., 800., 800.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]])
E             Full diff:
E             - array([[400., 400., 400., ..., 800., 800., 800.],
E             ?                                ^     ^     ^
E             + array([[400., 400., 400., ..., 400., 400., 400.],
E             ?                                ^     ^     ^
E             -        [400., 400., 400., ..., 800., 800., 800.],
E             ?                                ^     ^     ^
E             +        [400., 400., 400., ..., 400., 400., 400.],
E             ?                                ^     ^     ^
E             -        [400., 400., 400., ..., 800., 800., 800.],
E             ?                                ^     ^     ^
E             +        [400., 400., 400., ..., 400., 400., 400.],
E             ?                                ^     ^     ^
E                      ...,
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.]],
E               ).all

tests/integration/test_diffusion2d.py:69: AssertionError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
dt = 0.0016666666666666672
============================================================== short test summary info ===============================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.003 ± 6.0e-04 == 0.0016666666666666672
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
================================================================= 2 failed in 0.42s ==================================================================


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
