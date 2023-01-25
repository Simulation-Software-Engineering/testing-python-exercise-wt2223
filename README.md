# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
============================= test session starts =============================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\gally\Documents\sse_course\testing-python-exercise-wt2223
collected 5 items

tests\integration\test_diffusion2d.py ..                                 [ 40%]
tests\unit\test_diffusion2d_functions.py FFF                             [100%]

================================== FAILURES ===================================
___________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        w  = 10.
        x  = 20.
        dx = 0.1
        dy = 0.1

        testobject = SolveDiffusion2D()

        expected_val_nx = 100
        expected_val_ny = 200

        testobject.initialize_domain(w,x,dx,dy)

>       assert testobject.nx == expected_val_nx
E       assert 200 == 100
E        +  where 200 = <diffusion2d.SolveDiffusion2D object at 0x00000215E26F4CD0>.nx

tests\unit\test_diffusion2d_functions.py:27: AssertionError
_____________________ test_initialize_physical_parameters _____________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        w  = 10.
        x  = 10.
        dx = 0.1
        dy = 0.1
        d = 4.
        T_cold = 300.
        T_hot = 700.

        testobject = SolveDiffusion2D()

        expected_value = 0.00062


        testobject.initialize_domain(w,x,dx,dy)
        testobject.initialize_physical_parameters(d, T_cold, T_hot)

>       assert testobject.dt == pytest.approx(expected_value, abs = 1e-5)
E       assert 0.0625 == 0.00062 ▒ 1.0e-05
E         comparison failed
E         Obtained: 0.0625
E         Expected: 0.00062 ▒ 1.0e-05

tests\unit\test_diffusion2d_functions.py:53: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.0625
_________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Fixture
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        w  = 10.
        x  = 10.
        dx = 0.1
        dy = 0.1
        d = 4.
        T_cold = 300.
        T_hot = 700.

        testobject = SolveDiffusion2D()

        testobject.initialize_domain(w,x,dx,dy)
        testobject.initialize_physical_parameters(d, T_cold, T_hot)

        u_test = testobject.T_cold * numpy.ones((testobject.nx, testobject.ny))
        for i in range(testobject.nx):
            for j in range(testobject.ny):
                p2 = (i * testobject.dx - cx) ** 2 + (j * testobject.dy - cy) ** 2
                if p2 < r2:
                    u_test[i, j] = testobject.T_hot

        u_func = testobject.set_initial_condition()

>       assert numpy.all(u_func == u_test)
E       assert False
E        +  where False = <function all at 0x00000215DFE08220>(array([[700.,... 700., 700.]]) == array([[300.,... 300., 300.]])
E        +    where <function all at 0x00000215DFE08220> = numpy.all
E           Use -v to get more diff)

tests\unit\test_diffusion2d_functions.py:86: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.0625
=========================== short test summary info ===========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
========================= 3 failed, 2 passed in 0.49s =========================


### unittest log

============================= test session starts =============================
collecting ... collected 3 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain FAILED [ 33%]
test_diffusion2d_functions.py:90 (TestDiffusion2D.test_initialize_domain)
100 != 200

Expected :200
Actual   :100
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
    
        self.testobject.initialize_domain(w = 10., h = 20., dx = 0.1, dy = 0.1)
    
        expected_val_nx = 100
        expected_val_ny = 200
    
>       self.assertEqual(self.testobject.nx, expected_val_nx)

test_diffusion2d_functions.py:98: AssertionError
FAILED [ 66%]dt = 0.0625

test_diffusion2d_functions.py:100 (TestDiffusion2D.test_initialize_physical_parameters)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
    
        testobject = SolveDiffusion2D()
    
        expected_value = 0.00062
    
        self.testobject.initialize_domain(w = 10., h = 10., dx = 0.1, dy = 0.1)
        self.testobject.initialize_physical_parameters(d = 4., T_cold = 300., T_hot = 700.)
    
>       self.assertAlmostEqual(self.testobject.dt, expected_value, 4)
E       AssertionError: 0.0625 != 0.00062 within 4 places (0.06188 difference)

test_diffusion2d_functions.py:110: AssertionError
FAILED [100%]dt = 0.0625

test_diffusion2d_functions.py:111 (TestDiffusion2D.test_set_initial_condition)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
    
        self.testobject.initialize_domain(w=0.5, h=0.5, dx=0.1, dy=0.1)
        self.testobject.initialize_physical_parameters(d = 4., T_cold = 300., T_hot = 700.)
        u_current = self.testobject.set_initial_condition()
        u_expected = numpy.array([[300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.], [300., 300., 300., 300., 300.]])
    
>       self.assertTrue(numpy.allclose(u_expected, u_current))
E       AssertionError: False is not true

test_diffusion2d_functions.py:119: AssertionError





test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition 

============================== 3 failed in 0.26s ==============================

### integration test log

 ============================= test session starts =============================
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters FAILED          [ 50%]dt = 0.022727272727272728

test_diffusion2d.py:8 (test_initialize_physical_parameters)
0.022727272727272728 != 0.00043 ± 1.0e-05

Expected :0.00043 ± 1.0e-05
Actual   :0.022727272727272728
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w = 1.0
        h = 20.0
        dx = 0.1
        dy = 0.5
    
        d = 11.
        T_cold = 3.
        T_hot = 1700.
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
>       assert solver.dt == pytest.approx(0.00043, abs = 1e-5)
E       assert 0.022727272727272728 == 0.00043 ± 1.0e-05
E         comparison failed
E         Obtained: 0.022727272727272728
E         Expected: 0.00043 ± 1.0e-05

test_diffusion2d.py:27: AssertionError

test_diffusion2d.py::test_set_initial_condition FAILED                   [100%]dt = 0.022727272727272728

test_diffusion2d.py:28 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        w = 1.0
        h = 20.0
        dx = 0.1
        dy = 0.5
    
        nx = 10
        ny = 40
    
        d = 11.
        T_cold = 3.
        T_hot = 1700.
    
        u_expected = T_cold * numpy.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    u_expected[i, j] = T_hot
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        u_current = solver.set_initial_condition()
    
>       assert numpy.allclose(u_current, u_expected)

test_diffusion2d.py:60: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
<__array_function__ internals>:200: in allclose
    ???
C:\Users\gally\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\core\numeric.py:2270: in allclose
    res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
<__array_function__ internals>:200: in isclose
    ???
C:\Users\gally\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\core\numeric.py:2380: in isclose
    return within_tol(x, y, atol, rtol)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

x = array([[1700., 1700., 1700., ..., 1700., 1700., 1700.],
       [1700., 1700., 1700., ..., 1700., 1700., 1700.],
      ...700.],
       [1700., 1700., 1700., ..., 1700., 1700., 1700.],
       [1700., 1700., 1700., ..., 1700., 1700., 1700.]])
y = array([[3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3.,
        3., 3., 3., 3., 3., 3., 3., 3., 3., 3...., 3.,
        3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3.,
        3., 3., 3., 3., 3., 3., 3., 3.]])
atol = 1e-08, rtol = 1e-05

    def within_tol(x, y, atol, rtol):
        with errstate(invalid='ignore'), _no_nep50_warning():
>           return less_equal(abs(x-y), atol + rtol * abs(y))
E           ValueError: operands could not be broadcast together with shapes (200,40) (10,40)

C:\Users\gally\AppData\Local\Programs\Python\Python311\Lib\site-packages\numpy\core\numeric.py:2361: ValueError


============================== 2 failed in 0.28s ==============================

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
