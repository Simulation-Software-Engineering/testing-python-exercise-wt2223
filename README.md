# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

### unittest log

Introduced bug in the function `initialize_domain` leads to failure h statt w):

<pre><b>================================================================ test session starts =================================================================</b>
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/le/SSE/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                    </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                       [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#AA0000">F</font><font color="#00AA00">..</font><font color="#AA0000">                                                                                                   [100%]</font>

====================================================================== FAILURES ======================================================================
<font color="#FF5555"><b>_______________________________________________________________ test_initialize_domain _______________________________________________________________</b></font>

    <font color="#5555FF">def</font> <font color="#55FF55">test_initialize_domain</font>():
    <font color="#555555">    </font><font color="#AA5500">&quot;&quot;&quot;</font>
    <font color="#AA5500">    Check function SolveDiffusion2D.initialize_domain</font>
    <font color="#AA5500">    &quot;&quot;&quot;</font>
        solver = SolveDiffusion2D()
        w = <font color="#5555FF">12.</font>
        h = <font color="#5555FF">14.</font>
        dx = <font color="#5555FF">0.3</font>
        dy = <font color="#5555FF">0.4</font>

        expected_result_nx = pytest.approx(<font color="#5555FF">40.</font>, <font color="#55FFFF">abs</font>=<font color="#5555FF">0</font>)
        expected_result_ny = pytest.approx(<font color="#5555FF">35.</font>, <font color="#55FFFF">abs</font>=<font color="#5555FF">0</font>)

        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
&gt;       <font color="#5555FF">assert</font> expected_result_nx == solver.nx
<font color="#FF5555"><b>E       assert 40.0 ± 0.0e+00 == 46</b></font>
<font color="#FF5555"><b>E         comparison failed</b></font>
<font color="#FF5555"><b>E         Obtained: 46</b></font>
<font color="#FF5555"><b>E         Expected: 40.0 ± 1.0e-02</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:24: AssertionError
<font color="#55FFFF"><b>============================================================== short test summary info ===============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_initialize_domain</b> - assert 40.0 ± 0.0e+00 == 46
<font color="#AA0000">============================================================ </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.37s =============================================================</font>
</pre>

Introduced bug to function `initialize_physical_parameters` (- statt +):
<pre><b>================================================================ test session starts =================================================================</b>
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/le/SSE/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                    </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                       [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#00AA00">.</font><font color="#AA0000">F</font><font color="#00AA00">.</font><font color="#AA0000">                                                                                                   [100%]</font>

====================================================================== FAILURES ======================================================================
<font color="#FF5555"><b>________________________________________________________ test_initialize_physical_parameters _________________________________________________________</b></font>

    <font color="#5555FF">def</font> <font color="#55FF55">test_initialize_physical_parameters</font>():
    <font color="#555555">    </font><font color="#AA5500">&quot;&quot;&quot;</font>
    <font color="#AA5500">    Checks function SolveDiffusion2D.initialize_domain</font>
    <font color="#AA5500">    &quot;&quot;&quot;</font>
        solver = SolveDiffusion2D()
        solver.w = <font color="#5555FF">12.</font>
        solver.h = <font color="#5555FF">14.</font>
        d = <font color="#5555FF">2.</font>
        solver.dx = <font color="#5555FF">0.3</font>
        solver.dy = <font color="#5555FF">0.4</font>
        T_cold = <font color="#5555FF">200.</font>
        T_hot = <font color="#5555FF">500.</font>
    
        <font color="#555555"># expected_result_dx2, expected_result_dy2 = 0.09, 0.16</font>
        expected_result_dt = pytest.approx(<font color="#5555FF">0.0144</font>, <font color="#55FFFF">abs</font>=<font color="#5555FF">0.01</font>)
    
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
&gt;       <font color="#5555FF">assert</font> expected_result_dt == solver.dt
<font color="#FF5555"><b>E       assert 0.0144 ± 1.0e-02 == -0.051428571428571414</b></font>
<font color="#FF5555"><b>E         comparison failed</b></font>
<font color="#FF5555"><b>E         Obtained: -0.051428571428571414</b></font>
<font color="#FF5555"><b>E         Expected: 0.0144 ± 1.0e-02</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:45: AssertionError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
dt = -0.051428571428571414
<font color="#55FFFF"><b>============================================================== short test summary info ===============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_initialize_physical_parameters</b> - assert 0.0144 ± 1.0e-02 == -0.051428571428571414
<font color="#AA0000">============================================================ </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.36s =============================================================</font>
</pre>

Introduced bug in `set_initial_condition` (> statt <):
<pre><b>================================================================ test session starts =================================================================</b>
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/le/SSE/testing-python-exercise-wt2223
<b>collected 5 items                                                                                                                                    </b>

tests/integration/test_diffusion2d.py <font color="#00AA00">..                                                                                                       [ 40%]</font>
tests/unit/test_diffusion2d_functions.py <font color="#00AA00">..</font><font color="#AA0000">F                                                                                                   [100%]</font>

====================================================================== FAILURES ======================================================================
<font color="#FF5555"><b>_____________________________________________________________ test_set_initial_condition _____________________________________________________________</b></font>

    <font color="#5555FF">def</font> <font color="#55FF55">test_set_initial_condition</font>():
    <font color="#555555">    </font><font color="#AA5500">&quot;&quot;&quot;</font>
    <font color="#AA5500">    Checks function SolveDiffusion2D.get_initial_function</font>
    <font color="#AA5500">    &quot;&quot;&quot;</font>
        solver = SolveDiffusion2D()
        solver.nx = <font color="#5555FF">2</font>
        solver.ny = <font color="#5555FF">3</font>
        solver.T_cold = <font color="#5555FF">222.</font>
        solver.T_hot = <font color="#5555FF">555.</font>
        solver.dx = <font color="#5555FF">0.3</font>
        solver.dy = <font color="#5555FF">0.4</font>
    
        expected_result_u = np.array([[<font color="#5555FF">222.</font>, <font color="#5555FF">222.</font>, <font color="#5555FF">222.</font>],[<font color="#5555FF">222.</font>, <font color="#5555FF">222.</font>, <font color="#5555FF">222.</font>]])
        actual_u = solver.set_initial_condition()
&gt;       <font color="#5555FF">assert</font> np.array_equal(expected_result_u, actual_u)
<font color="#FF5555"><b>E       assert False</b></font>
<font color="#FF5555"><b>E        +  where False = &lt;function array_equal at 0x7f31aa990160&gt;(array([[222., 222., 222.],\n       [222., 222., 222.]]), array([[555., 555., 555.],\n       [555., 555., 555.]]))</b></font>
<font color="#FF5555"><b>E        +    where &lt;function array_equal at 0x7f31aa990160&gt; = np.array_equal</b></font>

<font color="#FF5555"><b>tests/unit/test_diffusion2d_functions.py</b></font>:64: AssertionError
<font color="#55FFFF"><b>============================================================== short test summary info ===============================================================</b></font>
<font color="#AA0000">FAILED</font> tests/unit/test_diffusion2d_functions.py::<b>test_set_initial_condition</b> - assert False
<font color="#AA0000">============================================================ </font><font color="#FF5555"><b>1 failed</b></font>, <font color="#00AA00">4 passed</font><font color="#AA0000"> in 0.37s =============================================================</font>
</pre>

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).