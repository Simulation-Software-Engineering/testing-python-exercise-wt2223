# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### Break test_initial_domain

```
/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py
Testing started at 17:06 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 6 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40] PASSED [ 16%]
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45] FAILED [ 33%]
test_diffusion2d_functions.py:15 (test_initialize_domain[12.0-18.0-0.4-0.4-30-45])
45 != 30

Expected :30
Actual   :45
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f1d58c794d0>, w = 12.0
h = 18.0, dx = 0.4, dy = 0.4, nx = 30, ny = 45

    @pytest.mark.parametrize('w, h, dx, dy, nx, ny', [(20., 20., 0.2, 0.5, 100, 40),
                                                      (12., 18., 0.4, 0.4, 30, 45),
                                                      (108., 112., 0.3, 0.3, 360, 373)])
    def test_initialize_domain(solver, w, h, dx, dy, nx, ny):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == nx
E       assert 45 == 30
E        +  where 45 = <diffusion2d.SolveDiffusion2D object at 0x7f1d58c794d0>.nx

test_diffusion2d_functions.py:24: AssertionError





test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373] FAILED [ 50%]
test_diffusion2d_functions.py:15 (test_initialize_domain[108.0-112.0-0.3-0.3-360-373])
373 != 360

Expected :360
Actual   :373
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f1d58e52190>, w = 108.0
h = 112.0, dx = 0.3, dy = 0.3, nx = 360, ny = 373

    @pytest.mark.parametrize('w, h, dx, dy, nx, ny', [(20., 20., 0.2, 0.5, 100, 40),
                                                      (12., 18., 0.4, 0.4, 30, 45),
                                                      (108., 112., 0.3, 0.3, 360, 373)])
    def test_initialize_domain(solver, w, h, dx, dy, nx, ny):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == nx
E       assert 373 == 360
E        +  where 373 = <diffusion2d.SolveDiffusion2D object at 0x7f1d58e52190>.nx

test_diffusion2d_functions.py:24: AssertionError





test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666] PASSED [ 66%]dt = 0.0016666666666666672

test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857] PASSED [ 83%]dt = 0.0007142857142857145

test_diffusion2d_functions.py::test_set_initial_condition PASSED         [100%]

========================= 2 failed, 4 passed in 0.17s ==========================

Process finished with exit code 1
```

#### Break test_initialize_physical_parameters

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py
Testing started at 17:11 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 6 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40] PASSED [ 16%]
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45] PASSED [ 33%]
test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373] PASSED [ 50%]
test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666] FAILED [ 66%]dt = 0.008333333333333337

test_diffusion2d_functions.py:27 (test_initialize_physical_parameters[6.0-0.001666666])
0.008333333333333337 != 0.001666666 ± 1.7e-09

Expected :0.001666666 ± 1.7e-09
Actual   :0.008333333333333337
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f638eea0610>, d = 6.0
dt = 0.001666666

    @pytest.mark.parametrize('d, dt', [(6., 0.001666666), (14., 0.0007142857)])
    def test_initialize_physical_parameters(solver, d, dt):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Only parametrize d, since T_cold and T_hot has no influence on calculating dt.
        solver.dx = 0.2
        solver.dy = 0.2
        solver.initialize_physical_parameters(d, 350., 500.)
>       assert solver.dt == pytest.approx(dt, rel=0.000001)
E       assert 0.008333333333333337 == 0.001666666 ± 1.7e-09
E         comparison failed
E         Obtained: 0.008333333333333337
E         Expected: 0.001666666 ± 1.7e-09

test_diffusion2d_functions.py:37: AssertionError





test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857] FAILED [ 83%]dt = 0.0035714285714285726

test_diffusion2d_functions.py:27 (test_initialize_physical_parameters[14.0-0.0007142857])
0.0035714285714285726 != 0.0007142857 ± 7.1e-10

