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

```bash
============================= test session starts ==============================
collecting ... collected 3 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain FAILED [ 33%]
test_diffusion2d_functions.py:11 (TestDiffusion2D.test_initialize_domain)
25 != 20

Expected :20
Actual   :25
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=4., dx=0.2, dy=0.2)
    
        self.assertEqual(self.solver.w, 5.)
        self.assertEqual(self.solver.h, 4.)
        self.assertEqual(self.solver.dx, 0.2)
        self.assertEqual(self.solver.dy, 0.2)
>       self.assertEqual(self.solver.nx, 25)

test_diffusion2d_functions.py:22: AssertionError
PASSED [ 66%]dt = 0.0012500000000000002
PASSED [100%]dt = 0.0006250000000000001



test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition 

=================== 1 failed, 2 passed, 8 warnings in 0.89s ====================

Process finished with exit code 1


```

### integration test

```bash
============================= test session starts ==============================
collecting ... collected 1 item

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain FAILED [100%]
test_diffusion2d_functions.py:11 (TestDiffusion2D.test_initialize_domain)
25 != 20

Expected :20
Actual   :25
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=5., h=4., dx=0.2, dy=0.2)
    
        self.assertEqual(self.solver.w, 5.)
        self.assertEqual(self.solver.h, 4.)
        self.assertEqual(self.solver.dx, 0.2)
        self.assertEqual(self.solver.dy, 0.2)
>       self.assertEqual(self.solver.nx, 25)

test_diffusion2d_functions.py:22: AssertionError




======================== 1 failed, 8 warnings in 0.68s =========================

Process finished with exit code 1
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
