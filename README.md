# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
=================================================== test session starts ===================================================
platform win32 -- Python 3.10.0, pytest-7.2.0, pluggy-1.0.0
rootdir: D:\GitHub\SSE\testing-python-exercise-wt2223      
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                             [ 40%]
tests\unit\test_diffusion2d_functions.py F..                                                                         [100%]

======================================================== FAILURES ========================================================= 
_________________________________________________ test_initialize_domain __________________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        for i in range(1000):
            w = np.random.rand() * 100
            h = np.random.rand() * 100
            dx = np.random.rand()
            dy = np.random.rand()
            solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
>           assert solver.nx == w // dx
E           assert 445 == (39.55370833910049 // 0.17907525324321327)
E            +  where 445 = <diffusion2d.SolveDiffusion2D object at 0x000001990145F190>.nx

tests\unit\test_diffusion2d_functions.py:22: AssertionError
================================================= short test summary info ================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 445 == (39.55370833910049 // 0.17907525324321327)
=============================================== 1 failed, 4 passed in 1.21s =============================================== 
```


### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