Expected :0.0007142857 ± 7.1e-10
Actual   :0.0035714285714285726
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f638efbd010>, d = 14.0
dt = 0.0007142857

    @pytest.mark.parametrize('d, dt', [(6., 0.001666666), (14., 0.0007142857)])
    def test_initialize_physical_parameters(solver, d, dt):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Only parametrize d, since T_cold and T_hot has no influence on calculating dt.
        solver.dx = 0.2
        solver.dy = 0.2
        solver.initialize_physical_parameters(d, 350., 500.)
>       assert solver.dt == pytest.approx(dt, rel=0.000001)
E       assert 0.0035714285714285726 == 0.0007142857 ± 7.1e-10
E         comparison failed
E         Obtained: 0.0035714285714285726
E         Expected: 0.0007142857 ± 7.1e-10

test_diffusion2d_functions.py:37: AssertionError





test_diffusion2d_functions.py::test_set_initial_condition PASSED         [100%]

========================= 2 failed, 4 passed in 0.16s ==========================

Process finished with exit code 1

#### Break test_set_initial_condition

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py
Testing started at 17:13 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 6 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40]
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45]
test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373]
test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666] PASSED [ 16%]PASSED [ 33%]PASSED [ 50%]
test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857]
test_diffusion2d_functions.py::test_set_initial_condition PASSED [ 66%]dt = 0.0016666666666666672
PASSED [ 83%]dt = 0.0007142857142857145
FAILED         [100%]
test_diffusion2d_functions.py:39 (test_set_initial_condition)
array([[800., 800., 800., ..., 400., 400., 400.],
       [800., 800., 800., ..., 400., 400., 400.],
       [800., 800., 800., ..., 400., 400., 400.],
       ...,
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.]]) != array([[400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       ...,
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.]])

<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f0b05d2e110>

    def test_set_initial_condition(solver):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver.dx = 0.7
        solver.dy = 0.7
        solver.nx = 200
        solver.ny = 200
        solver.T_cold = 400.
        solver.T_hot = 800.

        actual = solver.set_initial_condition()

        idx = np.array([5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9])
        idy = np. array([6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9])
        expected = np.ones((200, 200))
        expected[:, :] = 400.
        expected[idx, idy] = 800.

>       assert (actual == expected).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f0b05ea7810>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f0b05ea7810> = array([[800., 800., 800., ..., 400., 400., 400.],\n       [800., 800., 800., ..., 400., 400., 400.],\n       [800., 800., 800., ..., 400., 400., 400.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]]) == array([[400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]])
E             Full diff:
E             - array([[400., 400., 400., ..., 400., 400., 400.],
E             -        [400., 400., 400., ..., 400., 400., 400.],
E             -        [400., 400., 400., ..., 400., 400., 400.],
E             + array([[800., 800., 800., ..., 400., 400., 400.],
E             +        [800., 800., 800., ..., 400., 400., 400.],
E             +        [800., 800., 800., ..., 400., 400., 400.],
E                      ...,
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.]],
E               ).all

test_diffusion2d_functions.py:59: AssertionError


========================= 1 failed, 5 passed in 0.18s ==========================

Process finished with exit code 1

### unittest log

#### Break test_initial_domain

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py
Testing started at 13:06 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 12 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40]
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45] PASSED [  8%]FAILED [ 16%]
test_diffusion2d_functions.py:17 (test_initialize_domain[12.0-18.0-0.4-0.4-30-45])
45 != 30

Expected :30
Actual   :45
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f2841b18910>, w = 12.0
h = 18.0, dx = 0.4, dy = 0.4, nx = 30, ny = 45

    @pytest.mark.parametrize('w, h, dx, dy, nx, ny', [(20., 20., 0.2, 0.5, 100, 40),
                                                      (12., 18., 0.4, 0.4, 30, 45),
                                                      (108., 112., 0.3, 0.3, 360, 373)])
    def test_initialize_domain(solver, w, h, dx, dy, nx, ny):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == nx
E       assert 45 == 30
E        +  where 45 = <diffusion2d.SolveDiffusion2D object at 0x7f2841b18910>.nx

test_diffusion2d_functions.py:26: AssertionError
FAILED [ 25%]
test_diffusion2d_functions.py:17 (test_initialize_domain[108.0-112.0-0.3-0.3-360-373])
373 != 360

