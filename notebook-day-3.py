import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return la, np, plt, sci, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & +\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation

    The output is defined as

    \[
    h =
    \begin{bmatrix}
    x - (\ell/6)\sin\theta \\
    y + (\ell/6)\cos\theta
    \end{bmatrix}.
    \]

    The point \((x,y)\) is the center of mass of the booster.

    The vector

    \[
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]

    points along the booster axis from the center of mass toward the top of the booster.

    Therefore,

    \[
    h =
    \begin{bmatrix}
    x\\
    y
    \end{bmatrix}
    +
    \frac{\ell}{6}
    \begin{bmatrix}
    -\sin\theta\\
    \cos\theta
    \end{bmatrix}.
    \]

    So \(h\) is a point located on the booster axis, at a distance \(\ell/6\) from the center of mass, in the direction of the top of the booster.

    Since the distance from the center of mass to the top of the booster is \(\ell/2\), the point \(h\) is one third of the way from the center of mass to the top:

    \[
    \frac{\ell/6}{\ell/2}
    =
    \frac{1}{3}.
    \]

    Geometrically, \(h\) is not the center of mass. It is a point fixed on the booster body, located above the center of mass along the booster axis.
    """)
    return


@app.cell
def _(l, mo, np, svg, world):
    # Geometrical interpretation of h
    # We draw:
    # - the booster body,
    # - the center of mass (x, y),
    # - the point h,
    # - the segment from the center of mass to h.

    geom_x = 0.0
    geom_y = 2.0
    geom_theta = np.pi / 6

    # Coordinates of h
    geom_h_x = geom_x - (l / 6) * np.sin(geom_theta)
    geom_h_y = geom_y + (l / 6) * np.cos(geom_theta)

    # Coordinates of the top and bottom of the booster
    geom_top_x = geom_x - (l / 2) * np.sin(geom_theta)
    geom_top_y = geom_y + (l / 2) * np.cos(geom_theta)

    geom_bottom_x = geom_x + (l / 2) * np.sin(geom_theta)
    geom_bottom_y = geom_y - (l / 2) * np.cos(geom_theta)

    mo.Html(
        world(
            [-2, 2, -1, 4],
        
            # Booster axis
            svg.line(
                x1=geom_bottom_x,
                y1=geom_bottom_y,
                x2=geom_top_x,
                y2=geom_top_y,
                stroke="black",
                stroke_width="0.05",
            ),

            # Center of mass
            svg.circle(
                cx=geom_x,
                cy=geom_y,
                r=0.07,
                fill="blue",
            ),

            # Point h
            svg.circle(
                cx=geom_h_x,
                cy=geom_h_y,
                r=0.07,
                fill="red",
            ),

            # Segment from center of mass to h
            svg.line(
                x1=geom_x,
                y1=geom_y,
                x2=geom_h_x,
                y2=geom_h_y,
                stroke="red",
                stroke_width="0.03",
                stroke_dasharray="0.08 0.05",
            ),

            # Labels
            svg.text(
                x=geom_x + 0.1,
                y=geom_y,
                fill="blue",
            )("center $(x,y)$"),

            svg.text(
                x=geom_h_x + 0.1,
                y=geom_h_y,
                fill="red",
            )("$h$"),
        )
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interpretation of the drawing

    In the drawing:

    - the black line represents the booster axis;
    - the blue point is the center of mass \((x,y)\);
    - the red point is \(h\);
    - the dashed red segment shows the displacement from \((x,y)\) to \(h\).

    The vector from the center of mass to \(h\) is

    \[
    \frac{\ell}{6}
    \begin{bmatrix}
    -\sin\theta\\
    \cos\theta
    \end{bmatrix}.
    \]

    So \(h\) is attached to the booster body. When the booster rotates, the point \(h\) rotates with it.

    Thus, \(h\) can be interpreted as a controlled output point located on the booster axis, above the center of mass.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    We have

    \[
    h =
    \begin{bmatrix}
    x - \frac{\ell}{6}\sin\theta \\
    y + \frac{\ell}{6}\cos\theta
    \end{bmatrix}.
    \]

    Differentiate once:

    \[
    \dot h =
    \begin{bmatrix}
    \dot{x} - \frac{\ell}{6}\cos\theta \dot{\theta} \\
    \dot{y} - \frac{\ell}{6}\sin\theta \dot{\theta}
    \end{bmatrix}.
    \]

    Differentiate again:

    \[
    \ddot h =
    \begin{bmatrix}
    \ddot{x}
    +
    \frac{\ell}{6}\sin\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\cos\theta \ddot{\theta}
    \\
    \ddot{y}
    -
    \frac{\ell}{6}\cos\theta \dot{\theta}^2
    -
    \frac{\ell}{6}\sin\theta \ddot{\theta}
    \end{bmatrix}.
    \]

    When the auxiliary system is plugged in, the force is chosen so that the \(\dot{\theta}^2\) terms cancel. We obtain

    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta - g
    \end{bmatrix}.
    \]

    So the final result is

    \[
    \boxed{
    \dot h =
    \begin{bmatrix}
    \dot{x} - \frac{\ell}{6}\cos\theta \dot{\theta} \\
    \dot{y} - \frac{\ell}{6}\sin\theta \dot{\theta}
    \end{bmatrix}
    }
    \]

    and

    \[
    \boxed{
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta - g
    \end{bmatrix}
    }.
    \]
    """)
    return


