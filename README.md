# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
```bash 
_________________________________________________________________________________________________ test_initialize_domain _________________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
    
        w=40.
        h=20.
        dx=0.1
        dy=0.2
    
        expected_nx = 400
        expected_ny = 100
    
        solver = SolveDiffusion2D()
    
        solver.initialize_domain(w,h,dx,dy)
    
>       assert solver.nx == expected_nx and solver.ny == expected_ny
E       assert (200 == 400)
E        +  where 200 = <diffusion2d.SolveDiffusion2D object at 0x1188a7b50>.nx

tests/unit/test_diffusion2d_functions.py:26: AssertionError
================================================================================================ short test summary info =================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert (200 == 400)
============================================================================================== 1 failed, 4 passed in 0.23s =========================================================================================
```

```bash
__________________________________________________________________________________________ test_initialize_physical_parameters ___________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        w=40.
        h=20.
        dx=0.1
        dy=0.2
    
        D = 3.
        T_cold = 200.
        T_hot = 600.
        expected_dt = 1/750
    
        solver = SolveDiffusion2D()
        solver.initialize_domain(w,h,dx,dy)
    
        solver.initialize_physical_parameters(D, T_cold, T_hot)
    
    
>       assert expected_dt == pytest.approx(solver.dt, abs=0.01)
E       assert 0.0013333333333333333 == 20.0 ± 1.0e-02
E         comparison failed
E         Obtained: 0.0013333333333333333
E         Expected: 20.0 ± 1.0e-02

tests/unit/test_diffusion2d_functions.py:48: AssertionError
-------------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------------
dt = 20.0
================================================================================================ short test summary info =================================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0013333333333333333 == 20.0 ± 1.0e-02
```

```Bash
    __________________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________________

        def test_set_initial_condition():
            """
            Checks function SolveDiffusion2D.get_initial_function
            """
        
            w=40.
            h=20.
            dx=10.
            dy=10.
        
            D = 3.
            T_cold = 200.
            T_hot = 600.
        
            solver = SolveDiffusion2D()
            solver.initialize_domain(w,h,dx,dy)
        
            solver.initialize_physical_parameters(D, T_cold, T_hot)
        
            expected_u = T_cold * np.ones((solver.nx, solver.ny))
        
        
            solver_u = solver.set_initial_condition()
        
        
    >       assert np.array_equal(  expected_u,solver_u)
    E       assert False
    E        +  where False = <function array_equal at 0x101abf520>(array([[200., 200.],\n       [200., 200.],\n       [200., 200.],\n       [200., 200.]]), array([[600., 600.],\n       [600., 600.],\n       [600., 600.],\n       [600., 600.]]))
    E        +    where <function array_equal at 0x101abf520> = np.array_equal

    tests/unit/test_diffusion2d_functions.py:75: AssertionError
    --------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
    dt = 8.333333333333334
    =========================================================================================== short test summary info ============================================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
    ========================================================================================= 1 failed, 4 passed in 0.29s ==========================================================================================
```

### unittest log
```bash
    Fdt = 0.0013333333333333337
    .dt = 8.333333333333334
    .
    ======================================================================
    FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
    Check function SolveDiffusion2D.initialize_domain
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/markashraf/Documents/Winter_22:23/Simulation_Engineering/Git_Repos/testing-python-exercise-wt2223/test_diffusion2d_functions.py", line 33, in test_initialize_domain
        self.assertEqual(self.solver.nx, expected_nx)
    AssertionError: 200 != 400

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    FAILED (failures=1)
```
```bash
    .dt = 0.03333333333333333
    Fdt = 0.08333333333333333
    .
    ======================================================================
    FAIL: test_initialize_physical_parameters (test_diffusion2d_functions.TestDiffusion2D)
    Checks function SolveDiffusion2D.initialize_domain
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/markashraf/Documents/Winter_22:23/Simulation_Engineering/Git_Repos/testing-python-exercise-wt2223/test_diffusion2d_functions.py", line 47, in test_initialize_physical_parameters
        self.assertAlmostEqual(expected_dt, self.solver.dt,  2)
    AssertionError: 0.0013333333333333333 != 0.03333333333333333 within 2 places (0.032 difference)

    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    FAILED (failures=1)
```

```bash
    .dt = 0.0013333333333333337
    .dt = 8.333333333333334
    F
    ======================================================================
    FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D)
    Checks function SolveDiffusion2D.get_initial_function
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/markashraf/Documents/Winter_22:23/Simulation_Engineering/Git_Repos/testing-python-exercise-wt2223/test_diffusion2d_functions.py", line 69, in test_set_initial_condition
        self.assertTrue((expected_u==solver_u).all())
    AssertionError: False is not true

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    FAILED (failures=1)
```

### integration log

