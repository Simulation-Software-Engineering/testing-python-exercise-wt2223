# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```
=================================================================== test session starts ===================================================================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/bluzuk/Stuff/testing-python-exercise-wt2223
plugins: anyio-3.6.2
collected 5 items

tests/integration/test_diffusion2d.py ..                                                                                                            [ 40%]
tests/unit/test_diffusion2d_functions.py F..                                                                                                        [100%]

======================================================================== FAILURES =========================================================================
_________________________________________________________________ test_initialize_domain __________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=20., dx=0.5, dy=0.5)

        expected_nx = 10
        expected_ny = 40

        actual_nx = solver.nx
        actual_ny = solver.ny

>       assert (actual_nx == expected_nx)
E       assert 40 == 10

tests/unit/test_diffusion2d_functions.py:21: AssertionError
================================================================= short test summary info =================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40 == 10
=============================================================== 1 failed, 4 passed in 0.27s ===============================================================
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