@app.cell
def _(M, g, l, np):
    # First and second-order derivatives of h

    def fsod_h_and_derivatives(x, dx, y, dy, theta, dtheta, z):
        """
        Compute h, dh, and d2h.

        Inputs:
            x, dx       : horizontal position and velocity
            y, dy       : vertical position and velocity
            theta       : tilt angle
            dtheta      : angular velocity
            z           : auxiliary variable

        Returns:
            h, dh, d2h
        """

        fsod_h = np.array([
            x - (l / 6) * np.sin(theta),
            y + (l / 6) * np.cos(theta),
        ])

        fsod_dh = np.array([
            dx - (l / 6) * np.cos(theta) * dtheta,
            dy - (l / 6) * np.sin(theta) * dtheta,
        ])

        fsod_d2h = np.array([
            (z / M) * np.sin(theta),
            -(z / M) * np.cos(theta) - g,
        ])

        return fsod_h, fsod_dh, fsod_d2h

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    From the previous result,

    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta-g
    \end{bmatrix}.
    \]

    Differentiate once:

    \[
    h^{(3)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \dot z \sin\theta + z\dot\theta\cos\theta \\
    -\dot z \cos\theta + z\dot\theta\sin\theta
    \end{bmatrix}.
    \]

    Now differentiate again.

    Since the auxiliary system gives

    \[
    \ddot z = v_1,
    \]

    and

    \[
    \ddot\theta = \frac{v_2}{z},
    \]

    we obtain

    \[
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    (v_1-z\dot\theta^2)\sin\theta
    +
    (v_2+2\dot z\dot\theta)\cos\theta
    \\
    -(v_1-z\dot\theta^2)\cos\theta
    +
    (v_2+2\dot z\dot\theta)\sin\theta
    \end{bmatrix}.
    \]

    So the final results are

    \[
    \boxed{
    h^{(3)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \dot z \sin\theta + z\dot\theta\cos\theta \\
    -\dot z \cos\theta + z\dot\theta\sin\theta
    \end{bmatrix}
    }
    \]

    and

    \[
    \boxed{
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    (v_1-z\dot\theta^2)\sin\theta
    +
    (v_2+2\dot z\dot\theta)\cos\theta
    \\
    -(v_1-z\dot\theta^2)\cos\theta
    +
    (v_2+2\dot z\dot\theta)\sin\theta
    \end{bmatrix}
    }.
    \]
    """)
    return


@app.cell
def _(M, np):
    # Third and fourth-order derivatives of h

    def tfod_h3_h4(theta, dtheta, z, dz, v):
        """
        Compute h^(3) and h^(4).

        Inputs:
            theta  : tilt angle
            dtheta : angular velocity
            z      : auxiliary state
            dz     : derivative of z
            v      : auxiliary input [v1, v2]

        Returns:
            h3, h4
        """

        v1 = v[0]
        v2 = v[1]

        tfod_h3 = (1 / M) * np.array([
            dz * np.sin(theta) + z * dtheta * np.cos(theta),
            -dz * np.cos(theta) + z * dtheta * np.sin(theta),
        ])

        tfod_a = v1 - z * dtheta**2
        tfod_b = v2 + 2 * dz * dtheta

        tfod_h4 = (1 / M) * np.array([
            tfod_a * np.sin(theta) + tfod_b * np.cos(theta),
            -tfod_a * np.cos(theta) + tfod_b * np.sin(theta),
        ])

        return tfod_h3, tfod_h4

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Differentiating $h^{(3)}$ one more time yields the fourth derivative:

    $$
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    (v_1-z\dot\theta^2)\sin\theta + (v_2+2\dot z\dot\theta)\cos\theta \\
    -(v_1-z\dot\theta^2)\cos\theta + (v_2+2\dot z\dot\theta)\sin\theta
    \end{bmatrix}
    $$

    To keep things readable, we introduce two shorthand quantities:

    $$
    a = v_1 - z\dot\theta^2, \qquad b = v_2 + 2\dot z\dot\theta
    $$

    and the expression collapses into a clean rotation-like product:

    $$
    h^{(4)}
    =
    \frac{1}{M}
    \begin{bmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{bmatrix}
    \begin{bmatrix} a \\ b \end{bmatrix}
    $$

    The goal is to impose $h^{(4)} = u$, turning the system into a pure double integrator.
    Inverting the rotation matrix (which is orthogonal, so its inverse is just its transpose) gives:

    $$
    \begin{bmatrix} a \\ b \end{bmatrix}
    =
    M
    \begin{bmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{bmatrix}
    \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}
    $$

    Reading off the two components explicitly:

    $$
    a = M(u_1\sin\theta - u_2\cos\theta), \qquad b = M(u_1\cos\theta + u_2\sin\theta)
    $$

    Substituting back the definitions of $a$ and $b$, we can solve directly for the actual inputs $v_1$ and $v_2$:

    $$
    \boxed{v_1 = z\dot\theta^2 + M(u_1\sin\theta - u_2\cos\theta)}
    $$

    $$
    \boxed{v_2 = -2\dot z\dot\theta + M(u_1\cos\theta + u_2\sin\theta)}
    $$

    With this choice, all the nonlinear terms cancel exactly, and the closed-loop system satisfies simply:

    $$
    \boxed{h^{(4)} = u}
    $$
    """)
    return


@app.cell
def _(M, np):
    # Exact linearization
    # Given the new input u = [u1, u2],
    # compute v = [v1, v2] such that h^(4) = u.

    def exlin_v(theta, dtheta, z, dz, u):
        """
        Compute the auxiliary input v = [v1, v2]
        that gives h^(4) = u.

        Inputs:
            theta  : tilt angle
            dtheta : angular velocity
            z      : auxiliary state
            dz     : derivative of z
            u      : desired fourth derivative [u1, u2]

        Returns:
            v = [v1, v2]
        """

        u1 = u[0]
        u2 = u[1]

        v1 = (
            z * dtheta**2
            + M * (u1 * np.sin(theta) - u2 * np.cos(theta))
        )

        v2 = (
            -2 * dz * dtheta
            + M * (u1 * np.cos(theta) + u2 * np.sin(theta))
        )

        return np.array([v1, v2])

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    We define the output $h$ directly from the position variables $(x,\, y,\, \theta)$:

    $$
    h = \begin{bmatrix} x - \frac{\ell}{6}\sin\theta \\ y + \frac{\ell}{6}\cos\theta \end{bmatrix}
    $$

    Differentiating once brings in the velocities $(\dot x,\, \dot y,\, \dot\theta)$:

    $$
    \dot h = \begin{bmatrix} \dot x - \frac{\ell}{6}\cos\theta\,\dot\theta \\ \dot y - \frac{\ell}{6}\sin\theta\,\dot\theta \end{bmatrix}
    $$

    Differentiating again, the thrust $z$ enters the picture alongside $\theta$:

    $$
    \ddot h = \begin{bmatrix} \frac{z}{M}\sin\theta \\ -\frac{z}{M}\cos\theta - g \end{bmatrix}
    $$

    One more derivative, and the full set $(z,\, \dot z,\, \theta,\, \dot\theta)$ is needed:

    $$
    h^{(3)} = \frac{1}{M}\begin{bmatrix} \dot z\sin\theta + z\dot\theta\cos\theta \\ -\dot z\cos\theta + z\dot\theta\sin\theta \end{bmatrix}
    $$

    Each differentiation step draws in a new layer of the state, until all eight variables have appeared. Altogether, the function `Tr` achieves the mapping

    $$
    (x,\,\dot x,\,y,\,\dot y,\,\theta,\,\dot\theta,\,z,\,\dot z)
    \;\longmapsto\;
    (h_x,\,h_y,\,\dot h_x,\,\dot h_y,\,\ddot h_x,\,\ddot h_y,\,h_x^{(3)},\,h_y^{(3)})
    $$
    """)
    return


@app.cell
def _(M, g, l, np):
    # State to derivatives of the output

    def Tr(x, dx, y, dy, theta, dtheta, z, dz):
        """
        Convert the state variables into the output h
        and its first three derivatives.

        Inputs:
            x, dx       : horizontal position and velocity
            y, dy       : vertical position and velocity
            theta       : tilt angle
            dtheta      : angular velocity
            z, dz       : auxiliary state and its derivative

        Returns:
            h_x, h_y,
            dh_x, dh_y,
            d2h_x, d2h_y,
            d3h_x, d3h_y
        """

        # h
        h_x = x - (l / 6) * np.sin(theta)
        h_y = y + (l / 6) * np.cos(theta)

        # first derivative of h
        dh_x = dx - (l / 6) * np.cos(theta) * dtheta
        dh_y = dy - (l / 6) * np.sin(theta) * dtheta

        # second derivative of h
        d2h_x = (z / M) * np.sin(theta)
        d2h_y = -(z / M) * np.cos(theta) - g

        # third derivative of h
        d3h_x = (1 / M) * (
            dz * np.sin(theta)
            + z * dtheta * np.cos(theta)
        )

        d3h_y = (1 / M) * (
            -dz * np.cos(theta)
            + z * dtheta * np.sin(theta)
        )

        return (
            h_x,
            h_y,
            dh_x,
            dh_y,
            d2h_x,
            d2h_y,
            d3h_x,
            d3h_y,
        )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion

    We assume\[z<0.\]

    We are given

    \[
    h,\quad \dot h,\quad \ddot h,\quad h^{(3)}.
    \]

    From the previous formulas,

    \[
    \ddot h =
    \begin{bmatrix}
    \frac{z}{M}\sin\theta \\
    -\frac{z}{M}\cos\theta-g
    \end{bmatrix}.
    \]

    So

    \[
    \ddot h+
    \begin{bmatrix}
    0\\
    g
    \end{bmatrix}
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta\\
    -\cos\theta
    \end{bmatrix}.
    \]

    Let

    \[
    r=
    \sqrt{
    \ddot h_x^2+
    (\ddot h_y+g)^2
    }.
    \]

    Since \(z<0\),

    \[
    z=-Mr.
    \]

    Also,

    \[
    \sin\theta=-\frac{\ddot h_x}{r},
    \quad
    \cos\theta=\frac{\ddot h_y+g}{r}.
    \]

    Therefore,

    \[
    \theta=
    \operatorname{atan2}
    \left(
    -\ddot h_x,
    \ddot h_y+g
    \right).
    \]

    Now, using

    \[
    h=
    \begin{bmatrix}
    x-\frac{\ell}{6}\sin\theta\\
    y+\frac{\ell}{6}\cos\theta
    \end{bmatrix},
    \]

    we recover

    \[
    x=h_x+\frac{\ell}{6}\sin\theta,
    \]

    \[
    y=h_y-\frac{\ell}{6}\cos\theta.
    \]

    Using

    \[
    \dot h=
    \begin{bmatrix}
    \dot x-\frac{\ell}{6}\cos\theta\dot\theta\\
    \dot y-\frac{\ell}{6}\sin\theta\dot\theta
    \end{bmatrix},
    \]

    we recover

    \[
    \dot x=\dot h_x+\frac{\ell}{6}\cos\theta\dot\theta,
    \]

    \[
    \dot y=\dot h_y+\frac{\ell}{6}\sin\theta\dot\theta.
    \]

    It remains to recover \(\dot\theta\) and \(\dot z\).

    From

    \[
    h^{(3)}
    =
    \frac{1}{M}
    \begin{bmatrix}
    \dot z\sin\theta+z\dot\theta\cos\theta\\
    -\dot z\cos\theta+z\dot\theta\sin\theta
    \end{bmatrix},
    \]

    we get

    \[
    \dot z
    =
    M
    \left(
    h^{(3)}_x\sin\theta
    -
    h^{(3)}_y\cos\theta
    \right),
    \]

    and

    \[
    z\dot\theta
    =
    M
    \left(
    h^{(3)}_x\cos\theta
    +
    h^{(3)}_y\sin\theta
    \right).
    \]

    Since \(z\neq0\),

    \[
    \dot\theta
    =
    \frac{
    M
    \left(
    h^{(3)}_x\cos\theta
    +
    h^{(3)}_y\sin\theta
    \right)
    }{z}.
    \]

    Thus, from \(h,\dot h,\ddot h,h^{(3)}\), we recover uniquely

    \[
    x,\dot x,y,\dot y,\theta,\dot\theta,z,\dot z.
    \]
    """)
    return


