# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```code

===================================================== test session starts ======================================================
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\ACER\Documents\SSEexercises\testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 3 items                                                                                                              

tests/unit/test_diffusion2d_functions.py F..                                                                             [100%]

=========================================================== FAILURES ===========================================================
____________________________________________________ test_initialize_domain ____________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        nx = 30
        ny = 50
        solver.initialize_domain(w = 15.0, h = 20.0, dx = 0.5, dy = 0.4)
>       assert solver.nx == nx
E       assert 40 == 30
E        +  where 40 = <diffusion2d.SolveDiffusion2D object at 0x111d9a650>.nx

tests/unit/test_diffusion2d_functions.py:16: AssertionError
=================================================== short test summary info ====================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40 == 30
================================================= 1 failed, 2 passed in 1.18s ==================================================

```

```code

===================================================== test session starts ======================================================
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\ACER\Documents\SSEexercises\testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 3 items                                                                                                              

tests/unit/test_diffusion2d_functions.py .F.                                                                             [100%]

=========================================================== FAILURES ===========================================================
_____________________________________________ test_initialize_physical_parameters ______________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        dx2, dy2 = 1, 4
        solver.dx, solver.dy = 1, 2
        dt = pytest.approx(0.1333, abs = 0.0001)
        solver.initialize_physical_parameters(d=3., T_cold=350., T_hot = 650.)
>       assert solver.dt == dt
E       assert 0.2222222222222222 == 0.1333 ± 1.0e-04
E         comparison failed
E         Obtained: 0.2222222222222222
E         Expected: 0.1333 ± 1.0e-04

tests/unit/test_diffusion2d_functions.py:28: AssertionError
----------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.2222222222222222
=================================================== short test summary info ====================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.2222222222222222 == 0.1333 ± 1.0e-04
================================================= 1 failed, 2 passed in 1.25s ==================================================

```

```code

===================================================== test session starts ======================================================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\ACER\Documents\SSEexercises\testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 3 items                                                                                                              

tests/unit/test_diffusion2d_functions.py ..F                                                                             [100%]

=========================================================== FAILURES ===========================================================
__________________________________________________ test_set_initial_condition __________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 300.
        solver.T_hot = 700.
        solver.nx = 5
        solver.ny = 5
        solver.dx = 2.
        solver.dy = 3.
        test_op = [[300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 700., 300., 300.],
                    [300., 300., 300., 300., 300.]]
        main_op = solver.set_initial_condition()
>       assert (main_op == test_op).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x1152579f0>()
E        +    where <built-in method all of numpy.ndarray object at 0x1152579f0> = array([[300.,... 300., 300.]]) == [[300.0, 300....300.0, 300.0]]
E             Use -v to get more diff.all

tests/unit/test_diffusion2d_functions.py:57: AssertionError
=================================================== short test summary info ====================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================================= 1 failed, 2 passed in 1.12s ==================================================

```

### unittest log

```code

Fdt = 0.13333333333333333
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ACER/Documents/SSEexercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 28, in test_initialize_domain
    self.assertEqual(self.solver.nx, nx)
AssertionError: 7 != 10

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

```

```code

.dt = 0.08333333333333333
F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ACER/Documents/SSEexercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 43, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, dt)
AssertionError: 0.08333333333333333 != 0.1333 ± 1.0e-04

----------------------------------------------------------------------
Ran 3 tests in 0.056s

FAILED (failures=1)

```

```code

.dt = 0.13333333333333333
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ACER/Documents/SSEexercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 59, in test_set_initial_condition
    self.assertTrue(np.array_equal(test_op, main_op))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)

```

### Integration tests log

```code

===================================================== test session starts ======================================================
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\ACER\Documents\SSEexercises\testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 2 items                                                                                                              

tests/integration/test_diffusion2d.py FF                                                                                 [100%]

=========================================================== FAILURES ===========================================================
_____________________________________________ test_initialize_physical_parameters ______________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20.,h=15.,dx=2., dy=3.)
        solver.initialize_physical_parameters(d=3.,T_cold=350.,T_hot=650.)
>       assert solver.dt== 0.46153846153846156
E       assert 0.75 == 0.46153846153846156
E        +  where 0.75 = <diffusion2d.SolveDiffusion2D object at 0x110c0c9d0>.dt

tests/integration/test_diffusion2d.py:15: AssertionError
----------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.75
__________________________________________________ test_set_initial_condition __________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20.,h=15.,dx=2., dy=3.)
        solver.initialize_physical_parameters(d=3.,T_cold=300.,T_hot=700.)
        test_op = [[300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 700., 300., 300.],
                        [300., 300., 700., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.]]
        generated_op = solver.set_initial_condition()
>       assert (test_op == generated_op).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x110cd41b0>()
E        +    where <built-in method all of numpy.ndarray object at 0x110cd41b0> = [[300.0, 300...., 300.0], ...] == array([[300.,... 300., 300.]])
E             Use -v to get more diff.all

tests/integration/test_diffusion2d.py:35: AssertionError
----------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.75
=================================================== short test summary info ====================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.75 == 0.46153846153846156
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
====================================================== 2 failed in 1.00s =======================================================

```

```code

===================================================== test session starts ======================================================
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\ACER\Documents\SSEexercises\testing-python-exercise-wt2223
plugins: anyio-3.5.0
collected 2 items                                                                                                              

tests/integration/test_diffusion2d.py .F                                                                                 [100%]

=========================================================== FAILURES ===========================================================
__________________________________________________ test_set_initial_condition __________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20.,h=15.,dx=2., dy=3.)
        solver.initialize_physical_parameters(d=3.,T_cold=300.,T_hot=700.)
        test_op = [[300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 700., 300., 300.],
                        [300., 300., 700., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.]]
        generated_op = solver.set_initial_condition()
>       assert (test_op == generated_op).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x114d8b870>()
E        +    where <built-in method all of numpy.ndarray object at 0x114d8b870> = [[300.0, 300...., 300.0], ...] == array([[300.,... 300., 300.]])
E             Use -v to get more diff.all

tests/integration/test_diffusion2d.py:35: AssertionError
----------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.46153846153846156
=================================================== short test summary info ====================================================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
================================================= 1 failed, 1 passed in 0.79s ==================================================

```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).