# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```code
$ python3 -m pytest tests/unit/test_diffusion2d_functions.py
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/nimo/SSE/exercise8/testing-python-exercise-wt2223
plugins: xdist-3.1.0, allure-pytest-2.12.0, metadata-2.0.4, rerunfailures-11.0, anyio-3.6.2, json-report-1.5.0, Faker-16.6.0, order-1.0.1
collected 3 items                                                                                                                                                                                                 

tests/unit/test_diffusion2d_functions.py F..                                                                                                                                                                [100%]

==================================================================================================== FAILURES =====================================================================================================
_____________________________________________________________________________________________ test_initialize_domain ______________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        expected_nx = 1
        expected_ny = 1
        solver.initialize_domain( w=5., h=20., dx=5., dy=20.)
>       assert solver.nx == expected_nx and solver.ny == expected_ny
E       assert (4 == 1)
E        +  where 4 = <diffusion2d.SolveDiffusion2D object at 0x7f66d7620100>.nx

tests/unit/test_diffusion2d_functions.py:16: AssertionError
============================================================================================= short test summary info =============================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert (4 == 1)
=========================================================================================== 1 failed, 2 passed in 0.38s ===========================================================================================

```

```code
$ python -m pytest tests/unit/test_diffusion2d_functions.py 
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/nimo/SSE/exercise8/testing-python-exercise-wt2223
plugins: xdist-3.1.0, allure-pytest-2.12.0, metadata-2.0.4, rerunfailures-11.0, anyio-3.6.2, json-report-1.5.0, Faker-16.6.0, order-1.0.1
collected 3 items                                                                                                                                                                                                 

tests/unit/test_diffusion2d_functions.py .F.                                                                                                                                                                [100%]

==================================================================================================== FAILURES =====================================================================================================
_______________________________________________________________________________________ test_initialize_physical_parameters _______________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 5.
        solver.dy = 20.
        expected_dx2, expected_dy2 = 25., 400.
        expected_dt = pytest.approx(11.76,abs=0.01)
    
        solver.initialize_physical_parameters(d=1., T_cold=3., T_hot=2.)
    
>       assert expected_dt == solver.dt
E       assert 11.76 ± 1.0e-02 == 40.0
E         comparison failed
E         Obtained: 40.0
E         Expected: 11.76 ± 1.0e-02

tests/unit/test_diffusion2d_functions.py:30: AssertionError
---------------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------------
dt = 40.0
============================================================================================= short test summary info =============================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 11.76 ± 1.0e-02 == 40.0
=========================================================================================== 1 failed, 2 passed in 0.36s ===========================================================================================

```

```code
$ python -m pytest tests/unit/test_diffusion2d_functions.py 
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/nimo/SSE/exercise8/testing-python-exercise-wt2223
plugins: xdist-3.1.0, allure-pytest-2.12.0, metadata-2.0.4, rerunfailures-11.0, anyio-3.6.2, json-report-1.5.0, Faker-16.6.0, order-1.0.1
collected 3 items                                                                                                                                                                                                 

tests/unit/test_diffusion2d_functions.py ..F                                                                                                                                                                [100%]

==================================================================================================== FAILURES =====================================================================================================
___________________________________________________________________________________________ test_set_initial_condition ____________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx, solver.ny = 5, 5
        solver.dx, solver.dy = 5., 20.
        solver.T_cold, solver.T_hot = 3., 2.
    
        expected_u = [[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,],[3., 3., 3., 3., 3.,]]
    
        actual_u = solver.set_initial_condition()
    
>       assert (expected_u == actual_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f2682ba7030>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f2682ba7030> = [[3.0, 3.0, 3....0, 3.0, 3.0]] == array([[3., 3... 3., 3., 3.]])
E             Use -v to get more diff.all

tests/unit/test_diffusion2d_functions.py:46: AssertionError
============================================================================================= short test summary info =============================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
=========================================================================================== 1 failed, 2 passed in 0.38s ===========================================================================================

```

```code
$ python -m unittest tests/unit/test_diffusion2d_functions.py 
F
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/nimo/SSE/exercise8/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 21, in test_initialize_domain
    self.assertEqual(self.solver.nx,expected_nx)
AssertionError: 4 != 1

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

```

```code
$ python -m unittest tests/unit/test_diffusion2d_functions.py 
.dt = 40.0
F
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/nimo/SSE/exercise8/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 35, in test_initialize_physical_parameters
    self.assertAlmostEqual(expected_dt, self.solver.dt,2)
AssertionError: 11.76 != 40.0 within 2 places (28.240000000000002 difference)

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)

```

```code
$ python -m unittest tests/unit/test_diffusion2d_functions.py 
.dt = 11.764705882352942
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/nimo/SSE/exercise8/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 51, in test_set_initial_condition
    self.assertTrue(np.array_equal(expected_u, actual_u))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
