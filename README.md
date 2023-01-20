# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

================================================================ FAILURES ================================================================
_________________________________________________________ test_initialize_domain _________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # w=3., h=2., dx=1, dy=0.5
        solver.initialize_domain(3., 2., 1., 0.5)
    
        # Expected results
        expected_nx = 3
        expected_ny = 4
    
        # Actual results
        actual_nx = solver.nx
        actual_ny = solver.ny
    
        assert expected_nx == actual_nx
>       assert expected_ny == actual_ny
E       assert 4 == 2

tests/unit/test_diffusion2d_functions.py:27: AssertionError
__________________________________________________ test_initialize_physical_parameters ___________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # dx=1, dy=0.5
        # d=5., T_cold=200., T_hot=500.
        solver.dx, solver.dy = 1, 0.5
        solver.initialize_physical_parameters(5., 200., 500.)
    
        expected_dt = pytest.approx(0.02, abs=0.01)
    
        actual_dt = solver.dt
    
>       assert expected_dt == actual_dt
E       assert 0.02 ± 1.0e-02 == 0.08
E         comparison failed
E         Obtained: 0.08
E         Expected: 0.02 ± 1.0e-02

tests/unit/test_diffusion2d_functions.py:45: AssertionError
---------------------------------------------------------- Captured stdout call ----------------------------------------------------------
dt = 0.08
_______________________________________________________ test_set_initial_condition _______________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        # nx=3, ny=4, T_cold=200
        solver.nx, solver.ny = 3, 4
        solver.dx, solver.dy = 1, 0.5
        solver.T_cold, solver.T_hot = 200, 500
    
        expected_u = 200 * np.ones((3,4))
    
        actual_u = solver.set_initial_condition()
    
        for i in range(3):
            for j in range(4):
>               assert expected_u[i,j] == actual_u[i,j]
E               assert 200.0 == 500.0

tests/unit/test_diffusion2d_functions.py:64: AssertionError
======================================================== short test summary info =========================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 4 == 2
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.02 ± 1.0e-02 == 0.08
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 200.0 == 500.0
=========================================================== 3 failed in 0.44s ============================================================

### unittest log

Fdt = 0.08
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan/Documents/WS23/SSR/Exercises/python-testing/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 36, in test_initialize_domain
    self.assertEqual(expected_ny, actual_ny)
AssertionError: 4 != 2

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan/Documents/WS23/SSR/Exercises/python-testing/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 49, in test_initialize_physical_parameters
    self.assertAlmostEqual(expected_dt, actual_dt, 2)
AssertionError: 0.02 != 0.08 within 2 places (0.06 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan/Documents/WS23/SSR/Exercises/python-testing/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 66, in test_set_initial_condition
    self.assertEqual(expected_u[i,j], actual_u[i,j])
AssertionError: 200.0 != 500.0

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