@app.cell
def _(M, g, l, np):
    # Inversion
    # Given: h, dh, d2h, d3h

    # Recover: x, dx, y, dy, theta, dtheta, z, dz

    # Assumption: z < 0

    def T_inv(h, dh, d2h, d3h):
        """
        Invert the transformation from output derivatives to state variables.

        Inputs:
            h    = [h_x, h_y]
            dh   = [dh_x, dh_y]
            d2h  = [d2h_x, d2h_y]
            d3h  = [d3h_x, d3h_y]

        Returns:
            [x, dx, y, dy, theta, dtheta, z, dz]
        """

        inv_hx = h[0]
        inv_hy = h[1]

        inv_dhx = dh[0]
        inv_dhy = dh[1]

        inv_d2hx = d2h[0]
        inv_d2hy = d2h[1]

        inv_d3hx = d3h[0]
        inv_d3hy = d3h[1]

        # Compute r = sqrt(d2h_x^2 + (d2h_y + g)^2)
        inv_r = np.sqrt(
            inv_d2hx**2
            + (inv_d2hy + g)**2
        )

        if inv_r == 0:
            raise ValueError("Inversion is not possible because r = 0.")

        # Since z < 0:
        inv_z = -M * inv_r

        # Recover sin(theta) and cos(theta)
        inv_sin_theta = -inv_d2hx / inv_r
        inv_cos_theta = (inv_d2hy + g) / inv_r

        # Recover theta
        inv_theta = np.arctan2(
            inv_sin_theta,
            inv_cos_theta,
        )

        # Recover dz
        inv_dz = M * (
            inv_d3hx * inv_sin_theta
            - inv_d3hy * inv_cos_theta
        )

        # Recover dtheta
        inv_dtheta = (
            M
            * (
                inv_d3hx * inv_cos_theta
                + inv_d3hy * inv_sin_theta
            )
            / inv_z
        )

        # Recover x and y from h
        inv_x = inv_hx + (l / 6) * inv_sin_theta
        inv_y = inv_hy - (l / 6) * inv_cos_theta

        # Recover dx and dy from dh
        inv_dx = inv_dhx + (l / 6) * inv_cos_theta * inv_dtheta
        inv_dy = inv_dhy + (l / 6) * inv_sin_theta * inv_dtheta

        return np.array([
            inv_x,
            inv_dx,
            inv_y,
            inv_dy,
            inv_theta,
            inv_dtheta,
            inv_z,
            inv_dz,
        ])

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    We want to construct a trajectory between an initial state and a final state.

    The exact linearization gives

    \[
    h^{(4)}=u.
    \]

    So we can choose an admissible path for \(h(t)\), then recover the original variables using the inverse transformation.

    The idea is:

    1. Convert the initial state into

    \[
    h(0),\dot h(0),\ddot h(0),h^{(3)}(0).
    \]

    2. Convert the final state into

    \[
    h(t_f),\dot h(t_f),\ddot h(t_f),h^{(3)}(t_f).
    \]

    3. For each coordinate of \(h\), build a polynomial of degree \(7\).

    A degree \(7\) polynomial has 8 coefficients, so it can match 8 boundary conditions:

    \[
    h(0),\dot h(0),\ddot h(0),h^{(3)}(0),
    \]

    and

    \[
    h(t_f),\dot h(t_f),\ddot h(t_f),h^{(3)}(t_f).
    \]

    Then, at each time \(t\), we compute

    \[
    h(t),\dot h(t),\ddot h(t),h^{(3)}(t),h^{(4)}(t).
    \]

    Using the inverse map, we recover

    \[
    x,\dot x,y,\dot y,\theta,\dot\theta,z,\dot z.
    \]

    Finally, since

    \[
    u=h^{(4)},
    \]

    we compute \(v\), then the force components, and finally recover \(f\) and \(\phi\).
    """)
    return


@app.cell
def _(M, g, l, np):
    # Admissible Path Computation

    def ac_Tr(x, dx, y, dy, theta, dtheta, z, dz):
        """
        Convert state variables into:
        h, dh, d2h, d3h.
        """

        ac_h = np.array([
            x - (l / 6) * np.sin(theta),
            y + (l / 6) * np.cos(theta),
        ])

        ac_dh = np.array([
            dx - (l / 6) * np.cos(theta) * dtheta,
            dy - (l / 6) * np.sin(theta) * dtheta,
        ])

        ac_d2h = np.array([
            (z / M) * np.sin(theta),
            -(z / M) * np.cos(theta) - g,
        ])

        ac_d3h = (1 / M) * np.array([
            dz * np.sin(theta) + z * dtheta * np.cos(theta),
            -dz * np.cos(theta) + z * dtheta * np.sin(theta),
        ])

        return ac_h, ac_dh, ac_d2h, ac_d3h


    def ac_T_inv(h, dh, d2h, d3h):
        """
        Recover:
        x, dx, y, dy, theta, dtheta, z, dz
        from h, dh, d2h, d3h.

        We use the assumption z < 0.
        """

        ac_r = np.sqrt(
            d2h[0]**2
            + (d2h[1] + g)**2
        )

        if ac_r == 0:
            raise ValueError("Inversion impossible because r = 0.")

        ac_z = -M * ac_r

        ac_sin_theta = -d2h[0] / ac_r
        ac_cos_theta = (d2h[1] + g) / ac_r

        ac_theta = np.arctan2(
            ac_sin_theta,
            ac_cos_theta,
        )

        ac_dz = M * (
            d3h[0] * ac_sin_theta
            - d3h[1] * ac_cos_theta
        )

        ac_dtheta = (
            M
            * (
                d3h[0] * ac_cos_theta
                + d3h[1] * ac_sin_theta
            )
            / ac_z
        )

        ac_x = h[0] + (l / 6) * ac_sin_theta
        ac_y = h[1] - (l / 6) * ac_cos_theta

        ac_dx = dh[0] + (l / 6) * ac_cos_theta * ac_dtheta
        ac_dy = dh[1] + (l / 6) * ac_sin_theta * ac_dtheta

        return np.array([
            ac_x,
            ac_dx,
            ac_y,
            ac_dy,
            ac_theta,
            ac_dtheta,
            ac_z,
            ac_dz,
        ])


    def ac_v_from_u(theta, dtheta, z, dz, u):
        """
        Compute v = [v1, v2] such that h^(4) = u.
        """

        u1 = u[0]
        u2 = u[1]

        ac_v1 = (
            z * dtheta**2
            + M * (u1 * np.sin(theta) - u2 * np.cos(theta))
        )

        ac_v2 = (
            -2 * dz * dtheta
            + M * (u1 * np.cos(theta) + u2 * np.sin(theta))
        )

        return np.array([
            ac_v1,
            ac_v2,
        ])

    return ac_T_inv, ac_Tr, ac_v_from_u


@app.cell
def _(np):
    def ac_poly_row(t, derivative_order):
        """
        Row used to impose a derivative constraint on a degree 7 polynomial.
        """

        ac_row = np.zeros(8)

        for k in range(derivative_order, 8):
            ac_coeff = 1.0

            for j in range(derivative_order):
                ac_coeff *= k - j

            ac_row[k] = ac_coeff * t**(k - derivative_order)

        return ac_row


    def ac_poly_coeffs(p0, dp0, d2p0, d3p0, pf, dpf, d2pf, d3pf, tf):
        """
        Compute degree 7 polynomial coefficients satisfying:
        p, p', p'', p''' at t=0 and t=tf.
        """

        ac_A = np.vstack([
            ac_poly_row(0.0, 0),
            ac_poly_row(0.0, 1),
            ac_poly_row(0.0, 2),
            ac_poly_row(0.0, 3),
            ac_poly_row(tf, 0),
            ac_poly_row(tf, 1),
            ac_poly_row(tf, 2),
            ac_poly_row(tf, 3),
        ])

        ac_b = np.array([
            p0,
            dp0,
            d2p0,
            d3p0,
            pf,
            dpf,
            d2pf,
            d3pf,
        ])

        return np.linalg.solve(ac_A, ac_b)


    def ac_eval_poly(coeffs, t, derivative_order):
        """
        Evaluate a polynomial derivative at time t.
        """

        ac_value = 0.0

        for k in range(derivative_order, len(coeffs)):
            ac_coeff = 1.0

            for j in range(derivative_order):
                ac_coeff *= k - j

            ac_value += ac_coeff * coeffs[k] * t**(k - derivative_order)

        return ac_value

    return ac_eval_poly, ac_poly_coeffs


@app.cell
def _(M, ac_T_inv, ac_Tr, ac_eval_poly, ac_poly_coeffs, ac_v_from_u, l, np):
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        """
        Return a function fun(t) giving:

        x, dx, y, dy, theta, dtheta, z, dz, f, phi

        along an admissible trajectory matching the initial and final states.
        """

        # Convert initial state to h derivatives
        ac_h0, ac_dh0, ac_d2h0, ac_d3h0 = ac_Tr(
            x_0,
            dx_0,
            y_0,
            dy_0,
            theta_0,
            dtheta_0,
            z_0,
            dz_0,
        )

        # Convert final state to h derivatives
        ac_hf, ac_dhf, ac_d2hf, ac_d3hf = ac_Tr(
            x_tf,
            dx_tf,
            y_tf,
            dy_tf,
            theta_tf,
            dtheta_tf,
            z_tf,
            dz_tf,
        )

        # Polynomial coefficients for h_x(t)
        ac_coeffs_x = ac_poly_coeffs(
            ac_h0[0],
            ac_dh0[0],
            ac_d2h0[0],
            ac_d3h0[0],
            ac_hf[0],
            ac_dhf[0],
            ac_d2hf[0],
            ac_d3hf[0],
            tf,
        )

        # Polynomial coefficients for h_y(t)
        ac_coeffs_y = ac_poly_coeffs(
            ac_h0[1],
            ac_dh0[1],
            ac_d2h0[1],
            ac_d3h0[1],
            ac_hf[1],
            ac_dhf[1],
            ac_d2hf[1],
            ac_d3hf[1],
            tf,
        )

        def fun(t):
            # h and its derivatives
            ac_h = np.array([
                ac_eval_poly(ac_coeffs_x, t, 0),
                ac_eval_poly(ac_coeffs_y, t, 0),
            ])

            ac_dh = np.array([
                ac_eval_poly(ac_coeffs_x, t, 1),
                ac_eval_poly(ac_coeffs_y, t, 1),
            ])

            ac_d2h = np.array([
                ac_eval_poly(ac_coeffs_x, t, 2),
                ac_eval_poly(ac_coeffs_y, t, 2),
            ])

            ac_d3h = np.array([
                ac_eval_poly(ac_coeffs_x, t, 3),
                ac_eval_poly(ac_coeffs_y, t, 3),
            ])

            ac_d4h = np.array([
                ac_eval_poly(ac_coeffs_x, t, 4),
                ac_eval_poly(ac_coeffs_y, t, 4),
            ])

            # Recover state variables
            ac_state = ac_T_inv(
                ac_h,
                ac_dh,
                ac_d2h,
                ac_d3h,
            )

            ac_x = ac_state[0]
            ac_dx = ac_state[1]
            ac_y = ac_state[2]
            ac_dy = ac_state[3]
            ac_theta = ac_state[4]
            ac_dtheta = ac_state[5]
            ac_z = ac_state[6]
            ac_dz = ac_state[7]

            # Since h^(4) = u
            ac_u = ac_d4h

            # Compute v from u
            ac_v = ac_v_from_u(
                ac_theta,
                ac_dtheta,
                ac_z,
                ac_dz,
                ac_u,
            )

            ac_v2 = ac_v[1]

            if ac_z == 0:
                raise ValueError("The auxiliary force is undefined because z = 0.")

            # Auxiliary force components
            ac_A = ac_z - (M * l * ac_dtheta**2) / 6
            ac_B = (M * l * ac_v2) / (6 * ac_z)

            ac_alpha = ac_theta - np.pi / 2

            ac_fx = (
                np.cos(ac_alpha) * ac_A
                - np.sin(ac_alpha) * ac_B
            )

            ac_fy = (
                np.sin(ac_alpha) * ac_A
                - np.cos(ac_alpha) * ac_B
            )

            # Recover f and phi from:
            # fx = -f sin(theta + phi)
            # fy =  f cos(theta + phi)

            ac_f = np.sqrt(ac_fx**2 + ac_fy**2)

            ac_phi = np.arctan2(
                -ac_fx,
                ac_fy,
            ) - ac_theta

            # Normalize phi to [-pi, pi]
            ac_phi = (ac_phi + np.pi) % (2 * np.pi) - np.pi

            return np.array([
                ac_x,
                ac_dx,
                ac_y,
                ac_dy,
                ac_theta,
                ac_dtheta,
                ac_z,
                ac_dz,
                ac_f,
                ac_phi,
            ])

        return fun

    return (compute,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Result

    The function `compute(...)` returns a function `fun(t)`.

    For each time \(t\), `fun(t)` returns

    \[
    x,\dot x,y,\dot y,\theta,\dot\theta,z,\dot z,f,\phi.
    \]

    The construction works because the output \(h(t)\) is chosen as a degree 7 polynomial matching

    \[
    h,\dot h,\ddot h,h^{(3)}
    \]

    at both the initial and final times.

    Then the inverse transformation recovers the physical state, and exact linearization gives the force and reactor angle needed to follow the path.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    We now test the function `compute(...)` with the prescribed boundary conditions.

    Initial state:

    \[
    (x_0,\dot x_0,y_0,\dot y_0,\theta_0,\dot\theta_0,z_0,\dot z_0)
    =
    (5,0,20,-1,-\pi/8,0,-Mg,0).
    \]

    Final state:

    \[
    (x_f,\dot x_f,y_f,\dot y_f,\theta_f,\dot\theta_f,z_f,\dot z_f)
    =
    (0,0,2\ell/3,0,0,0,-Mg,0).
    \]

    Final time:

    \[
    t_f=10.
    \]

    We plot the relevant variables and then animate the resulting trajectory.
    """)
    return


