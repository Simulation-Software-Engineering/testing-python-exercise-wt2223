# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### Break test_initial_domain

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

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
