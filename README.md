# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### Bug in test_initialize_domain()
I changed `self.nx = int(w / dx)` to `self.nx = int(h / dx)`.

<pre><b>=============================================================== test session starts ===============================================================</b>
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                 </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                    [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#AA0000">F</font><font color="#00AA00">..</font><font color="#AA0000">                                                                                                [100%]</font>

==================================================================== FAILURES =====================================================================
<font color="#FF5555"><b>_____________________________________________________________ test_initialize_domain ______________________________________________________________</b></font>

    def test_initialize_domain():
        &quot;&quot;&quot;
        Check function SolveDiffusion2D.initialize_domain
        &quot;&quot;&quot;
        solver = SolveDiffusion2D()
        w = 12.0
        h = 14.0
        dx = 0.3
        dy = 0.4
    
        expected_result_nx = pytest.approx(40.0, abs=0)
        expected_result_ny = pytest.approx(35.0, abs=0)
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    
&gt;       assert expected_result_nx == solver.nx
<font color="#FF5555"><b>E       assert 40.0 ± 0.0e+00 == 46</b></font>
<font color="#FF5555"><b>E         comparison failed</b></font>
<font color="#FF5555"><b>E         Obtained: 46</b></font>
<font color="#FF5555"><b>E         Expected: 40.0 ± 0.0e+00</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:24: AssertionError
<font color="#55FFFF"><b>============================================================= short test summary info =============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_initialize_domain</b> - assert 40.0 ± 0.0e+00 == 46
<font color="#AA0000">=========================================================== </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.51s ===========================================================</font>
</pre>

#### Bug in test_initialize_physical_parameters()
I changed `self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))` to `self.dt = dx2 * dy2 / (2 * self.D * (dx2 - dy2))`.

<pre><b>=============================================================== test session starts ===============================================================</b>
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                 </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                    [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#00AA00">.</font><font color="#AA0000">F</font><font color="#00AA00">.</font><font color="#AA0000">                                                                                                [100%]</font>

==================================================================== FAILURES =====================================================================
<font color="#FF5555"><b>_______________________________________________________ test_initialize_physical_parameters _______________________________________________________</b></font>

    def test_initialize_physical_parameters():
        &quot;&quot;&quot;
        Checks function SolveDiffusion2D.initialize_domain
        &quot;&quot;&quot;
        solver = SolveDiffusion2D()
        solver.w = 12.0
        solver.h = 14.0
        solver.dx = 0.3
        solver.dy = 0.4
        d = 2.0
        T_cold = 250.0
        T_hot = 800.0
    
        expected_dt = pytest.approx(0.0144, abs=0.01)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        assert T_cold == solver.T_cold
        assert T_hot == solver.T_hot
&gt;       assert expected_dt == solver.dt
<font color="#FF5555"><b>E       assert 0.0144 ± 1.0e-02 == -0.051428571428571414</b></font>
<font color="#FF5555"><b>E         comparison failed</b></font>
<font color="#FF5555"><b>E         Obtained: -0.051428571428571414</b></font>
<font color="#FF5555"><b>E         Expected: 0.0144 ± 1.0e-02</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:46: AssertionError
-------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------
dt = -0.051428571428571414
<font color="#55FFFF"><b>============================================================= short test summary info =============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_initialize_physical_parameters</b> - assert 0.0144 ± 1.0e-02 == -0.051428571428571414
<font color="#AA0000">=========================================================== </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.52s ===========================================================</font>
</pre>

#### Bug in test_set_initial_condition()
I changed `if p2 < r2:` to `if p2 >= r2:`.

<pre><b>=============================================================== test session starts ===============================================================</b>
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                 </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                    [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#00AA00">..</font><font color="#AA0000">F                                                                                                [100%]</font>

==================================================================== FAILURES =====================================================================
<font color="#FF5555"><b>___________________________________________________________ test_set_initial_condition ____________________________________________________________</b></font>

    def test_set_initial_condition():
        &quot;&quot;&quot;
        Checks function SolveDiffusion2D.get_initial_function
        &quot;&quot;&quot;
        solver = SolveDiffusion2D()
        solver.nx = 2
        solver.ny = 3
        solver.T_cold = 222.
        solver.T_hot = 555.
        solver.dx = 0.3
        solver.dy = 0.4
    
        expected_u = np.array([[222., 222., 222.], [222., 222., 222.]])
    
        actual_u = solver.set_initial_condition()
    
&gt;       assert np.array_equal(expected_u, actual_u)
<font color="#FF5555"><b>E       assert False</b></font>
<font color="#FF5555"><b>E        +  where False = &lt;function array_equal at 0x7f2eac3a1e10&gt;(array([[222., 222., 222.],\n       [222., 222., 222.]]), array([[555., 555., 555.],\n       [555., 555., 555.]]))</b></font>
<font color="#FF5555"><b>E        +    where &lt;function array_equal at 0x7f2eac3a1e10&gt; = np.array_equal</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:65: AssertionError
<font color="#55FFFF"><b>============================================================= short test summary info =============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_set_initial_condition</b> - assert False
<font color="#AA0000">=========================================================== </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.51s ===========================================================</font></pre>

### unittest log

#### Bug in test_initialize_domain()
I changed `self.nx = int(w / dx)` to `self.nx = int(h / dx)`.

<pre>Fdt = 0.014400000000000003
..
======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File &quot;/home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py&quot;, line 29, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_result_nx)
AssertionError: 46 != 40.0

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
</pre>

#### Bug in test_initialize_physical_parameters()
I changed `self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))` to `self.dt = dx2 * dy2 / (2 * self.D * (dx2 - dy2))`.

<pre>.dt = -0.051428571428571414
F.
======================================================================
FAIL: test_initialize_physical_parameters (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File &quot;/home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py&quot;, line 50, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, expected_dt, 1)
AssertionError: -0.051428571428571414 != 0.0144 within 1 places (0.06582857142857142 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
</pre>


#### Bug in test_set_initial_condition()
I changed `if p2 < r2:` to `if p2 >= r2:`.

<pre>.dt = 0.014400000000000003
.F
======================================================================
FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File &quot;/home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223/tests/unit/test_diffusion2d_functions.py&quot;, line 67, in test_set_initial_condition
    self.assertTrue(np.array_equal(actual_u, expected_u))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
</pre>

## Integration Tests
I changed `self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))` to `self.dt = dx2 * dy2 / (2 * self.D * (dx2 - dy2))` and `self.nx = int(w / dx)` to `self.nx = int(h / dx)` causing both integration tests to fail.

<pre><b>=============================================== test session starts ================================================</b>
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/kim/Documents/SSE/exercises/ex05/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                  </b>

tests/integration/test_diffusion2d.py <font color="#AA0000">FF                                                                     [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#AA0000">FF</font><font color="#00AA00">.</font><font color="#AA0000">                                                                 [100%]</font>

===================================================== FAILURES =====================================================
<font color="#FF5555"><b>_______________________________________ test_initialize_physical_parameters ________________________________________</b></font>

    def test_initialize_physical_parameters():
        &quot;&quot;&quot;
        Checks function SolveDiffusion2D.initialize_domain
        &quot;&quot;&quot;
        solver = SolveDiffusion2D()
        w = 12.0
        h = 14.0
        dx = 0.3
        dy = 0.4
        d = 2.0
        T_cold = 250.0
        T_hot = 800.0
    
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        expected_dt = pytest.approx(0.0144, 0.01)
    
&gt;       assert solver.dt == expected_dt
<font color="#FF5555"><b>E       assert -0.051428571428571414 == 0.0144 ± 1.4e-04</b></font>
<font color="#FF5555"><b>E         comparison failed</b></font>
<font color="#FF5555"><b>E         Obtained: -0.051428571428571414</b></font>
<font color="#FF5555"><b>E         Expected: 0.0144 ± 1.4e-04</b></font>

<font color="#FF5555"><b>tests/integration/test_diffusion2d.py</b></font>:28: AssertionError
----------------------------------------------- Captured stdout call -----------------------------------------------
dt = -0.051428571428571414
<font color="#FF5555"><b>____________________________________________ test_set_initial_condition ____________________________________________</b></font>

    def test_set_initial_condition():
        &quot;&quot;&quot;
        Checks function SolveDiffusion2D.get_initial_function
        &quot;&quot;&quot;
        solver = SolveDiffusion2D()
        w = 0.6
        h = 12.0
        T_cold = 222.0
        T_hot = 555.0
        dx = 0.3
        dy = 4.0
        d = 5.0
    
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        expected_u = np.array([[222., 222., 222.], [222., 222., 222.]])
    
        actual_u = solver.set_initial_condition()
    
&gt;       assert np.array_equal(actual_u, expected_u)
<font color="#FF5555"><b>E       assert False</b></font>
<font color="#FF5555"><b>E        +  where False = &lt;function array_equal at 0x7f7e40d66320&gt;(array([[222., 222., 222.],\n       [222., 222., 222.],\n       [222., 222., 222.],\n       [222., 222., 222.],\n       [22...2., 222.],\n       [222., 222., 222.],\n       [222., 222., 222.],\n       [222., 222., 222.],\n       [222., 222., 222.]]), array([[222., 222., 222.],\n       [222., 222., 222.]]))</b></font>
<font color="#FF5555"><b>E        +    where &lt;function array_equal at 0x7f7e40d66320&gt; = np.array_equal</b></font>

<font color="#FF5555"><b>tests/integration/test_diffusion2d.py</b></font>:51: AssertionError
----------------------------------------------- Captured stdout call -----------------------------------------------
dt = -0.009050911376492771
<font color="#FF5555"><b>______________________________________ TestDiffusion2D.test_initialize_domain ______________________________________</b></font>

self = &lt;test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain&gt;

    def test_initialize_domain(self):
        &quot;&quot;&quot;
        Check function SolveDiffusion2D.initialize_domain
        &quot;&quot;&quot;
        w = 12.0
        h = 14.0
        dx = 0.3
        dy = 0.4
    
        expected_result_nx = 40.0
        expected_result_ny = 35.0
        self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    
&gt;       self.assertEqual(self.solver.nx, expected_result_nx)
<font color="#FF5555"><b>E       AssertionError: 46 != 40.0</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:29: AssertionError
<font color="#FF5555"><b>_______________________________ TestDiffusion2D.test_initialize_physical_parameters ________________________________</b></font>

self = &lt;test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters&gt;

    def test_initialize_physical_parameters(self):
        &quot;&quot;&quot;
        Checks function SolveDiffusion2D.initialize_domain
        &quot;&quot;&quot;
        self.solver.w = 12.0
        self.solver.h = 14.0
        self.solver.dx = 0.3
        self.solver.dy = 0.4
        d = 2.0
        T_cold = 250.0
        T_hot = 800.0
    
        expected_dt = 0.0144
        self.solver.initialize_physical_parameters(
            d=d, T_cold=T_cold, T_hot=T_hot)
    
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
&gt;       self.assertAlmostEqual(self.solver.dt, expected_dt, 1)
<font color="#FF5555"><b>E       AssertionError: -0.051428571428571414 != 0.0144 within 1 places (0.06582857142857142 difference)</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:50: AssertionError
----------------------------------------------- Captured stdout call -----------------------------------------------
dt = -0.051428571428571414
<font color="#55FFFF"><b>============================================= short test summary info ==============================================</b></font>
<font color="#AA0000">FAILED</font> tests/integration/test_diffusion2d.py::<b>test_initialize_physical_parameters</b> - assert -0.051428571428571414 == 0.0144 ± 1.4e-04
<font color="#AA0000">FAILED</font> tests/integration/test_diffusion2d.py::<b>test_set_initial_condition</b> - assert False
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>TestDiffusion2D::test_initialize_domain</b> - AssertionError: 46 != 40.0
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>TestDiffusion2D::test_initialize_physical_parameters</b> - AssertionError: -0.051428571428571414 != 0.0144 within 1 places (0.06582857142857142 difference)
<font color="#AA0000">=========================================== </font><font color="#FF5555"><b>4 failed</b></font>, <font color="#00AA00">1 passed</font><font color="#AA0000"> in 0.43s ============================================</font>
</pre>

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