@app.cell
def _(M, compute, g, l, np):
    # Graphical Validation

    gv_tf = 10.0

    gv_fun = compute(
        5.0,          # x_0
        0.0,          # dx_0
        20.0,         # y_0
        -1.0,         # dy_0
        -np.pi / 8,   # theta_0
        0.0,          # dtheta_0
        -M * g,       # z_0
        0.0,          # dz_0

        0.0,          # x_tf
        0.0,          # dx_tf
        2 * l / 3,    # y_tf
        0.0,          # dy_tf
        0.0,          # theta_tf
        0.0,          # dtheta_tf
        -M * g,       # z_tf
        0.0,          # dz_tf

        gv_tf,
    )

    gv_t_grid = np.linspace(0.0, gv_tf, 1000)

    # Evaluate the path
    gv_values = np.array([
        gv_fun(gv_t)
        for gv_t in gv_t_grid
    ]).T

    gv_x = gv_values[0]
    gv_dx = gv_values[1]
    gv_y = gv_values[2]
    gv_dy = gv_values[3]
    gv_theta = gv_values[4]
    gv_dtheta = gv_values[5]
    gv_z = gv_values[6]
    gv_dz = gv_values[7]
    gv_f = gv_values[8]
    gv_phi = gv_values[9]

    print("Initial value from computed path:")
    print(gv_fun(0.0))

    print("\nFinal value from computed path:")
    print(gv_fun(gv_tf))

    print("\nMaximum |theta|:", np.max(np.abs(gv_theta)))
    print("Maximum |phi|:", np.max(np.abs(gv_phi)))
    print("Minimum z:", np.min(gv_z))
    print("Minimum f:", np.min(gv_f))
    return (
        gv_dx,
        gv_dy,
        gv_f,
        gv_fun,
        gv_phi,
        gv_t_grid,
        gv_tf,
        gv_theta,
        gv_x,
        gv_y,
    )


