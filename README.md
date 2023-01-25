# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
Launching pytest with arguments /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 3 items

test_diffusion2d_functions.py::test_initialize_domain FAILED             [ 33%]
test_diffusion2d_functions.py:9 (test_initialize_domain)
100 != 250

Expected :250
Actual   :100
<Click to see difference>

def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
    
        assert solver.ny == 200
>       assert solver.nx == 250
E       assert 100 == 250
E        +  where 100 = <diffusion2d.SolveDiffusion2D object at 0x7f133a8341f0>.nx

test_diffusion2d_functions.py:18: AssertionError

test_diffusion2d_functions.py::test_initialize_physical_parameters FAILED [ 66%]dt = 5e-06

test_diffusion2d_functions.py:19 (test_initialize_physical_parameters)
5e-06 != 5.714e-06 ± 1.0e-07

Expected :5.714e-06 ± 1.0e-07
Actual   :5e-06
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
        solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
    
        expected_result = pytest.approx(0.000005714, abs=1e-7)
    
>       assert solver.dt == expected_result
E       assert 5e-06 == 5.714e-06 ± 1.0e-07
E         comparison failed
E         Obtained: 5e-06
E         Expected: 5.714e-06 ± 1.0e-07

test_diffusion2d_functions.py:30: AssertionError

test_diffusion2d_functions.py::test_set_initial_condition FAILED         [100%]dt = 0.05

test_diffusion2d_functions.py:32 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=6., h=2., dx=2., dy=1.)
        solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
    
        u_expected = np.array([[300., 300.], [300., 300.], [300., 300.]])
>       u_actual = solver.set_initial_condition()

test_diffusion2d_functions.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x7f133a82c1f0>

    def set_initial_condition(self):
        u = self.T_cold * np.ones((self.nx, self.ny))
    
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 4
        for i in range(self.nx*3):
            for j in range(self.ny*3):
                p2 = (i * self.dx - cx) ** 2 + (j * self.dy - cy) ** 2
                if p2 < r2:
>                   u[i, j] = self.T_hot
E                   IndexError: index 1 is out of bounds for axis 0 with size 1

../../diffusion2d.py:78: IndexError


============================== 3 failed in 0.42s ===============================

Process finished with exit code 1
```

### unittest log
```
/home/aburabazam/PycharmProjects/SimSoftEng/SSE/venv/bin/python /snap/pycharm-community/312/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --target test_diffusion2d_functions.py::TestDiffusion2D 
Testing started at 09:00 ...
Launching pytest with arguments test_diffusion2d_functions.py::TestDiffusion2D --no-header --no-summary -q in /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 3 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain FAILED [ 33%]
test_diffusion2d_functions.py:19 (TestDiffusion2D.test_initialize_domain)
250 != 100

Expected :100
Actual   :250
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
    
        expected_ny = 200
        expected_nx = 250
    
        self.assertEqual(self.solver.ny, expected_ny)
>       self.assertEqual(self.solver.nx, expected_nx)

test_diffusion2d_functions.py:30: AssertionError
FAILED [ 66%]dt = 1.4285714285714286e-06

test_diffusion2d_functions.py:33 (TestDiffusion2D.test_initialize_physical_parameters)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
        self.solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
    
        expected_result = 0.000005714
    
>       self.assertAlmostEqual(self.solver.dt, expected_result, 7)
E       AssertionError: 1.4285714285714286e-06 != 5.714e-06 within 7 places (4.285428571428572e-06 difference)

test_diffusion2d_functions.py:43: AssertionError
FAILED [100%]dt = 0.014285714285714285

test_diffusion2d_functions.py:44 (TestDiffusion2D.test_set_initial_condition)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.initialize_domain(w=6., h=2., dx=2., dy=1.)
        self.solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
        u_actual = self.solver.set_initial_condition()
    
        u_expected = np.array([[300., 300.], [300., 300.], [300., 300.]])
    
>       self.assertTrue(np.allclose(u_expected, u_actual))
E       AssertionError: False is not true

test_diffusion2d_functions.py:55: AssertionError





test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition 

============================== 3 failed in 0.43s ===============================

Process finished with exit code 1

```

### integration test log

```
/home/aburabazam/PycharmProjects/SimSoftEng/SSE/venv/bin/python /snap/pycharm-community/312/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/integration/test_diffusion2d.py 
Testing started at 09:23 ...
Launching pytest with arguments /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/integration/test_diffusion2d.py --no-header --no-summary -q in /home/aburabazam/PycharmProjects/SimSoftEng/SSE/testing-python-exercise-wt2223/tests/integration

============================= test session starts ==============================
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters FAILED          [ 50%]dt = 1.4285714285714286e-06

test_diffusion2d.py:10 (test_initialize_physical_parameters)
1.4285714285714286e-06 != 5.714e-06 ± 1.0e-07

Expected :5.714e-06 ± 1.0e-07
Actual   :1.4285714285714286e-06
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=2., dx=0.02, dy=0.01)
        solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
    
        expected_result = approx(0.000005714, abs=1e-7)
    
>       assert solver.dt == expected_result
E       assert 1.4285714285714286e-06 == 5.714e-06 ± 1.0e-07
E         comparison failed
E         Obtained: 1.4285714285714286e-06
E         Expected: 5.714e-06 ± 1.0e-07

test_diffusion2d.py:21: AssertionError

test_diffusion2d.py::test_set_initial_condition FAILED                   [100%]dt = 0.014285714285714285

test_diffusion2d.py:23 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=6., h=2., dx=2., dy=1.)
        solver.initialize_physical_parameters(d=7., T_cold=300., T_hot=700.)
        u_actual = solver.set_initial_condition()
    
        u_expected = 300.0 * np.ones((3, 2))
    
>       assert np.isclose(u_actual, u_expected).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7ff3ad0706f0>()
E        +    where <built-in method all of numpy.ndarray object at 0x7ff3ad0706f0> = array([[False, False],\n       [False, False],\n       [False, False]]).all
E        +      where array([[False, False],\n       [False, False],\n       [False, False]]) = <function isclose at 0x7ff3c0da7b50>(array([[150., 150.],\n       [150., 150.],\n       [150., 150.]]), array([[300., 300.],\n       [300., 300.],\n       [300., 300.]]))
E        +        where <function isclose at 0x7ff3c0da7b50> = np.isclose

test_diffusion2d.py:35: AssertionError


============================== 2 failed in 0.47s ===============================

Process finished with exit code 1
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
