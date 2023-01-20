# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
============================= test session starts ==============================
collecting ... collected 3 items

test_diffusion2d_functions.py::test_initialize_domain FAILED             [ 33%]
test_diffusion2d_functions.py:8 (test_initialize_domain)
0 != 1

Expected :1
Actual   :0
<Click to see difference>

def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # arrange
        solver = SolveDiffusion2D()
        w = 1.0
        h = 2.0
        dx = 1.0
        dy = 1.0
    
        # act
        solver.initialize_domain(w, h, dx, dy)
    
        # assert
>       assert solver.nx == 1
E       assert 0 == 1
E        +  where 0 = <diffusion2d.SolveDiffusion2D object at 0x116a646d0>.nx

test_diffusion2d_functions.py:24: AssertionError

test_diffusion2d_functions.py::test_initialize_physical_parameters FAILED [ 66%]dt = -6.0

test_diffusion2d_functions.py:27 (test_initialize_physical_parameters)
0.4 != -6.0

Expected :-6.0
Actual   :0.4
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # arrange
        solver = SolveDiffusion2D()
        solver.dx = 1.0
        solver.dy = 2.0
    
        d = 1.
        T_cold = 100
        T_hot = 500
    
        # act
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        # assert
        dx2, dy2 = 1.0, 4.0
        expected_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))
    
>       assert expected_dt == solver.dt
E       assert 0.4 == -6.0
E        +  where -6.0 = <diffusion2d.SolveDiffusion2D object at 0x116a67d00>.dt

test_diffusion2d_functions.py:48: AssertionError

test_diffusion2d_functions.py::test_set_initial_condition FAILED         [100%]
test_diffusion2d_functions.py:50 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Arrange
        solver = SolveDiffusion2D()
        solver.T_cold = 100
        solver.T_hot = 500
        solver.nx = 1
        solver.ny = 4
        solver.dx = 1.0
        solver.dy = 2.0
    
        # Act
        actual_result = solver.set_initial_condition()
    
        # Assert
        # based on my extensive physics knowledge, I have computed that with the given input, the result must be this
        expected_result = [[100.0, 100.0, 100.0, 100.0]]
    
        ar = np.array(expected_result)
        br = np.array(actual_result)
        # numpy already has a suitable function to compare multi-dimensional arrays
>       assert np.array_equal(ar, br)
E       assert False
E        +  where False = <function array_equal at 0x101c85240>(array([[100., 100., 100., 100.]]), array([[1500.,  100.,  100.,  100.]]))
E        +    where <function array_equal at 0x101c85240> = np.array_equal

test_diffusion2d_functions.py:74: AssertionError


============================== 3 failed in 0.33s ===============================
```

### unittest log

```
Testing started at 17:03 ...
Launching unittests with arguments python -m unittest /Users/felixneubauer/Documents/Business/Uni_Stuttgart/Semester_2/SimulationSWE/other_tasks/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py in /Users/felixneubauer/Documents/Business/Uni_Stuttgart/Semester_2/SimulationSWE/other_tasks/testing-python-exercise-wt2223/tests/unit



Ran 3 tests in 0.003s

FAILED (failures=3)


1 != 0

Expected :0
Actual   :1
<Click to see difference>

Traceback (most recent call last):
  File "/Users/felixneubauer/Documents/Business/Uni_Stuttgart/Semester_2/SimulationSWE/other_tasks/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 55, in test_initialize_domain
    self.assertEqual(solver.nx, 1)
AssertionError: 0 != 1





dt = 4


4 != 0.4

Expected :0.4
Actual   :4
<Click to see difference>

Traceback (most recent call last):
  File "/Users/felixneubauer/Documents/Business/Uni_Stuttgart/Semester_2/SimulationSWE/other_tasks/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 38, in test_initialize_physical_parameters
    self.assertEqual(expected_dt, solver.dt)
AssertionError: 0.4 != 4






Failure
Traceback (most recent call last):
  File "/Users/felixneubauer/Documents/Business/Uni_Stuttgart/Semester_2/SimulationSWE/other_tasks/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py", line 81, in test_set_initial_condition
    self.assertTrue(np.array_equal(ar, br))
AssertionError: False is not true






Process finished with exit code 1
```

### integration test log

```
============================= test session starts ==============================
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters FAILED          [ 50%]dt = 0.6

test_diffusion2d.py:8 (test_initialize_physical_parameters)
0.4 != 0.6

Expected :0.6
Actual   :0.4
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        d = 1.0
        dx = 1.0
        dy = 2.0
        w = 1.0
        h = 2.0
        T_cold = 100
        T_hot = 500
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        expected_value = 0.4
>       assert expected_value == solver.dt
E       assert 0.4 == 0.6
E        +  where 0.6 = <diffusion2d.SolveDiffusion2D object at 0x12756c6a0>.dt

test_diffusion2d.py:27: AssertionError




test_diffusion2d.py::test_set_initial_condition FAILED                   [100%]dt = 0.6

test_diffusion2d.py:28 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        d = 1.0
        dx = 1.0
        dy = 2.0
        w = 1.0
        h = 4.0
        T_cold = 100
        T_hot = 500
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        actual_result = solver.set_initial_condition()
    
        expected_result = [[100.0, 100.0]]
    
        # numpy already has a suitable function to compare multi-dimensional arrays
>       assert np.array_equal(expected_result, actual_result)
E       AssertionError: assert False
E        +  where False = <function array_equal at 0x1049f9480>([[100.0, 100.0]], 'your mama')
E        +    where <function array_equal at 0x1049f9480> = np.array_equal

test_diffusion2d.py:51: AssertionError





============================== 2 failed in 0.37s ===============================

Process finished with exit code 1
```


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
