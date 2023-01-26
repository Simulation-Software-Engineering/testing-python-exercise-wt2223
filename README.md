# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

Run with ```python -m pytest```

```
=============================================================================================== FAILURES ===============================================================================================
________________________________________________________________________________________ test_initialize_domain ________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(2.,20.,0.1,0.1)
>       assert solver.nx == 20.
E       assert 200 == 20.0
E        +  where 200 = <diffusion2d.SolveDiffusion2D object at 0x000001DBC48D6980>.nx

tests\unit\test_diffusion2d_functions.py:14: AssertionError
======================================================================================= short test summary info ======================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 200 == 20.0
===================================================================================== 1 failed, 4 passed in 0.41s ====================================================================================== 
```

```
======================================================================================== test session starts =========================================================================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                                                                                                        [ 40%] 
tests\unit\test_diffusion2d_functions.py .F.                                                                                                                                                    [100%]

============================================================================================== FAILURES ============================================================================================== 
________________________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        expected_value = 0.0005000000000000001

        solver = SolveDiffusion2D()
        solver.dx = 0.1
        solver.dy = 0.1
        solver.initialize_physical_parameters(5.,400.,800.)
        assert solver.D == 5.
>       assert solver.T_cold == 400.
E       assert 800.0 == 400.0
E        +  where 800.0 = <diffusion2d.SolveDiffusion2D object at 0x000001A35C3131C0>.T_cold

tests\unit\test_diffusion2d_functions.py:29: AssertionError
---------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------- 
dt = 0.0005000000000000001
====================================================================================== short test summary info ======================================================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 800.0 == 400.0
==================================================================================== 1 failed, 4 passed in 0.42s ===================================================================================== 
```

```
===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                                                                                                 [ 40%] 
tests\unit\test_diffusion2d_functions.py ..F                                                                                                                                             [100%]

========================================================================================== FAILURES =========================================================================================== 
_________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_value = np.array([[300., 300., 300.],[300., 300., 700.]])

        solver = SolveDiffusion2D()
        solver.dx = 5
        solver.dy = 3
        solver.nx = 2
        solver.ny = 3
        solver.T_cold = 300
        solver.T_hot = 700

>       assert (solver.set_initial_condition() == expected_value).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x00000175E5D7E310>()
E        +    where <built-in method all of numpy.ndarray object at 0x00000175E5D7E310> = array([[300.,... 300., 300.]]) == array([[300.,... 300., 700.]])
E             Use -v to get more diff.all

tests\unit\test_diffusion2d_functions.py:48: AssertionError
=================================================================================== short test summary info =================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================================================================= 1 failed, 4 passed in 0.42s =================================================================================
```

### unittest log

Run with ```python -m unittest discover```

```
Fdt = 0.0005000000000000001
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 19, in test_initialize_domain
    self.assertEqual(self.solver.nx, 20)
AssertionError: 200 != 20

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

```
.dt = 0.0013333333333333337
F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 35, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, expected_value)
AssertionError: 0.0013333333333333337 != 0.0008000000000000001

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

```
.dt = 0.0008000000000000001
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 51, in test_set_initial_condition
    self.assertTrue((self.solver.set_initial_condition() == expected_value).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

### Integration Tests
```
===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223
collected 8 items

tests\integration\test_diffusion2d.py ..                                                                                                                                                 [ 25%] 
tests\unit\test_diffusion2d_functions.py .F....                                                                                                                                          [100%]

========================================================================================== FAILURES =========================================================================================== 
_____________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters _____________________________________________________________________ 

self = <tests.unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        expected_value = 0.0008000000000000001

        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(5.,400.,800.)
        self.assertEqual(self.solver.D, 5.)
        self.assertEqual(self.solver.T_cold, 400.)
        self.assertEqual(self.solver.T_hot, 800.)
>       self.assertEqual(self.solver.dt, expected_value)
E       AssertionError: 0.0013333333333333337 != 0.0008000000000000001

tests\unit\test_diffusion2d_functions.py:35: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------- 
dt = 0.0013333333333333337
=================================================================================== short test summary info =================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.0013333333333333337 != 0.0008000000000000001
================================================================================= 1 failed, 7 passed in 0.48s ================================================================================= 
```

```
===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Andreas\Desktop\Uni\testing-python-exercise-wt2223
collected 8 items

tests\integration\test_diffusion2d.py .F                                                                                                                                                 [ 25%]
tests\unit\test_diffusion2d_functions.py ..F..F                                                                                                                                          [100%] 

========================================================================================== FAILURES =========================================================================================== 
_________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        exp_w = 10.
        exp_h = 9.
        exp_dx = 5.
        exp_dy = 3.
        exp_nx = int(exp_w/exp_dx)
        exp_ny = int(exp_h/exp_dy)
        exp_d = 4.
        exp_t_cold = 300.
        exp_t_hot = 700.

        exp_u = exp_t_cold * np.ones((exp_nx, exp_ny))
        exp_r, exp_cx, exp_cy = 2, 5, 5
        exp_r2 = exp_r ** 2
        for i in range(exp_nx):
            for j in range(exp_ny):
                exp_p2 = (i * exp_dx - exp_cx) ** 2 + (j * exp_dy - exp_cy) ** 2
                if exp_p2 < exp_r2:
                    exp_u[i, j] = exp_t_hot

        solver.initialize_domain(exp_w,exp_h,exp_dx,exp_dy)
        solver.initialize_physical_parameters(exp_d,exp_t_cold,exp_t_hot)
>       assert (solver.set_initial_condition() == exp_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x000001F9807760D0>()
E        +    where <built-in method all of numpy.ndarray object at 0x000001F9807760D0> = array([[300.,... 300., 300.]]) == array([[300.,... 300., 700.]])
E             Use -v to get more diff.all

tests\integration\test_diffusion2d.py:56: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------- 
dt = 0.8272058823529411
_________________________________________________________________________ TestDiffusion2D.test_set_initial_condition __________________________________________________________________________ 

self = <tests.unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_value = np.array([[300., 300., 300.],[300., 300., 700.]])

        self.solver.dx = 5
        self.solver.dy = 3
        self.solver.nx = 2
        self.solver.ny = 3
        self.solver.T_cold = 300
        self.solver.T_hot = 700

>       self.assertTrue((self.solver.set_initial_condition() == expected_value).all())
E       AssertionError: False is not true

tests\unit\test_diffusion2d_functions.py:51: AssertionError
_________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_value = np.array([[300., 300., 300.],[300., 300., 700.]])

        solver = SolveDiffusion2D()
        solver.dx = 5
        solver.dy = 3
        solver.nx = 2
        solver.ny = 3
        solver.T_cold = 300
        solver.T_hot = 700

>       assert (solver.set_initial_condition() == expected_value).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x000001F980776310>()
E        +    where <built-in method all of numpy.ndarray object at 0x000001F980776310> = array([[300.,... 300., 300.]]) == array([[300.,... 300., 700.]])
E             Use -v to get more diff.all

tests\unit\test_diffusion2d_functions.py:94: AssertionError
=================================================================================== short test summary info =================================================================================== 
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: False is not true
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================================================================= 3 failed, 5 passed in 0.48s ================================================================================= 
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
