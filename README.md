# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```code

(test_venv) jay@s-8d3a3dd8 testing-python-exercise-wt2223 % python -m pytest tests/unit/test_diffusion2d_functions.py
===================================================== test session starts ======================================================
platform darwin -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/jay/Downloads/testing-python-exercise-wt2223
collected 3 items                                                                                                              

tests/unit/test_diffusion2d_functions.py F..                                                                             [100%]

=========================================================== FAILURES ===========================================================
____________________________________________________ test_initialize_domain ____________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        nx = 30
        ny = 50
        solver.initialize_domain(w = 15.0, h = 20.0, dx = 0.5, dy = 0.4)
>       assert solver.nx == nx
E       assert 40 == 30
E        +  where 40 = <diffusion2d.SolveDiffusion2D object at 0x111d9a650>.nx

tests/unit/test_diffusion2d_functions.py:16: AssertionError
=================================================== short test summary info ====================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40 == 30
================================================= 1 failed, 2 passed in 1.18s ==================================================
(test_venv) jay@s-8d3a3dd8 testing-python-exercise-wt2223 % 

```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
