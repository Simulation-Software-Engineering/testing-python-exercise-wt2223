# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

``` python
=========================================================== test session starts ===========================================================
platform linux -- Python 3.10.9, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/tim/Files/Documents/Uni/Lehre/SSE/exercises/testing-python-exercise-wt2223
collected 5 items

tests/integration/test_diffusion2d.py ..                                                                                            [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                        [100%]

================================================================ FAILURES =================================================================
_________________________________________________________ test_initialize_domain __________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        # Default params
        solver.initialize_domain()
        assert solver.w == 10.
        assert solver.h == 10.
        assert solver.dx == 0.1
        assert solver.dy == 0.1
        assert solver.nx == 100
        assert solver.ny == 100

        # Some different params
        solver.initialize_domain(20., 40., 0.08, 0.1)
        assert solver.w == 20.
        assert solver.h == 40.
        assert solver.dx == 0.08
        assert solver.dy == 0.1
>       assert solver.nx == 250
E       assert 500 == 250
E        +  where 500 = <diffusion2d.SolveDiffusion2D object at 0x7f035d177a90>.nx

tests/unit/test_diffusion2d_functions.py:37: AssertionError
___________________________________________________ test_initialize_physical_parameters ___________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        # Default params
        solver.dx = 0.1
        solver.dy = 0.1
        solver.initialize_physical_parameters()
        assert solver.D == 4.
        assert solver.T_cold == 300.
        assert solver.T_hot == 700.
        assert solver.dt == pytest.approx(0.0006250, abs=0.0000001)

        # Some different params
        solver.dx = 0.08
        solver.dy = 0.1
        solver.initialize_physical_parameters(10., 200., 800.)
        assert solver.D == 10.
        assert solver.T_cold == 200.
        assert solver.T_hot == 800.
>       assert solver.dt == pytest.approx(0.0001951, abs=0.0000001)
E       assert 0.0001248780487804878 == 0.0001951 ± 1.0e-07
E         comparison failed
E         Obtained: 0.0001248780487804878
E         Expected: 0.0001951 ± 1.0e-07

tests/unit/test_diffusion2d_functions.py:63: AssertionError
---------------------------------------------------------- Captured stdout call -----------------------------------------------------------
dt = 0.0006250000000000001
dt = 0.0001248780487804878
_______________________________________________________ test_set_initial_condition ________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        solver.dx = 1
        solver.dy = 2
        solver.nx = 10
        solver.ny = 5
        solver.T_cold = 300.
        solver.T_hot = 700.

        expected_result = np.ones((10, 5))*300
        for i in range(4, 7):
            for j in range(2, 4):
                expected_result[i][j] = 700

        actual_result = solver.set_initial_condition()

>       assert_almost_equal(actual_result, expected_result)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E
E       Mismatched elements: 9 / 50 (18%)
E       Max absolute difference: 400.
E       Max relative difference: 1.33333333
E        x: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...
E        y: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...

tests/unit/test_diffusion2d_functions.py:86: AssertionError
========================================================= short test summary info =========================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 500 == 250
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0001248780487804878 == 0.0001951 ± 1.0e-07
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError:
======================================================= 3 failed, 2 passed in 0.49s =======================================================
```

### unittest log

``` python
Fdt = 0.0006250000000000001
dt = 0.0001248780487804878
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tim/Files/Documents/Uni/Lehre/SSE/exercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 42, in test_initialize_domain
    self.assertEqual(self.solver.nx, 250)
AssertionError: 500 != 250

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tim/Files/Documents/Uni/Lehre/SSE/exercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 66, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.0001951, 7)
AssertionError: 0.0001248780487804878 != 0.0001951 within 7 places (7.02219512195122e-05 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tim/Files/Documents/Uni/Lehre/SSE/exercises/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 87, in test_set_initial_condition
    assert_almost_equal(actual_result, expected_result)
  File "/nix/store/jwhndh6ylcgbpyxf4d81z4rkvqfrk4lr-python3-3.10.9-env/lib/python3.10/site-packages/numpy/testing/_private/utils.py", line 583, in assert_almost_equal
    return assert_array_almost_equal(actual, desired, decimal, err_msg)
  File "/nix/store/jwhndh6ylcgbpyxf4d81z4rkvqfrk4lr-python3-3.10.9-env/lib/python3.10/site-packages/numpy/testing/_private/utils.py", line 1046, in assert_array_almost_equal
    assert_array_compare(compare, x, y, err_msg=err_msg, verbose=verbose,
  File "/nix/store/jwhndh6ylcgbpyxf4d81z4rkvqfrk4lr-python3-3.10.9-env/lib/python3.10/site-packages/numpy/testing/_private/utils.py", line 844, in assert_array_compare
    raise AssertionError(msg)
AssertionError:
Arrays are not almost equal to 7 decimals

Mismatched elements: 9 / 50 (18%)
Max absolute difference: 400.
Max relative difference: 1.33333333
 x: array([[300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],...
 y: array([[300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],...

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)

```

