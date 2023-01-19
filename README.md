# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
==================================== test session starts =====================================
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/jo/Uni/SSE-Labs/07-testing/testing-python-exercise-wt2223, configfile: pytest.ini
collected 5 items                                                                            

tests/integration/test_diffusion2d.py ..                                               [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                           [100%]

========================================== FAILURES ==========================================
___________________________________ test_initialize_domain ___________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20., h=15., dx=0.1, dy=0.2)
    
>       assert solver.nx == 200
E       assert 150 == 200
E        +  where 150 = <diffusion2d.SolveDiffusion2D object at 0x7fab75fcb040>.nx

tests/unit/test_diffusion2d_functions.py:18: AssertionError
____________________________ test_initialize_physical_parameters _____________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.2
        solver.dy = 0.1
        solver.initialize_physical_parameters(d=5., T_cold=400.0, T_hot=600.0)
    
>       assert solver.dt == approx(0.0008)
E       assert 0.06000000000000001 == 0.0008 ± 8.0e-10
E         comparison failed
E         Obtained: 0.06000000000000001
E         Expected: 0.0008 ± 8.0e-10

tests/unit/test_diffusion2d_functions.py:31: AssertionError
------------------------------------ Captured stdout call ------------------------------------
dt = 0.06000000000000001
_________________________________ test_set_initial_condition _________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.T_cold = 400.0
        solver.T_hot = 600.0
    
        # this results in a 6x5 grid with the lower-most cell containing the center
        # of the circle
        solver.nx = 6
        solver.ny = 5
        solver.dx = 1.25
        solver.dy = 1.5
    
        expected = 400.0 * np.ones((6, 5))
        for i in range(3, 6):
            for j in range(3, 5):
                expected[i][j] = 600.0
    
        result = solver.set_initial_condition()
    
>       assert np.isclose(result, expected).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7fab75e18330>()
E        +    where <built-in method all of numpy.ndarray object at 0x7fab75e18330> = array([[ True,  True,  True,  True,  True],\n       [ True,  True,  True,  True,  True],\n       [ True,  True,  True,  ...,  True,  True, False, False],\n       [ True,  True,  True, False, False],\n       [ True,  True,  True, False, False]]).all
E        +      where array([[ True,  True,  True,  True,  True],\n       [ True,  True,  True,  True,  True],\n       [ True,  True,  True,  ...,  True,  True, False, False],\n       [ True,  True,  True, False, False],\n       [ True,  True,  True, False, False]]) = <function isclose at 0x7fab827604c0>(array([[400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.]]), array([[400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 400., 400.],\n       [400., 400., 400., 600., 600.],\n       [400., 400., 400., 600., 600.],\n       [400., 400., 400., 600., 600.]]))
E        +        where <function isclose at 0x7fab827604c0> = np.isclose

tests/unit/test_diffusion2d_functions.py:57: AssertionError
================================== short test summary info ===================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 150 == 200
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.06000000000000001 == 0.0008 ± 8.0e-10
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================ 3 failed, 2 passed in 0.55s =================================
```


### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