Expected :360
Actual   :373
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f2841ee4410>, w = 108.0
h = 112.0, dx = 0.3, dy = 0.3, nx = 360, ny = 373

    @pytest.mark.parametrize('w, h, dx, dy, nx, ny', [(20., 20., 0.2, 0.5, 100, 40),
                                                      (12., 18., 0.4, 0.4, 30, 45),
                                                      (108., 112., 0.3, 0.3, 360, 373)])
    def test_initialize_domain(solver, w, h, dx, dy, nx, ny):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == nx
E       assert 373 == 360
E        +  where 373 = <diffusion2d.SolveDiffusion2D object at 0x7f2841ee4410>.nx

test_diffusion2d_functions.py:26: AssertionError







test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373]
test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666]
test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857]
test_diffusion2d_functions.py::test_set_initial_condition PASSED [ 33%]dt = 0.0016666666666666672
PASSED [ 41%]dt = 0.0007142857142857145
PASSED         [ 50%]
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_0_first
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_1_second PASSED [ 58%]FAILED [ 66%]
test_diffusion2d_functions.py:67 (TestOperations.test_initialize_domain_1_second)
30 != 45

Expected :45
Actual   :30
<Click to see difference>

a = (<test_diffusion2d_functions.TestOperations testMethod=test_initialize_domain_1_second>,)

    @wraps(func)
    def standalone_func(*a):
>       return func(*(a + p.args), **p.kwargs)

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/lib/python3.11/site-packages/parameterized/parameterized.py:533: AssertionError
FAILED [ 75%]
test_diffusion2d_functions.py:67 (TestOperations.test_initialize_domain_2_third)
360 != 373

Expected :373
Actual   :360
<Click to see difference>

a = (<test_diffusion2d_functions.TestOperations testMethod=test_initialize_domain_2_third>,)

    @wraps(func)
    def standalone_func(*a):
>       return func(*(a + p.args), **p.kwargs)

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/lib/python3.11/site-packages/parameterized/parameterized.py:533: AssertionError
PASSED [ 83%]dt = 0.0016666666666666672
PASSED [ 91%]dt = 0.0007142857142857145
PASSED [100%]






test_diffusion2d_functions.py::TestOperations::test_initialize_domain_2_third
test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_0_first
test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_1_second
test_diffusion2d_functions.py::TestOperations::test_set_initial_condition

========================= 4 failed, 8 passed in 0.19s ==========================

Process finished with exit code 1

#### Break test_initialize_physical_parameters

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py 
Testing started at 13:07 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 12 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40] 
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45] 
test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373] 
test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666] PASSED [  8%]PASSED [ 16%]PASSED [ 25%]FAILED [ 33%]dt = 0.0006666666666666669

test_diffusion2d_functions.py:29 (test_initialize_physical_parameters[6.0-0.001666666])
0.0006666666666666669 != 0.001666666 ± 1.7e-09

Expected :0.001666666 ± 1.7e-09
Actual   :0.0006666666666666669
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f9cae7da810>, d = 6.0
dt = 0.001666666

    @pytest.mark.parametrize('d, dt', [(6., 0.001666666), (14., 0.0007142857)])
    def test_initialize_physical_parameters(solver, d, dt):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Only parametrize d, since T_cold and T_hot has no influence on calculating dt.
        solver.dx = 0.2
        solver.dy = 0.2
        solver.initialize_physical_parameters(d, 350., 500.)
>       assert solver.dt == pytest.approx(dt, rel=0.000001)
E       assert 0.0006666666666666669 == 0.001666666 ± 1.7e-09
E         comparison failed
E         Obtained: 0.0006666666666666669
E         Expected: 0.001666666 ± 1.7e-09

test_diffusion2d_functions.py:39: AssertionError
FAILED [ 41%]dt = 0.0002857142857142858

test_diffusion2d_functions.py:29 (test_initialize_physical_parameters[14.0-0.0007142857])
0.0002857142857142858 != 0.0007142857 ± 7.1e-10

