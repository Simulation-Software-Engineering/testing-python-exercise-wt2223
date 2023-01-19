# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
================================================= test session starts ==================================================
platform linux -- Python 3.11.0, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/marcel/Projects/testing-python-exercise-wt2223
collected 5 items

tests/integration/test_diffusion2d.py ..                                                                         [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                     [100%]

======================================================= FAILURES =======================================================
________________________________________________ test_initialize_domain ________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20., h=5., dx=0.5, dy=0.5)

        assert solver.w == 20
        assert solver.h == 5
        assert solver.dx == 0.5
        assert solver.dy == 0.5
>       assert solver.nx == 40
E       assert 10 == 40
E        +  where 10 = <diffusion2d.SolveDiffusion2D object at 0x7f18b173d650>.nx

tests/unit/test_diffusion2d_functions.py:20: AssertionError
_________________________________________ test_initialize_physical_parameters __________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain()
        solver.initialize_physical_parameters(d=5., T_cold=200., T_hot=600.)

        assert solver.D == 5
>       assert solver.T_cold == 200
E       assert 600.0 == 200
E        +  where 600.0 = <diffusion2d.SolveDiffusion2D object at 0x7f18b184ec10>.T_cold

tests/unit/test_diffusion2d_functions.py:33: AssertionError
------------------------------------------------- Captured stdout call -------------------------------------------------
dt = 0.0005000000000000001
______________________________________________ test_set_initial_condition ______________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain()
        solver.initialize_physical_parameters()
        u = solver.set_initial_condition()

>       assert u[0,0] == 300
E       assert 700.0 == 300

tests/unit/test_diffusion2d_functions.py:47: AssertionError
------------------------------------------------- Captured stdout call -------------------------------------------------
dt = 0.0006250000000000001
=============================================== short test summary info ================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 10 == 40
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 600.0 == 200
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 700.0 == 300
============================================= 3 failed, 2 passed in 0.42s ==============================================
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
