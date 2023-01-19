# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```bash

======================================================= FAILURES =======================================================
________________________________________________ test_initialize_domain ________________________________________________
    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=5., h=4., dx=0.2, dy=0.2)

        assert solver.w == 5.
        assert solver.h == 4.
        assert solver.dx == 0.2
        assert solver.dy == 0.2
>       assert solver.nx == 25
E       assert 20 == 25
E        +  where 20 = <diffusion2d.SolveDiffusion2D object at 0x7f96dbea6f80>.nx

tests/unit/test_diffusion2d_functions.py:19: AssertionError
=============================================== short test summary info ================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 20 == 25
============================================= 1 failed, 2 passed in 0.83s ==============================================
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
