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
=================================================== test session starts ===================================================
platform win32 -- Python 3.10.0, pytest-7.2.0, pluggy-1.0.0
rootdir: D:\GitHub\SSE\testing-python-exercise-wt2223
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                             [ 40%]
tests\unit\test_diffusion2d_functions.py FFF                                                                         [100%]

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
E           assert 169 == (94.67744282534127 // 0.5232638101357804)
E            +  where 169 = <diffusion2d.SolveDiffusion2D object at 0x0000023837033220>.nx

tests\unit\test_diffusion2d_functions.py:22: AssertionError
___________________________________________ test_initialize_physical_parameters ___________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        solver.w = 10.
        solver.h = 10.
        solver.dx = 0.1
        solver.dy = 0.1
        solver.nx = 100
        solver.ny = 100

        dx2, dy2 = solver.dx ** 2, solver.dy**2

        for i in range(1000):
            d = np.random.rand() * 100
            T_cold = np.random.rand() * 10000
            T_hot = np.random.rand() * 10000
            solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
            assert solver.D == d
            assert solver.T_cold == T_cold
            assert solver.T_hot == T_hot

            dt = pytest.approx(dx2 * dy2 / (2 * solver.D * (dx2 + dy2)), 0.01)
>           assert solver.dt == dt
E           assert 8.540838119817876e-05 == 0.00012811257...6814 ± 1.3e-06
E             comparison failed
E             Obtained: 8.540838119817876e-05
E             Expected: 0.00012811257179726814 ± 1.3e-06

tests\unit\test_diffusion2d_functions.py:51: AssertionError
-------------------------------------------------- Captured stdout call ---------------------------------------------------
dt = 8.540838119817876e-05
_______________________________________________ test_set_initial_condition ________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        solver.w = 10.
        solver.h = 10.
        solver.dx = 0.1
        solver.dy = 0.1
        solver.nx = 100
        solver.ny = 100

        solver.D = 4.
        solver.T_cold = 300.
        solver.T_hot = 700.
        solver.dt = 0.000625

        u = solver.set_initial_condition()
        assert u.shape == (100, 100)
        assert u.min() == solver.T_cold
>       assert u.max() == solver.T_hot
E       assert 1400.0 == 700.0
E        +  where 1400.0 = <built-in method max of numpy.ndarray object at 0x000002383707EE50>()
E        +    where <built-in method max of numpy.ndarray object at 0x000002383707EE50> = array([[300., 300., 300., ..., 300., 300., 300.],\n       [300., 300., 300., ..., 300., 300., 300.],\n       [300., 300....300., 300., 300.],\n       [300., 300., 300., ..., 300., 300., 300.],\n       [300., 300., 300., ..., 300., 300., 300.]]).max
E        +  and   700.0 = <diffusion2d.SolveDiffusion2D object at 0x00000238370984C0>.T_hot

tests\unit\test_diffusion2d_functions.py:75: AssertionError
================================================= short test summary info =================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 169 == (94.67744282534127 // 0.5232638101357804)
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 8.540838119817876e-05 == 0.00012811257...6814 ± 1.3e-06
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 1400.0 == 700.0
=============================================== 3 failed, 2 passed in 1.36s ===============================================
```

### unittest log

```
Launching unittests with arguments python -m unittest D:/GitHub/SSE/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py in D:\GitHub\SSE\testing-python-exercise-wt2223\tests\unit



111.0 != 37

Expected :37
Actual   :111.0
<Click to see difference>

Traceback (most recent call last):
  File "D:\Programme & Funktionen\PyCharm Community Edition 2019.2.2\helpers\pycharm\teamcity\diff_tools.py", line 32, in _patched_equals
    old(self, first, second, msg)
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 839, in assertEqual
    assertion_func(first, second, msg=msg)
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 832, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 37 != 111.0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 59, in testPartExecutor
    yield
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 615, in run
    testMethod()
  File "D:\GitHub\SSE\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 28, in test_initialize_domain
    self.assertEqual(self.solver.nx, w // dx)

dt = 0.0002837885791219549
D:\GitHub\SSE\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py:56: DeprecationWarning: Please use assertAlmostEqual instead.
  self.assertAlmostEquals(self.solver.dt, dt, 2)
dt = 0.0001524399938569907
dt = 2.0613416973528867e-05
dt = 0.0002049174953392603
dt = 0.00014924574560637533
dt = 9.995065225381505e-05
dt = 0.0001798893416755572
dt = 0.00011597342969159412
dt = 0.00016356510992831505
dt = 0.0003962470475809662


Ran 3 tests in 0.030s

FAILED (failures=2)


700.0 != 490000.0

Expected :490000.0
Actual   :700.0
<Click to see difference>

Traceback (most recent call last):
  File "D:\Programme & Funktionen\PyCharm Community Edition 2019.2.2\helpers\pycharm\teamcity\diff_tools.py", line 32, in _patched_equals
    old(self, first, second, msg)
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 839, in assertEqual
    assertion_func(first, second, msg=msg)
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 832, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 490000.0 != 700.0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 59, in testPartExecutor
    yield
  File "D:\Programme & Funktionen\Python3\lib\unittest\case.py", line 615, in run
    testMethod()
  File "D:\GitHub\SSE\testing-python-exercise-wt2223\tests\unit\test_diffusion2d_functions.py", line 77, in test_set_initial_condition
    self.assertEqual(u.max(), self.solver.T_hot)


Assertion failed

Assertion failed

Process finished with exit code 1

Assertion failed

Assertion failed

Assertion failed

Assertion failed

```

### Integration Test Log

```
============================= test session starts =============================
platform win32 -- Python 3.7.3, pytest-7.2.1, pluggy-1.0.0 -- D:\Programme & Funktionen\Python3\python.exe
cachedir: .pytest_cache
rootdir: D:\GitHub\SSE\testing-python-exercise-wt2223\tests\integration
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters FAILED          [ 50%]dt = 0.0036764705882352945

test_diffusion2d.py:9 (test_initialize_physical_parameters)
0.0036764705882352945 != 0.00551 ± 5.5e-06

Expected :0.00551 ± 5.5e-06
Actual   :0.0036764705882352945
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=54846., h=546., dx=0.3, dy=0.5)
        solver.initialize_physical_parameters(d=6., T_cold=400., T_hot=420.)
    
        expected = pytest.approx(0.00551, 0.001)
>       assert solver.dt == expected
E       assert 0.0036764705882352945 == 0.00551 ± 5.5e-06

test_diffusion2d.py:19: AssertionError

test_diffusion2d.py::test_set_initial_condition FAILED                   [100%]dt = 0.0004166666666666668

test_diffusion2d.py:21 (test_set_initial_condition)
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
E        +  where False = <function array_equal at 0x0000018F651109D8>(array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]), array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]))
E        +    where <function array_equal at 0x0000018F651109D8> = np.array_equal

test_diffusion2d.py:32: AssertionError


================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters _____________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=54846., h=546., dx=0.3, dy=0.5)
        solver.initialize_physical_parameters(d=6., T_cold=400., T_hot=420.)
    
        expected = pytest.approx(0.00551, 0.001)
>       assert solver.dt == expected
E       assert 0.0036764705882352945 == 0.00551 ± 5.5e-06

test_diffusion2d.py:19: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.0036764705882352945
_________________________ test_set_initial_condition __________________________

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
E        +  where False = <function array_equal at 0x0000018F651109D8>(array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]), array([[1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       ...,\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.],\n       [1., 1., 1., ..., 1., 1., 1.]]))
E        +    where <function array_equal at 0x0000018F651109D8> = np.array_equal

test_diffusion2d.py:32: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.0004166666666666668
=========================== short test summary info ===========================
FAILED test_diffusion2d.py::test_initialize_physical_parameters - assert 0.00...
FAILED test_diffusion2d.py::test_set_initial_condition - assert False
============================== 2 failed in 1.49s ==============================

Process finished with exit code 0

Assertion failed

Assertion failed

Assertion failed

Assertion failed

```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