@app.cell
def _(gv_dx, gv_dy, gv_f, gv_phi, gv_t_grid, gv_theta, gv_x, gv_y, np, plt):
    def gv_plot_path():
        gv_fig, gv_axes = plt.subplots(5, 1, figsize=(8, 12), sharex=True)

        gv_axes[0].plot(gv_t_grid, gv_x, label=r"$x(t)$")
        gv_axes[0].plot(gv_t_grid, gv_y, label=r"$y(t)$")
        gv_axes[0].set_ylabel("position")
        gv_axes[0].grid(True)
        gv_axes[0].legend()

        gv_axes[1].plot(gv_t_grid, gv_dx, label=r"$\dot{x}(t)$")
        gv_axes[1].plot(gv_t_grid, gv_dy, label=r"$\dot{y}(t)$")
        gv_axes[1].set_ylabel("velocity")
        gv_axes[1].grid(True)
        gv_axes[1].legend()

        gv_axes[2].plot(gv_t_grid, gv_theta, label=r"$\theta(t)$")
        gv_axes[2].axhline(np.pi / 2, color="grey", linestyle="--")
        gv_axes[2].axhline(-np.pi / 2, color="grey", linestyle="--")
        gv_axes[2].set_ylabel(r"$\theta$")
        gv_axes[2].grid(True)
        gv_axes[2].legend()

        gv_axes[3].plot(gv_t_grid, gv_f, label=r"$f(t)$")
        gv_axes[3].set_ylabel("force")
        gv_axes[3].grid(True)
        gv_axes[3].legend()

        gv_axes[4].plot(gv_t_grid, gv_phi, label=r"$\phi(t)$")
        gv_axes[4].axhline(np.pi / 2, color="grey", linestyle="--")
        gv_axes[4].axhline(-np.pi / 2, color="grey", linestyle="--")
        gv_axes[4].set_xlabel("time")
        gv_axes[4].set_ylabel(r"$\phi$")
        gv_axes[4].grid(True)
        gv_axes[4].legend()

        gv_fig.tight_layout()

        return gv_fig


    gv_path_plot = gv_plot_path()
    gv_path_plot
    return