```bash
    platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
    rootdir: /Users/markashraf/Documents/Winter_22:23/Simulation_Engineering/Git_Repos/testing-python-exercise-wt2223
    collected 5 items                                                                                                                                                                                              

    tests/integration/test_diffusion2d.py F.                                                                                                                                                                 [ 40%]
    tests/unit/test_diffusion2d_functions.py .F.                                                                                                                                                             [100%]

    =================================================================================================== FAILURES ===================================================================================================
    _____________________________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________________________

        def test_initialize_physical_parameters():
            """
            Checks function SolveDiffusion2D.initialize_domain
            """
            w=40.
            h=20.
            dx=0.1
            dy=0.2
            D = 3.
            T_cold = 200.
            T_hot = 600.
        
            expected_dt = 1/750
        
            solver = SolveDiffusion2D()
            solver.initialize_domain(w,h,dx,dy)
            solver.initialize_physical_parameters(D, T_cold, T_hot)
        
    >       assert expected_dt == pytest.approx(solver.dt, abs=0.01)
    E       assert 0.0013333333333333333 == 0.03333333333333333 ± 1.0e-02
    E         comparison failed
    E         Obtained: 0.0013333333333333333
    E         Expected: 0.03333333333333333 ± 1.0e-02

    tests/integration/test_diffusion2d.py:27: AssertionError
    --------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
    dt = 0.03333333333333333
    _____________________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters ______________________________________________________________________________

    self = <unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

        def test_initialize_physical_parameters(self):
            """
            Checks function SolveDiffusion2D.initialize_domain
            """
            expected_dt = 1/750
            self.solver.dx = self.dx
            self.solver.dy = self.dy
        
            self.solver.initialize_physical_parameters(self.D, self.T_cold, self.T_hot)
        
    >       self.assertAlmostEqual(expected_dt, self.solver.dt,  2)
    E       AssertionError: 0.0013333333333333333 != 0.03333333333333333 within 2 places (0.032 difference)

    tests/unit/test_diffusion2d_functions.py:47: AssertionError
    --------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
    dt = 0.03333333333333333
    =========================================================================================== short test summary info ============================================================================================
    FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0013333333333333333 == 0.03333333333333333 ± 1.0e-02
    FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.0013333333333333333 != 0.03333333333333333 within 2 places (0.032 difference)
    ========================================================================================= 2 failed, 3 passed in 0.26s ==========================================================================================
```

```bash
    platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
    rootdir: /Users/markashraf/Documents/Winter_22:23/Simulation_Engineering/Git_Repos/testing-python-exercise-wt2223
    collected 5 items                                                                                                                                                                                              

    tests/integration/test_diffusion2d.py .F                                                                                                                                                                 [ 40%]
    tests/unit/test_diffusion2d_functions.py ..F                                                                                                                                                             [100%]

    =================================================================================================== FAILURES ===================================================================================================
    __________________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________________

        def test_set_initial_condition():
            """
            Checks function SolveDiffusion2D.get_initial_function
            """
        
            w=40.
            h=20.
            dx=10.
            dy=10.
            D = 3.
            T_cold = 200.
            T_hot = 600.
        
            solver = SolveDiffusion2D()
            solver.initialize_domain(w,h,dx,dy)
            solver.initialize_physical_parameters(D, T_cold, T_hot)
            solver_u = solver.set_initial_condition()
        
            expected_u = T_cold * np.ones((solver.nx, solver.ny))
        
    >       assert np.array_equal(expected_u, solver_u)
    E       assert False
    E        +  where False = <function array_equal at 0x102273880>(array([[200., 200.],\n       [200., 200.],\n       [200., 200.],\n       [200., 200.]]), array([[600., 600.],\n       [600., 600.],\n       [600., 600.],\n       [600., 600.]]))
    E        +    where <function array_equal at 0x102273880> = np.array_equal

    tests/integration/test_diffusion2d.py:49: AssertionError
    --------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
    dt = 8.333333333333334
    __________________________________________________________________________________ TestDiffusion2D.test_set_initial_condition __________________________________________________________________________________

    self = <unit.test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

        def test_set_initial_condition(self):
            """
            Checks function SolveDiffusion2D.get_initial_function
            """
            self.dx=10.
            self.dy=10.
            self.solver.dx = self.dx
            self.solver.dy = self.dy
            self.solver.nx = self.nx
            self.solver.ny = self.ny
            self.solver.T_cold = self.T_cold
        
            expected_u = self.T_cold * np.ones((self.solver.nx, self.solver.ny))
        
            solver_u = self.solver.set_initial_condition()
        
    >       self.assertTrue((expected_u==solver_u).all())
    E       AssertionError: False is not true

    tests/unit/test_diffusion2d_functions.py:65: AssertionError
    =========================================================================================== short test summary info ============================================================================================
    FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
    FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: False is not true
    ========================================================================================= 2 failed, 3 passed in 0.25s ==========================================================================================
```
## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
