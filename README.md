# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```bash
==================================== FAILURES ====================================
_____________________________ test_initialize_domain _____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 3.0
        h = 9.0
        dx = 0.4
        dy = 0.3
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == 7
E       assert 22 == 7
E        +  where 22 = <diffusion2d.diffusion2d.SolveDiffusion2D object at 0x7fdcae2bc1c0>.nx

tests/unit/test_diffusion2d_functions.py:19: AssertionError
============================ short test summary info =============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 22 == 7
========================== 1 failed, 4 passed in 0.36s ===========================
❯ pytest
============================== test session starts ===============================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/matthias/Repos/diffusion2d
collected 5 items                                                                

tests/integration/test_diffusion2d.py ..                                   [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                               [100%]

==================================== FAILURES ====================================
_____________________________ test_initialize_domain _____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 3.0
        h = 9.0
        dx = 0.4
        dy = 0.3
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == 7
E       assert 22 == 7
E        +  where 22 = <diffusion2d.diffusion2d.SolveDiffusion2D object at 0x7f908eea83a0>.nx

tests/unit/test_diffusion2d_functions.py:19: AssertionError
______________________ test_initialize_physical_parameters _______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.4
        solver.dy = 0.3
        d = 10.
        T_cold = 200.
        T_hot = 400.
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        exprected_dt = pytest.approx(0.00288, abs=0.00001)
>       assert solver.dt == exprected_dt
E       assert 0.0014400000000000003 == 0.00288 ± 1.0e-05
E         comparison failed
E         Obtained: 0.0014400000000000003
E         Expected: 0.00288 ± 1.0e-05

tests/unit/test_diffusion2d_functions.py:36: AssertionError
------------------------------ Captured stdout call ------------------------------
dt = 0.0014400000000000003
___________________________ test_set_initial_condition ___________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 1
        solver.ny = 1
        solver.dx = 1
        solver.dy = 1
        solver.T_cold = 200.
        solver.T_hot = 400.
        u = solver.set_initial_condition()
>       assert u[0, 0] == 200.
E       assert 400.0 == 200.0

tests/unit/test_diffusion2d_functions.py:52: AssertionError
============================ short test summary info =============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 22 == 7
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0014400000000000003 == 0.00288 ± 1.0e-05
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 400.0 == 200.0
========================== 3 failed, 2 passed in 0.37s ==========================
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
