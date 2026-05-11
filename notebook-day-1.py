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

    return np, plt, sci


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g= 1.0  #gravity constant, m/s^2
    M= 1.0 # booster mass , kg
    l = 2.0 # total booster lentgh, meters
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(np):
    def force_components(f, theta, phi):
        """
        Compute the cartesian components of the reactor thrust force.

        Parameters:
            f     : thrust magnitude (>= 0)
            theta : booster tilt angle (rad, CCW from vertical)
            phi   : thrust deflection angle relative to booster axis (rad, CCW)

        Returns:
            fx, fy: force components in world coordinates

        Physics:
            The total thrust direction in world coordinates is (theta + phi).
            We decompose this into x and y using trigonometry:
              - x-component points left when sin is positive (hence the negative sign)
              - y-component points upward when cos is positive
        """
        # Total angle of thrust vector measured from vertical (world y-axis)
        # x-component: negative because theta>0 (left tilt) should push leftward
        fx= -f * np.sin(theta + phi)
        # y-component: positive upward thrust
        fy= f * np.cos(theta + phi)
        return fx, fy

    return (force_components,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(M, force_components, g):
    def center_of_mass_acceleration(f, theta, phi):
        """
        Compute the linear acceleration of the booster's center of mass.

        Parameters:
            f     : thrust magnitude
            theta : booster tilt angle (rad)
            phi   : thrust deflection angle (rad)

        Returns:
            x_ddot, y_ddot: acceleration components (m/s^2)

        Physics:
            Newton's second law: F = M * a  =>  a = F / M
            - Horizontal acceleration comes entirely from thrust
            - Vertical acceleration = thrust/M - gravity (g acts downward)
        """
        # Get thrust components in world coordinates
        fx, fy= force_components(f, theta, phi)

        # Horizontal acceleration: a_x = F_x / M
        x_ddot=fx/M
        # Vertical acceleration: a_y = F_y / M - g
        # (gravity g pulls downward, reducing net upward acceleration)
        y_ddot= fy/M - g
        return x_ddot, y_ddot

    return (center_of_mass_acceleration,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 /12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell
def _(J, l, np):
    def angular_acceleration(f, phi):
        """
        Compute the angular acceleration (theta_ddot) of the booster.

        Parameters:
            f   : thrust magnitude
            phi : thrust deflection angle relative to booster axis (rad)

        Returns:
            theta_ddot: angular acceleration (rad/s^2)

        Physics:
            Torque = force * lever_arm * sin(angle_between_them)
            - The reactor is at the base, lever arm = l/2 from COM
            - Only the perpendicular component of thrust creates torque
            - Torque = -(l/2) * f * sin(phi)  [negative for CCW convention]
            - theta_ddot = Torque / J  (moment of inertia)
        """
        # Torque about COM: lever arm (l/2) × perpendicular thrust component f*sin(phi)
        # Negative sign enforces the correct CCW rotation convention
        # Angular acceleration = Torque / Moment of Inertia
        theta_ddot = - ((l/2)*f/J)*np.sin(phi)
        return theta_ddot

    return (angular_acceleration,)


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


@app.cell
def _(angular_acceleration, center_of_mass_acceleration, np):
    # Dimension of the state space:
    # s = [x, vx, y, vy, theta, omega]
    n = 6

    def F(s, f, phi):
        """
        Compute the time derivative of the state vector (the vector field).

        Parameters:
            s   : state vector [x, vx, y, vy, theta, omega]
            f   : thrust magnitude (control input)
            phi : thrust angle (control input)

        Returns:
            s_dot : time derivative ds/dt = [x_dot, vx_dot, y_dot, vy_dot,
                                             theta_dot, omega_dot]

        State space (n=6 dimensions):
            x     : horizontal position of COM
            vx    : horizontal velocity (x_dot)
            y     : vertical position of COM
            vy    : vertical velocity (y_dot)
            theta : tilt angle (CCW from vertical)
            omega : angular velocity (theta_dot)
        """
        # Unpack the state vector for readability
        x, vx, y, vy, theta, omega = s

        # --- Kinematic equations (by definition) ---

        # Position derivatives equal velocities
        x_dot = vx        # dx/dt = v_x

        # Linear accelerations from forces (translation dynamics)
        # center_of_mass_acceleration applies F=ma with gravity
        vx_dot, vy_dot = center_of_mass_acceleration(f, theta, phi)

        # Position derivatives equal velocities
        y_dot = vy        # dy/dt = v_y

        # Angle derivative equals angular velocity
        theta_dot = omega  # d(theta)/dt = omega

        # --- Dynamic equations (from Newton-Euler) ---

        # Angular acceleration from torque (rotation dynamics)
        # angular_acceleration applies torque = I * alpha
        omega_dot = angular_acceleration(f, phi)

        # Assemble and return the full state derivative vector
        # Order must match state vector: [x, vx, y, vy, theta, omega]
        return np.array([
            x_dot,      # dx/dt
            vx_dot,     # d(vx)/dt
            y_dot,      # dy/dt
            vy_dot,     # d(vy)/dt
            theta_dot,  # d(theta)/dt
            omega_dot,  # d(omega)/dt
        ])

    return (F,)


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


@app.cell
def _(F, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):

        def rhs(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        def ground_hit(t, y):
            return y[2] - l / 2

        ground_hit.terminal  = True
        ground_hit.direction = -1

        result = sci.solve_ivp(
            rhs, t_span, y0,
            dense_output=True,
            events=ground_hit,
        )

        if not result.success:
            raise RuntimeError(result.message)

        if result.t_events[0].size > 0:
            t_land = result.t_events[0][0]
            _raw   = result.sol
            def sol(t):
                scalar = np.ndim(t) == 0
                t_arr  = np.atleast_1d(np.asarray(t, dtype=float))
                out    = _raw(np.minimum(t_arr, t_land))
                if scalar:
                    return out[:, 0]
                return out
            return sol

        return result.sol

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


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]

        # [x, vx, y, vy, theta, omega]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        # No thrust, no tilt
        def f_phi(t, y):
            return np.array([0.0, 0.0])

        # Solve the dynamics
        sol = redstart_solve(t_span, y0, f_phi)

        # Time samples for plotting
        t = np.linspace(t_span[0], t_span[1], 1000)

        # y(t) is the 3rd state variable
        y_t = sol(t)[2]

        # Plot the trajectory
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")

        # Reference line y = l
        plt.plot(
            t,
            l * np.ones_like(t),
            color="grey",
            ls="--",
            label=r"$y=\ell$",
        )

        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.ylabel("height")
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


@app.cell
def _(M, g):
    T = 5.0

    # Desired landing trajectory
    def y_landing(t):
        return 10 - 2*t - (7/25)*t**2 + (8/125)*t**3

    # Vertical velocity
    def vy_landing(t):
        return -2 - (14/25)*t + (24/125)*t**2

    # Vertical acceleration
    def ay_landing(t):
        return -(14/25) + (48/125)*t

    # Required thrust
    def f_landing(t):
        return M * (ay_landing(t) + g)

    return T, f_landing


@app.cell
def _(T, f_landing, l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, T]

        # [x, vx, y, vy, theta, omega]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        # Force along the booster axis: phi = 0
        def f_phi(t, y):
            return np.array([f_landing(t), 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0.0, T, 1000)
        states = sol(t)

        y_t = states[2]
        vy_t = states[3]

        plt.plot(t, y_t, label=r"$y(t)$")
        plt.plot(t, l/2 * np.ones_like(t), "--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing: Height")
        plt.xlabel("time $t$")
        plt.ylabel("height")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.plot(t, vy_t, label=r"$\dot y(t)$")
        plt.plot(t, np.zeros_like(t), "--", label=r"$\dot y=0$")
        plt.title("Controlled Landing: Vertical Velocity")
        plt.xlabel("time $t$")
        plt.ylabel("vertical velocity")
        plt.grid(True)
        plt.legend()
        plt.show()

        final_state = sol(T)
        print("Final state:", final_state)

        return final_state

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


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        width  = x_max - x_min
        height = y_max - y_min

        return svg.svg(
            viewBox=f"0 0 {width} {height}",
            xmlns="http://www.w3.org/2000/svg",
        )(
            # Flip y-axis so y increases upward (SVG default is downward)
            transform.translate(x=-x_min, y=y_max)(
                transform.scale(x=1, y=-1)(
                    # Sky background
                    svg.rect(x=x_min, y=0,     width=width, height=y_max,  fill="lightblue"),
                    # Ground
                    svg.rect(x=x_min, y=y_min, width=width, height=-y_min, fill="tan"),
                    # Landing pad: 2m wide, centered at x=0, sitting on y=0
                    svg.rect(x=-1,    y=-0.1,  width=2,     height=0.1,    fill="green"),
                    # Any extra objects passed by the caller
                    *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    # Three test scenes: empty world, black square on pad, colored squares in corners
    mo.hstack([
        mo.Html(world([-3, 3, -2, 4])),
        mo.Html(world([-3, 3, -2, 4], svg.rect(x=-1, y=0, width=2, height=2, fill="black"))),
        mo.Html(world([-3, 3, -2, 4],
            svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
            svg.rect(x=1,  y=2, width=2, height=2, fill="blue"),
        )),
    ], justify="space-around")

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


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        body_width  = 0.16
        flame_width = 0.12
        # Flame length proportional to thrust: equals l/2 when f = Mg
        flame_len   = (l / 2) * max(0.0, f / (M * g))

        # Booster body: rectangle centered on the center of mass
        body = svg.rect(
            x=-body_width / 2, y=-l / 2,
            width=body_width,  height=l,
            rx=0.03, fill="black",
        )

        # Flame: attached at the base of the booster, rotated by phi relative to booster axis
        flame = transform.translate(y=-l / 2)(
            transform.rotate(a=np.degrees(phi))(
                svg.rect(
                    x=-flame_width / 2, y=-flame_len,
                    width=flame_width,  height=flame_len,
                    fill="orangered",
                )
            )
        )

        # Place and tilt the whole booster at position (x, y) with angle theta
        return transform.translate(x=x, y=y)(
            transform.rotate(a=np.degrees(theta))(
                flame, body,
            )
        )

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    # Left: booster at rest with no thrust
    # Middle: booster with thrust f=Mg along its axis
    # Right: booster tilted 45°, thrust 2Mg, nozzle rotated 90°
    mo.hstack([
        mo.Html(world([-3, 3, -2, 4], booster(0, l/2, 0, 0, 0))),
        mo.Html(world([-3, 3, -2, 4], booster(0, l, 0, M*g, 0))),
        mo.Html(world([-3, 3, -2, 4], booster(-l/2, l, np.pi/4, 2*M*g, np.pi/2))),
    ], justify="space-around")
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


@app.cell
def _(M, animate_transform, g, l, np, svg, transform):
    def booster_anim(x, y, theta, f, phi, T):
        body_width  = 0.16
        flame_width = 0.12

        # Static booster body rectangle centered on center of mass
        body = svg.rect(
            x=-body_width / 2, y=-l / 2,
            width=body_width,  height=l,
            rx=0.03, fill="black",
        )

        # Animated flame: nozzle angle and length both change over time
        flame = transform.translate(y=-l / 2)(
            # Rotate flame by phi(t) relative to booster axis
            animate_transform.rotate(a=lambda t: np.degrees(phi(t)), T=T)(
                # Scale flame height proportionally to thrust f(t)
                animate_transform.scale(
                    x=1.0,
                    y=lambda t: max(0.0, f(t) / (M * g)),
                    T=T,
                )(
                    svg.rect(
                        x=-flame_width / 2, y=-l / 2,
                        width=flame_width,  height=l / 2,
                        fill="orangered",
                    )
                )
            )
        )

        # Animate position (x(t), y(t)) and tilt angle theta(t) of the whole booster
        return animate_transform.translate(x=x, y=y, T=T)(
            animate_transform.rotate(a=lambda t: np.degrees(theta(t)), T=T)(
                flame, body,
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    # Test: booster moves across the screen while spinning and increasing thrust over 5s
    def booster_anim_0():
        T = 5.0
        def x(t):     return -l/2 + l * (t / T)
        def y(t):     return l/2  + l/2 * (t / T)
        def theta(t): return (t / T) * 2 * np.pi
        def f(t):     return M * g * (t / T)
        def phi(t):   return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(world([-3, 3, -2, 4], booster_anim_0())).center()
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


@app.cell
def _(booster_anim, mo, redstart_solve, world):
    def animated_simulation(t_span, y0, f_phi, view_box=[-3, 3, -2, 12]):
        # Solve the ODE for the given scenario
        sol = redstart_solve(t_span, y0, f_phi)
        T   = t_span[1] - t_span[0]

        # Extract each state variable and input as a function of time for the animator
        def x(t):     return sol(t)[0]
        def y(t):     return sol(t)[2]
        def theta(t): return sol(t)[4]
        def f(t):     return f_phi(t, sol(t))[0]
        def phi(t):   return f_phi(t, sol(t))[1]

        return mo.Html(world(view_box, booster_anim(x, y, theta, f, phi, T=T)))

    return (animated_simulation,)


@app.cell
def _(animated_simulation, np):
    # No thrust, no tilt: booster falls freely under gravity and stops when it hits the ground
    def f_phi_1(t, y): return np.array([0.0, 0.0])
    animated_simulation([0.0, 5.0], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], f_phi_1)
    return


@app.cell
def _(M, animated_simulation, g, np):
    # Thrust exactly equals gravity (f = Mg): booster hovers in place without moving
    def f_phi_2(t, y): return np.array([M * g, 0.0])
    animated_simulation([0.0, 5.0], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], f_phi_2)
    return


@app.cell
def _(M, animated_simulation, g, np):
    # Thrust f = Mg but nozzle angled at pi/8: booster drifts sideways while falling
    def f_phi_3(t, y): return np.array([M * g, np.pi / 8])
    animated_simulation([0.0, 5.0], [0.0, 0.0, 10.0, 0.0, 0.0, 0.0], f_phi_3)
    return


@app.cell
def _(T, animated_simulation, f_landing, np):
    # Controlled landing: time-varying thrust along the booster axis brings
    # the booster smoothly to rest at ground level at t = 5s
    def f_phi_4(t, y): return np.array([f_landing(t), 0.0])
    animated_simulation([0.0, T], [0.0, 0.0, 10.0, -2.0, 0.0, 0.0], f_phi_4,
                        view_box=[-3, 3, -1, 12])
    return


if __name__ == "__main__":
    app.run()
