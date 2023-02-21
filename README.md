# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### One Broken function

```
=================================================== test session starts ===================================================
platform win32 -- Python 3.10.0, pytest-7.2.0, pluggy-1.0.0
rootdir: D:\GitHub\SSE\testing-python-exercise-wt2223
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                             [ 40%]
tests\unit\test_diffusion2d_functions.py F..                                                                         [100%]

======================================================== FAILURES =========================================================
_________________________________________________ test_initialize_domain __________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        for i in range(1000):
            w = np.random.rand() * 100
            h = np.random.rand() * 100
            dx = np.random.rand()
            dy = np.random.rand()
            solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
>           assert solver.nx == w // dx
E           assert 445 == (39.55370833910049 // 0.17907525324321327)
E            +  where 445 = <diffusion2d.SolveDiffusion2D object at 0x000001990145F190>.nx

tests\unit\test_diffusion2d_functions.py:22: AssertionError
================================================= short test summary info =================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 445 == (39.55370833910049 // 0.17907525324321327)
=============================================== 1 failed, 4 passed in 1.21s ===============================================
```

#### all functions broken:

```
============================================================================================================================================= test session starts =============================================================================================================================================
platform win32 -- Python 3.10.7, pytest-7.2.1, pluggy-1.0.0
rootdir: D:\Repositories\SimulationSoftwareEngineering\testing-python-exercise-wt2223
collected 3 items                                                                                                                                                                                                                                                                                              

tests\unit\test_diffusion2d_functions.py FFF                                                                                                                                                                                                                                                             [100%]

================================================================================================================================================== FAILURES ===================================================================================================================================================
___________________________________________________________________________________________________________________________________ TestDiffusion2D.test_initialize_domain ____________________________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        for i in range(10):
            w = np.random.rand() * 100
            h = np.random.rand() * 100
            dx = np.random.rand()
            dy = np.random.rand()
            self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
>           self.assertEqual(self.solver.nx, w // dx)
E           AssertionError: 4 != 21.0

tests\unit\test_diffusion2d_functions.py:28: AssertionError
_____________________________________________________________________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters _____________________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100

        dx2, dy2 = self.solver.dx ** 2, self.solver.dy**2

        for i in range(10):
            d = np.random.rand() * 100
            T_cold = np.random.rand() * 10000
            T_hot = np.random.rand() * 10000
            self.solver.initialize_physical_parameters(
                d=d, T_cold=T_cold, T_hot=T_hot)

            self.assertEqual(self.solver.D, d)
            self.assertEqual(self.solver.T_cold, T_cold)
            self.assertEqual(self.solver.T_hot, T_hot)

            dt = dx2 * dy2 / (2 * self.solver.D * (dx2 + dy2))
>           self.assertAlmostEqual(self.solver.dt, dt, 5)
E           AssertionError: 4.028530148514474e-05 != 8.057060297028948e-05 within 5 places (4.028530148514474e-05 difference)

tests\unit\test_diffusion2d_functions.py:56: AssertionError
-------------------------------------------------------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------------------------------------------------------
dt = 4.028530148514474e-05
_________________________________________________________________________________________________________________________________ TestDiffusion2D.test_set_initial_condition __________________________________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.w = 10.
        self.solver.h = 10.
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100
        self.solver.D = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
        self.solver.dt = 0.000625

        u = self.solver.set_initial_condition()
        self.assertEqual(u.shape, (100, 100))
        self.assertEqual(u.min(), self.solver.T_cold)
>       self.assertEqual(u.max(), self.solver.T_hot)
E       AssertionError: 1400.0 != 700.0

tests\unit\test_diffusion2d_functions.py:77: AssertionError
=========================================================================================================================================== short test summary info ===========================================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 4 != 21.0
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 4.028530148514474e-05 != 8.057060297028948e-05 within 5 places (4.028530148514474e-05 difference)
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: 1400.0 != 700.0
============================================================================================================================================== 3 failed in 0.49s ==============================================================================================================================================
```

### unittest log

```
Fdt = 4.448331115120221e-05
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Repositories\SimulationSoftwareEngineering\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 28, in test_initialize_domain
    self.assertEqual(self.solver.nx, w // dx)
AssertionError: 124 != 34.0

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Repositories\SimulationSoftwareEngineering\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 56, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, dt, 5)
AssertionError: 4.448331115120221e-05 != 8.896662230240442e-05 within 5 places (4.448331115120221e-05 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Repositories\SimulationSoftwareEngineering\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 77, in test_set_initial_condition
    self.assertEqual(u.max(), self.solver.T_hot)
AssertionError: 1400.0 != 700.0

----------------------------------------------------------------------
Ran 3 tests in 0.007s

FAILED (failures=3)
```

### Integration Test Log

```
======================================================================================================== test session starts ========================================================================================================
platform win32 -- Python 3.10.7, pytest-7.2.1, pluggy-1.0.0
rootdir: D:\Repositories\SimulationSoftwareEngineering\testing-python-exercise-wt2223
collected 2 items

tests\integration\test_diffusion2d.py FF                                                                                                                                                                                       [100%]

============================================================================================================= FAILURES ==============================================================================================================
________________________________________________________________________________________________ test_initialize_physical_parameters ________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=54846., h=546., dx=0.3, dy=0.5)
        solver.initialize_physical_parameters(d=6., T_cold=400., T_hot=420.)

        expected = pytest.approx(0.00551, 0.001)
>       assert solver.dt == expected
E       assert 0.0027573529411764703 == 0.00551 ± 5.5e-06
E         comparison failed
E         Obtained: 0.0027573529411764703
E         Expected: 0.00551 ± 5.5e-06

tests\integration\test_diffusion2d.py:19: AssertionError
------------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------------
dt = 0.0027573529411764703
____________________________________________________________________________________________________ test_set_initial_condition _____________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(100., 100., 0.1, .1)
        solver.initialize_physical_parameters(4., 1., 1.)

        actual_u = solver.set_initial_condition()
        expected_u = np.ones((1000, 1000))
>       assert np.array_equal(expected_u, actual_u)
E       assert False
E        +  where False = <function array_equal at 0x00000260D28ABEB0>(array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1.,
1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]), array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]))
E        +    where <function array_equal at 0x00000260D28ABEB0> = np.array_equal

tests\integration\test_diffusion2d.py:32: AssertionError
------------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------------
dt = 0.00031250000000000006
====================================================================================================== short test summary info ======================================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0027573529411764703 == 0.00551 ± 5.5e-06
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
========================================================================================================= 2 failed in 0.92s =========================================================================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
