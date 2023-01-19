# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
``` def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20., h=12., dx=0.5, dy=0.2)
        excepted_nx = 40
        excepted_ny = 60
    
>       assert solver.nx == excepted_nx, f'nx value should be {excepted_nx} but got {solver.nx}'
E       AssertionError: nx value should be 40 but got 24
E       assert 24 == 40
E        +  where 24 = <diffusion2d.SolveDiffusion2D object at 0x11aacc910>.nx

tests/unit/test_diffusion2d_functions.py:18: AssertionError
```

```
 def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.5
        solver.dy = 0.2
        solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
        calculated_dt = 0.0011
        expected_dt = pytest.approx(calculated_dt, abs=0.01)
>       assert expected_dt == solver.dt , 'Assertion error'
E       AssertionError: Assertion error
E       assert 0.0011 ± 1.0e-02 == 1.7500000000000002
E         comparison failed
E         Obtained: 1.7500000000000002
E         Expected: 0.0011 ± 1.0e-02

tests/unit/test_diffusion2d_functions.py:32: AssertionError
```

```

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 5
        solver.ny = 5
        solver.D = 3.0
        solver.dx = 0.25
        solver.dy = 0.1
        solver.T_cold = 200.0
        solver.T_hot = 500.0
        #  According to the algorithm if I pass these values to the function it should give me numpy array with all the values equal to 200
        excepted_u = np.ones((5, 5)) * 200.0
        calculated_u = solver.set_initial_condition()
        assert calculated_u.shape == excepted_u.shape, f'output shape should be {calculated_u.shape} but got {excepted_u.shape}'
>       assert np.array_equal(excepted_u,calculated_u), f'calculated u/initial condition should fe {excepted_u} but the function returned {calculated_u}'
E       AssertionError: calculated u/initial condition should fe [[200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]] but the function returned [[500. 500. 500. 500. 500.]
E          [500. 500. 500. 500. 500.]
E          [500. 500. 500. 500. 500.]
E          [500. 500. 500. 500. 500.]
E          [500. 500. 500. 500. 500.]]
E       assert False
E        +  where False = <function array_equal at 0x106245750>(array([[200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.]]), array([[500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.]]))
E        +    where <function array_equal at 0x106245750> = np.array_equal

tests/unit/test_diffusion2d_functions.py:50: AssertionError
```
### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