Expected :0.0007142857 ± 7.1e-10
Actual   :0.0002857142857142858
<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f9cae9a8e10>, d = 14.0
dt = 0.0007142857

    @pytest.mark.parametrize('d, dt', [(6., 0.001666666), (14., 0.0007142857)])
    def test_initialize_physical_parameters(solver, d, dt):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Only parametrize d, since T_cold and T_hot has no influence on calculating dt.
        solver.dx = 0.2
        solver.dy = 0.2
        solver.initialize_physical_parameters(d, 350., 500.)
>       assert solver.dt == pytest.approx(dt, rel=0.000001)
E       assert 0.0002857142857142858 == 0.0007142857 ± 7.1e-10
E         comparison failed
E         Obtained: 0.0002857142857142858
E         Expected: 0.0007142857 ± 7.1e-10

test_diffusion2d_functions.py:39: AssertionError







test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857] 
test_diffusion2d_functions.py::test_set_initial_condition PASSED         [ 50%]
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_0_first 
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_1_second 
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_2_third 
test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_0_first PASSED [ 58%]PASSED [ 66%]PASSED [ 75%]FAILED [ 83%]dt = 0.0006666666666666669

test_diffusion2d_functions.py:75 (TestOperations.test_initialize_physical_parameters_0_first)
0.001666666 ± 1.7e-09 != 0.0006666666666666669

Expected :0.0006666666666666669
Actual   :0.001666666 ± 1.7e-09
<Click to see difference>

a = (<test_diffusion2d_functions.TestOperations testMethod=test_initialize_physical_parameters_0_first>,)

    @wraps(func)
    def standalone_func(*a):
>       return func(*(a + p.args), **p.kwargs)

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/lib/python3.11/site-packages/parameterized/parameterized.py:533: AssertionError
FAILED [ 91%]dt = 0.0002857142857142858

test_diffusion2d_functions.py:75 (TestOperations.test_initialize_physical_parameters_1_second)
0.0007142857 ± 7.1e-10 != 0.0002857142857142858

Expected :0.0002857142857142858
Actual   :0.0007142857 ± 7.1e-10
<Click to see difference>

a = (<test_diffusion2d_functions.TestOperations testMethod=test_initialize_physical_parameters_1_second>,)

    @wraps(func)
    def standalone_func(*a):
>       return func(*(a + p.args), **p.kwargs)

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/lib/python3.11/site-packages/parameterized/parameterized.py:533: AssertionError
PASSED [100%]






test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_1_second 
test_diffusion2d_functions.py::TestOperations::test_set_initial_condition 

========================= 4 failed, 8 passed in 0.19s ==========================

Process finished with exit code 1

#### Break test_set_initial_condition

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/bin/python /opt/pycharm-2022.2.3/plugins/python/helpers/pycharm/_jb_pytest_runner.py --path /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py 
Testing started at 13:08 ...
Launching pytest with arguments /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /home/chris/projects/AI_backmap/lecture_simulation_software_engineering/exercise/exercise7/testing-python-exercise-wt2223/tests/unit

============================= test session starts ==============================
collecting ... collected 12 items

test_diffusion2d_functions.py::test_initialize_domain[20.0-20.0-0.2-0.5-100-40] 
test_diffusion2d_functions.py::test_initialize_domain[12.0-18.0-0.4-0.4-30-45] 
test_diffusion2d_functions.py::test_initialize_domain[108.0-112.0-0.3-0.3-360-373] 
test_diffusion2d_functions.py::test_initialize_physical_parameters[6.0-0.001666666] PASSED [  8%]PASSED [ 16%]PASSED [ 25%]
test_diffusion2d_functions.py::test_initialize_physical_parameters[14.0-0.0007142857] 
test_diffusion2d_functions.py::test_set_initial_condition PASSED [ 33%]dt = 0.0016666666666666672
PASSED [ 41%]dt = 0.0007142857142857145
FAILED         [ 50%]
test_diffusion2d_functions.py:41 (test_set_initial_condition)
array([[800., 800., 800., ..., 400., 400., 400.],
       [800., 800., 800., ..., 400., 400., 400.],
       [800., 800., 800., ..., 400., 400., 400.],
       ...,
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.]]) != array([[400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       ...,
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.]])

