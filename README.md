# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```code
(venv) nimo@pop-os:~/SSE/exercise8/testing-python-exercise-wt2223$ python3 -m pytest tests/unit/test_diffusion2d_functions.py
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/nimo/SSE/exercise8/testing-python-exercise-wt2223
plugins: xdist-3.1.0, allure-pytest-2.12.0, metadata-2.0.4, rerunfailures-11.0, anyio-3.6.2, json-report-1.5.0, Faker-16.6.0, order-1.0.1
collected 3 items                                                                                                                                                                                                 

tests/unit/test_diffusion2d_functions.py F..                                                                                                                                                                [100%]

==================================================================================================== FAILURES =====================================================================================================
_____________________________________________________________________________________________ test_initialize_domain ______________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        expected_nx = 1
        expected_ny = 1
        solver.initialize_domain( w=5., h=20., dx=5., dy=20.)
>       assert solver.nx == expected_nx and solver.ny == expected_ny
E       assert (4 == 1)
E        +  where 4 = <diffusion2d.SolveDiffusion2D object at 0x7f66d7620100>.nx

tests/unit/test_diffusion2d_functions.py:16: AssertionError
============================================================================================= short test summary info =============================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert (4 == 1)
=========================================================================================== 1 failed, 2 passed in 0.38s ===========================================================================================

```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
