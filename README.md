# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

> Failed only one test, to show the logs. Easier to read!

============================================================================================== test session starts ===============================================================================================
platform win32 -- Python 3.8.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\EL6XJYW\Downloads\testing-python-exercise-wt2223-main
collected 3 items

tests\unit\test_diffusion2d_functions.py F..                                                                                                                                                                [100%]

==================================================================================================== FAILURES ==================================================================================================== 
_____________________________________________________________________________________________ test_initialize_domain _____________________________________________________________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        w, h, dx, dy = 1.0, 2.0, 2.0, 2.0
        solver.initialize_domain(
            w=w, h=h, dx=dx, dy=dy
        )

        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy

>       assert solver.nx == int(w / dx) + 1
E       assert 0 == (0 + 1)
E        +  where 0 = <diffusion2d.SolveDiffusion2D object at 0x000001757E36D5E0>.nx
E        +  and   0 = int((1.0 / 2.0))

tests\unit\test_diffusion2d_functions.py:25: AssertionError
============================================================================================ short test summary info ============================================================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 0 == (0 + 1)
========================================================================================== 1 failed, 2 passed in 0.96s =========================================================================================== 


### unittest log

> Failed only one test, to show the logs. Easier to read!

Testing started at 5:07 PM ...
Launching pytest with arguments C:/Users/EL6XJYW/Downloads/testing-python-exercise-wt2223-main/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in C:\Users\EL6XJYW\Downloads\testing-python-exercise-wt2223-main\tests\unit

============================= test session starts =============================
collecting ... collected 3 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain 
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition PASSED [ 33%]PASSED [ 66%]dt = 0.0006250000000000001
FAILED [100%]
test_diffusion2d_functions.py:47 (TestDiffusion2D.test_set_initial_condition)
array([[300.]]) != array([[299.]])

Expected :array([[299.]])
Actual   :array([[300.]])
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # could move all this to the setUp, true...
        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 10.
        self.solver.dy = 10.
        self.solver.nx = int(self.solver.w / self.solver.dx)
        self.solver.ny = int(self.solver.h / self.solver.dy)
    
        self.solver.d = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
    
        res = self.solver.set_initial_condition()
        _res = np.full((1, 1), 299.)
>       assert (res == _res).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x0000017BC9EDF0F0>()
E        +    where <built-in method all of numpy.ndarray object at 0x0000017BC9EDF0F0> = array([[300.]]) == array([[299.]])
E             Full diff:
E             - array([[299.]])
E             ?         ^^^
E             + array([[300.]])
E             ?         ^^^.all

test_diffusion2d_functions.py:66: AssertionError




========================= 1 failed, 2 passed in 0.64s =========================

Process finished with exit code 1

## integration test log

============================================================================================== test session starts ===============================================================================================
platform win32 -- Python 3.8.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\EL6XJYW\Downloads\testing-python-exercise-wt2223-main
collected 2 items

tests\integration\test_diffusion2d.py F.                                                                                                                                                                    [100%]

==================================================================================================== FAILURES ==================================================================================================== 
______________________________________________________________________________________ test_initialize_physical_parameters _______________________________________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(
            w=10., h=10., dx=10., dy=10.
        )
        solver.initialize_physical_parameters(
            d=3., T_cold=300., T_hot=700.
        )
        expected_dt = 8.33335
>       assert expected_dt == approx(solver.dt, abs=1e-5)
E       assert 8.33335 == 8.333333333333334 ± 1.0e-05
E         comparison failed
E         Obtained: 8.33335
E         Expected: 8.333333333333334 ± 1.0e-05

tests\integration\test_diffusion2d.py:21: AssertionError
---------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------- 
dt = 8.333333333333334
============================================================================================ short test summary info ============================================================================================= 
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 8.33335 == 8.333333333333334 ± 1.0e-05
========================================================================================== 1 failed, 1 passed in 0.91s ===========================================================================================

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
