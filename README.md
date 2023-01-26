# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
``` 
def test_initialize_domain():
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
        self.w = 20
        self.h = 12
        solver.nx = 5
        solver.ny = 5
        solver.D = 3.0
        solver.dx = 0.25
        solver.dy = 0.1
        solver.T_cold = 200.0
        solver.T_hot = 500.0
        #  According to the algorithm if I pass these values to the function it should give me numpy array with all the values equal to T_cold
        excepted_u = np.ones((5, 5)) * self.solver.T_cold
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
```
=========================================================================================================================== FAILURES ===========================================================================================================================
____________________________________________________________________________________________________________ TestDiffusion2D.test_initialize_domain ____________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=20., h=12., dx=0.5, dy=0.2)
        excepted_nx, excepted_ny = 40, 60
        # assert self.solver.nx == excepted_nx, f'nx value should be {excepted_nx} but got {self.solver.nx}'
        # assert self.solver.ny == excepted_ny, f'nx value should be {excepted_ny} but got {self.solver.ny}'
>       self.assertEqual(self.solver.nx, excepted_nx)
E       AssertionError: 80 != 40

tests/unit/test_diffusion2d_functions.py:22: AssertionError
=================================================================================================================== short test summary info ====================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 80 != 40
```

```
=========================================================================================================================== FAILURES ===========================================================================================================================
_____________________________________________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters ______________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
        calculated_dt = 0.00574
        # expected_dt = pytest.approx(calculated_dt, abs=0.01)
        # assert expected_dt == self.solver.dt , 'Assertion error'
>       self.assertAlmostEqual(self.solver.dt, calculated_dt, 4)
E       AssertionError: 0.002873563218390805 != 0.00574 within 4 places (0.0028664367816091953 difference)

tests/unit/test_diffusion2d_functions.py:33: AssertionError
--------------------------------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------------------------------
dt = 0.002873563218390805
=================================================================================================================== short test summary info ====================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.002873563218390805 != 0.00574 within 4 places (0.0028664367816091953 difference)
```
```
=========================================================================================================================== FAILURES ===========================================================================================================================
__________________________________________________________________________________________________________ TestDiffusion2D.test_set_initial_condition __________________________________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver = SolveDiffusion2D()
        self.solver.nx = 5
        self.solver.ny = 5
        self.solver.D = 3.0
        self.solver.dx = 0.25
        self.solver.dy = 0.1
        self.solver.T_cold = 200.0
        self.solver.T_hot = 500.0
        #  According to the algorithm if I pass these values to the function it should give me numpy array with all the values equal to 200
        excepted_u = np.ones((5, 5)) * 200.0
        calculated_u = self.solver.set_initial_condition()
        self.assertEqual(calculated_u.shape,excepted_u.shape)
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
E        +  where False = <function array_equal at 0x10161dab0>(array([[200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.]]), array([[500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.],\n       [500., 500., 500., 500., 500.]]))
E        +    where <function array_equal at 0x10161dab0> = np.array_equal

tests/unit/test_diffusion2d_functions.py:51: AssertionError
=================================================================================================================== short test summary info ====================================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: calculated u/initial condition should fe [[200. 200. 200. 200. 200.]
================================================================================================================= 1 failed, 4 passed in 0.31s ==================================================================================================================
```

### Integration test log
```
============================================================================================ FAILURES =============================================================================================
_______________________________________________________________________________ test_initialize_physical_parameters _______________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain( w=20., h=12., dx=0.5, dy=0.2)
        solver.initialize_physical_parameters(d=3., T_cold=200., T_hot=500.)
        expected_dt = 0.00574
>       assert expected_dt == approx(solver.dt, abs=1e-5)
E       assert 0.00574 == 0.017400000000000006 ± 1.0e-05
E         comparison failed
E         Obtained: 0.00574
E         Expected: 0.017400000000000006 ± 1.0e-05

tests/integration/test_diffusion2d.py:18: AssertionError
-------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------
dt = 0.017400000000000006
===================================================================================== short test summary info =====================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.00574 == 0.017400000000000006 ± 1.0e-05
======================================================================================== 1 failed in 0.27s ========================================================================================
```
```

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain( w=20., h=12., dx=0.5, dy=0.2)
        T_cold = 200.
        solver.initialize_physical_parameters(d=3., T_cold=T_cold, T_hot=700.)
        u = solver.set_initial_condition()
        excepted_u = np.ones((5, 5)) * T_cold
>       assert np.array_equal(excepted_u,u), f'calculated u/initial condition should fe {excepted_u} but the function returned {u}'
E       AssertionError: calculated u/initial condition should fe [[200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]
E          [200. 200. 200. 200. 200.]] but the function returned [[201. 201. 201. ... 201. 201. 201.]
E          [201. 201. 201. ... 201. 201. 201.]
E          [201. 201. 201. ... 201. 201. 201.]
E          ...
E          [201. 201. 201. ... 201. 201. 201.]
E          [201. 201. 201. ... 201. 201. 201.]
E          [201. 201. 201. ... 201. 201. 201.]]
E       assert False
E        +  where False = <function array_equal at 0x10598db40>(array([[200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.],\n       [200., 200., 200., 200., 200.]]), array([[201., 201., 201., ..., 201., 201., 201.],\n       [201., 201., 201., ..., 201., 201., 201.],\n       [201., 201....201., 201., 201.],\n       [201., 201., 201., ..., 201., 201., 201.],\n       [201., 201., 201., ..., 201., 201., 201.]]))
E        +    where <function array_equal at 0x10598db40> = np.array_equal

tests/integration/test_diffusion2d.py:31: AssertionError
-------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------
dt = 0.00574712643678161
===================================================================================== short test summary info =====================================================================================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError: calculated u/initial condition should fe [[200. 200. 200. 200. 200.]
======================================================================================== 1 failed in 0.28s ========================================================================================
```
## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
