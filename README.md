# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

collected 5 items

tests/integration/test_diffusion2d.py ..
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                                                                                   [100%]

================================================================================================================ FAILURES ================================================================================================================
_________________________________________________________________________________________________________ test_initialize_domain _________________________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(31., 35., 0.1, 0.3)
        expected_nx = pytest.approx(310., 0.1)
        expected_ny = pytest.approx(960., 0.1)

        assert solver.nx == expected_nx
>       assert solver.ny == expected_ny
E       assert 116 == 960.0 ± 9.6e+01
E         comparison failed
E         Obtained: 116
E         Expected: 960.0 ± 9.6e+01

test_diffusion2d_functions.py:20: AssertionError
__________________________________________________________________________________________________ test_initialize_physical_parameters ___________________________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
         Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(31., 50., 0.1, 0.3)
        solver.initialize_physical_parameters(2.)
        expected_res = 0.00225

>       assert solver.dt == expected_res
E       assert 0.0022500000000000003 == 0.00225
E        +  where 0.0022500000000000003 = <diffusion2d.SolveDiffusion2D object at 0x0000020570357D30>.dt

test_diffusion2d_functions.py:32: AssertionError
---------------------------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------------------------
dt = 0.0022500000000000003
_______________________________________________________________________________________________________ test_set_initial_condition _______________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(5., 7., 0.1, 0.3)
        solver.T_hot = 300
        solver.T_cold = 500
        u = solver.set_initial_condition()
        expected_u = np.ones((solver.nx, solver.ny))

>       assert (u == expected_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x000002057035CED0>()
E        +    where <built-in method all of numpy.ndarray object at 0x000002057035CED0> = array([[500.,... 300., 300.]]) == array([[1., 1... 1., 1., 1.]])
E             Use -v to get more diff.all

test_diffusion2d_functions.py:46: AssertionError
======================================================================================================== short test summary info =========================================================================================================
FAILED test_diffusion2d_functions.py::test_initialize_domain - assert 116 == 960.0 ± 9.6e+01
FAILED test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0022500000000000003 == 0.00225
FAILED test_diffusion2d_functions.py::test_set_initial_condition - assert False
=========================================================================================================== 3 failed in 0.26s ============================================================================================================


### unittest log

Fdt = 0.0022500000000000003
FF
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
File "E:\Desktop\Lecture\UniStuttgart\WS2022\05-Simulation Software Engineering\ex_pytest\testing-python-exercise-wt2223\test_diffusion2d_functions.py", line 21, in test_initialize_domain
self.assertEqual(self.solver.nx, 31)
AssertionError: 310 != 31

======================================================================
FAIL: test_initialize_physical_parameters (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
File "E:\Desktop\Lecture\UniStuttgart\WS2022\05-Simulation Software Engineering\ex_pytest\testing-python-exercise-wt2223\test_diffusion2d_functions.py", line 32, in test_initialize_physical_parameters
self.assertEqual(self.solver.dt, expected_res)
AssertionError: 0.0022500000000000003 != 0.00225

======================================================================
FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
File "E:\Desktop\Lecture\UniStuttgart\WS2022\05-Simulation Software Engineering\ex_pytest\testing-python-exercise-wt2223\test_diffusion2d_functions.py", line 44, in test_set_initial_condition
self.assertTrue((u == expected_u).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=3)


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