@app.cell
def _(booster_anim, gv_fun, gv_tf, mo, world):
    def gv_animation():
        def gv_anim_x(t):
            return gv_fun(t)[0]

        def gv_anim_y(t):
            return gv_fun(t)[2]

        def gv_anim_theta(t):
            return gv_fun(t)[4]

        def gv_anim_f(t):
            return gv_fun(t)[8]

        def gv_anim_phi(t):
            return gv_fun(t)[9]

        return mo.Html(
            world(
                [-2, 7, -1, 22],
                booster_anim(
                    gv_anim_x,
                    gv_anim_y,
                    gv_anim_theta,
                    gv_anim_f,
                    gv_anim_phi,
                    T=gv_tf,
                ),
            )
        ).center()


    gv_animation()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interpretation

    The graphs show whether the path satisfies the prescribed initial and final conditions.

    We check that:

    \[
    x(0)=5,
    \quad
    y(0)=20,
    \quad
    \theta(0)=-\pi/8,
    \]

    and

    \[
    x(t_f)=0,
    \quad
    y(t_f)=2\ell/3,
    \quad
    \theta(t_f)=0.
    \]

    The variable \(z(t)\) should remain negative because the inversion was derived under the assumption

    \[
    z<0.
    \]

    The plots of \(f(t)\) and \(\phi(t)\) show whether the required force and reactor angle remain reasonable.

    If the trajectory looks too aggressive, or if \(\phi(t)\) becomes too large, the natural fix is to increase \(t_f\). A larger final time gives the booster more time to reach the final state and usually reduces the required control effort.
    """)
    return


if __name__ == "__main__":
    app.run()
