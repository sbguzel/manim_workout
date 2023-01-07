from manim import *
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate

m = 0.1
k = 1
b = 0.1
f = 0

class MassSpringDamper(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        def derivs(state, t):
            dydx = np.zeros_like(state)

            dydx[0] = state[1]
            dydx[1] = (-k/m) * state[0] - (b/m) * state[1] + (1/m) * f

            return dydx

        dt = 0.1
        t = np.arange(0, 3, dt)

        pos = 3.0
        vel = 0.0

        state = ([pos, vel])

        y = integrate.odeint(derivs, state, t)

        px = y[:, 0]
        v = y[:, 1]

        text, number = label = VGroup(
            Text("Speed = "),
            DecimalNumber(
                v[0],
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        square = Square().move_to(px[0]*RIGHT + RIGHT).set_color(BLUE)
        
        s_arrow = Arrow(px[0]*RIGHT,v[0]*0.5*RIGHT)

        self.add(square, label.move_to(2 * UP),s_arrow)

        tracker = ValueTracker(v[0])

        number.add_updater(lambda d: d.set_value(tracker.get_value()))

        curve = VGroup()
        curve.add(Line(np.array([0,0,0]),np.array([0,0,0])))

        def get_curve():
            last_line = curve[-1]
            x = i/10
            y = px[i+1] / 5
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            curve.add(new_line)

            return curve

    
        for i in range(len(px)-1):
            sine_curve_line = always_redraw(get_curve)          
            self.add(sine_curve_line)
            self.play(
                AnimationGroup(
                    square.animate.move_to(px[i]*RIGHT + RIGHT),
                    ApplyMethod(s_arrow.put_start_and_end_on,px[i]*RIGHT,v[i]*0.5*RIGHT),
                    tracker.animate.set_value(float(v[i])),
                    run_time=1/10,
                    rate_func=linear,
                    lag_ratio=0
                )
                )
        