<Click to see difference>

solver = <diffusion2d.SolveDiffusion2D object at 0x7f8681aa2890>

    def test_set_initial_condition(solver):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver.dx = 0.7
        solver.dy = 0.7
        solver.nx = 200
        solver.ny = 200
        solver.T_cold = 400.
        solver.T_hot = 800.
    
        actual = solver.set_initial_condition()
    
        idx = np.array([5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9])
        idy = np.array([6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9])
        expected = np.ones((200, 200))
        expected[:, :] = 400.
        expected[idx, idy] = 800.
    
>       assert (actual == expected).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f8681a6c330>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f8681a6c330> = array([[800., 800., 800., ..., 400., 400., 400.],\n       [800., 800., 800., ..., 400., 400., 400.],\n       [800., 800., 800., ..., 400., 400., 400.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]]) == array([[400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       ...,\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.],\n       [400., 400., 400., ..., 400., 400., 400.]])
E             Full diff:
E             - array([[400., 400., 400., ..., 400., 400., 400.],
E             -        [400., 400., 400., ..., 400., 400., 400.],
E             -        [400., 400., 400., ..., 400., 400., 400.],
E             + array([[800., 800., 800., ..., 400., 400., 400.],
E             +        [800., 800., 800., ..., 400., 400., 400.],
E             +        [800., 800., 800., ..., 400., 400., 400.],
E                      ...,
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.],
E                      [400., 400., 400., ..., 400., 400., 400.]],
E               ).all

test_diffusion2d_functions.py:61: AssertionError

test_diffusion2d_functions.py::TestOperations::test_initialize_domain_0_first 
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_1_second 
test_diffusion2d_functions.py::TestOperations::test_initialize_domain_2_third 
test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_0_first 
test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters_1_second 
test_diffusion2d_functions.py::TestOperations::test_set_initial_condition PASSED [ 58%]PASSED [ 66%]PASSED [ 75%]PASSED [ 83%]dt = 0.0016666666666666672
PASSED [ 91%]dt = 0.0007142857142857145
FAILED [100%]
test_diffusion2d_functions.py:84 (TestOperations.test_set_initial_condition)
self = <test_diffusion2d_functions.TestOperations testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        self.solver.dx = 0.7
        self.solver.dy = 0.7
        self.solver.nx = 200
        self.solver.ny = 200
        self.solver.T_cold = 400.
        self.solver.T_hot = 800.
    
        actual = self.solver.set_initial_condition()
    
        idx = np.array([5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9])
        idy = np.array([6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9])
        expected = np.ones((200, 200))
        expected[:, :] = 400.
        expected[idx, idy] = 800.
    
>       np.testing.assert_equal(actual, expected)

test_diffusion2d_functions.py:101: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (<built-in function eq>, array([[800., 800., 800., ..., 400., 400., 400.],
       [800., 800., 800., ..., 400., 400., ...00., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.],
       [400., 400., 400., ..., 400., 400., 400.]]))
kwds = {'err_msg': '', 'header': 'Arrays are not equal', 'strict': False, 'verbose': True}

    @wraps(func)
    def inner(*args, **kwds):
        with self._recreate_cm():
>           return func(*args, **kwds)
E           AssertionError: 
E           Arrays are not equal
E           
E           Mismatched elements: 96 / 40000 (0.24%)
E           Max absolute difference: 400.
E           Max relative difference: 1.
E            x: array([[800., 800., 800., ..., 400., 400., 400.],
E                  [800., 800., 800., ..., 400., 400., 400.],
E                  [800., 800., 800., ..., 400., 400., 400.],...
E            y: array([[400., 400., 400., ..., 400., 400., 400.],
E                  [400., 400., 400., ..., 400., 400., 400.],
E                  [400., 400., 400., ..., 400., 400., 400.],...

/home/chris/programs/mambaforge/envs/SSE_exercise_testing/lib/python3.11/contextlib.py:81: AssertionError






========================= 2 failed, 10 passed in 0.20s =========================

Process finished with exit code 1

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