### integration test log

``` python
=========================================================== test session starts ===========================================================
platform linux -- Python 3.10.9, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/tim/Files/Documents/Uni/Lehre/SSE/exercises/testing-python-exercise-wt2223
collected 5 items

tests/integration/test_diffusion2d.py FF                                                                                            [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                        [100%]

================================================================ FAILURES =================================================================
___________________________________________________ test_initialize_physical_parameters ___________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        # Default params
        solver.initialize_domain()
        solver.initialize_physical_parameters()

        assert solver.dt == pytest.approx(0.0006250, abs=0.0000001)

        # Some different params
        solver.initialize_domain(20., 40., 0.08, 0.1)
        solver.initialize_physical_parameters(10., 200., 800.)

>       assert solver.dt == pytest.approx(0.0001951, abs=0.0000001)
E       assert 0.0001248780487804878 == 0.0001951 ± 1.0e-07
E         comparison failed
E         Obtained: 0.0001248780487804878
E         Expected: 0.0001951 ± 1.0e-07

tests/integration/test_diffusion2d.py:29: AssertionError
---------------------------------------------------------- Captured stdout call -----------------------------------------------------------
dt = 0.0006250000000000001
dt = 0.0001248780487804878
_______________________________________________________ test_set_initial_condition ________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        solver.initialize_domain(10., 10., 1., 2.)
        solver.initialize_physical_parameters(1., 300., 700.)

        expected_result = np.ones((10, 5))*300
        for i in range(4, 7):
            for j in range(2, 4):
                expected_result[i][j] = 700

        actual_result = solver.set_initial_condition()

>       assert_almost_equal(actual_result, expected_result)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E
E       Mismatched elements: 9 / 50 (18%)
E       Max absolute difference: 400.
E       Max relative difference: 1.33333333
E        x: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...
E        y: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...

tests/integration/test_diffusion2d.py:48: AssertionError
---------------------------------------------------------- Captured stdout call -----------------------------------------------------------
dt = 0.1
_________________________________________________ TestDiffusion2D.test_initialize_domain __________________________________________________

self = <tests.unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        # Default params
        self.solver.initialize_domain()
        self.assertEqual(self.solver.w, 10.)
        self.assertEqual(self.solver.h, 10.)
        self.assertEqual(self.solver.dx, 0.1)
        self.assertEqual(self.solver.dy, 0.1)
        self.assertEqual(self.solver.nx, 100)
        self.assertEqual(self.solver.ny, 100)

        # Some different params
        self.solver.initialize_domain(20., 40., 0.08, 0.1)
        self.assertEqual(self.solver.w, 20.)
        self.assertEqual(self.solver.h, 40.)
        self.assertEqual(self.solver.dx, 0.08)
        self.assertEqual(self.solver.dy, 0.1)
>       self.assertEqual(self.solver.nx, 250)
E       AssertionError: 500 != 250

tests/unit/test_diffusion2d_functions.py:42: AssertionError
___________________________________________ TestDiffusion2D.test_initialize_physical_parameters ___________________________________________

self = <tests.unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        # Default params
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters()
        self.assertEqual(self.solver.D, 4.)
        self.assertEqual(self.solver.T_cold, 300.)
        self.assertEqual(self.solver.T_hot, 700.)
        self.assertAlmostEqual(self.solver.dt, 0.0006250, 7)

        # Some different params
        self.solver.dx = 0.08
        self.solver.dy = 0.1
        self.solver.initialize_physical_parameters(10., 200., 800.)
        self.assertEqual(self.solver.D, 10.)
        self.assertEqual(self.solver.T_cold, 200.)
        self.assertEqual(self.solver.T_hot, 800.)
>       self.assertAlmostEqual(self.solver.dt, 0.0001951, 7)
E       AssertionError: 0.0001248780487804878 != 0.0001951 within 7 places (7.02219512195122e-05 difference)

tests/unit/test_diffusion2d_functions.py:66: AssertionError
---------------------------------------------------------- Captured stdout call -----------------------------------------------------------
dt = 0.0006250000000000001
dt = 0.0001248780487804878
_______________________________________________ TestDiffusion2D.test_set_initial_condition ________________________________________________

self = <tests.unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.dx = 1
        self.solver.dy = 2
        self.solver.nx = 10
        self.solver.ny = 5
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.

        expected_result = np.ones((10, 5))*300
        for i in range(4, 7):
            for j in range(2, 4):
                expected_result[i][j] = 700

        actual_result = self.solver.set_initial_condition()

>       assert_almost_equal(actual_result, expected_result)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E
E       Mismatched elements: 9 / 50 (18%)
E       Max absolute difference: 400.
E       Max relative difference: 1.33333333
E        x: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...
E        y: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...

tests/unit/test_diffusion2d_functions.py:87: AssertionError
========================================================= short test summary info =========================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0001248780487804878 == 0.0001951 ± 1.0e-07
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError:
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 500 != 250
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.00012487804878...
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError:
============================================================ 5 failed in 0.51s ============================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
