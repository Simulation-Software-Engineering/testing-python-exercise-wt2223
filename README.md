# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/sumanth0703/Desktop/testing-python-exercise-wt2223
collected 3 items                                                              

tests/unit/test_diffusion2d_functions.py FFF                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 200
        expected_ny = 50
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20.,h=10.,dx=0.1,dy=0.2)
    
>       assert expected_nx == solver.nx
E       assert 200 == 201
E        +  where 201 = <diffusion2d.SolveDiffusion2D object at 0x7fb612c91360>.nx

tests/unit/test_diffusion2d_functions.py:18: AssertionError
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx=0.2
        solver.dy=0.1
        #expected_dt = pytest.approx(0.0008, abs=0.0001)
        solver.initialize_physical_parameters(d=5., T_cold=400., T_hot=600.)
>       assert solver.dt == pytest.approx(0.0008)
E       assert -0.0492 == 0.0008 ± 8.0e-10
E         comparison failed
E         Obtained: -0.0492
E         Expected: 0.0008 ± 8.0e-10

tests/unit/test_diffusion2d_functions.py:30: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = -0.0492
__________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 10
        solver.ny = 10
        solver.d = 4.
        solver.T_cold = 300.
        solver.T_hot = 700.
        solver.dx=0.1
        solver.dy=0.1
        u = solver.set_initial_condition()
        expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 4, 10, 10
        r2 = r ** 2
        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = solver.T_hot
    
>       assert(u == expected_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7fb612cb9710>()
E        +    where <built-in method all of numpy.ndarray object at 0x7fb612cb9710> = array([[350.,... 350., 350.]]) == array([[300.,... 300., 300.]])
E             Use -v to get more diff.all

tests/unit/test_diffusion2d_functions.py:56: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 200 == 201
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert -0.0492 == 0.0008 ± 8.0e-10
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False


### unittest log

Fdt = -0.0492
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2d)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sumanth0703/Desktop/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 25, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_nx)
AssertionError: 201 != 200

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2d)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sumanth0703/Desktop/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 38, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.0008)
AssertionError: -0.0492 != 0.0008 within 7 places (0.05 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2d)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sumanth0703/Desktop/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 63, in test_set_initial_condition
    self.assertTrue((u == expected_u).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
