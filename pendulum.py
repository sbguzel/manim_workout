from manim import *
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate

G = 9.8  # acceleration due to gravity, in m/s^2
L = 2.0  # length of pendulum 1 in m
M = 3.0  # mass of pendulum 1 in kg

class Pendulum(Scene):
    def construct(self):
        axes = NumberPlane().set_opacity(0.2)
        self.add(axes)

        def derivs(state, t):
            dydx = np.zeros_like(state)
            dydx[0] = state[1]

            dydx[1] = (-G/L) * state[0]

            return dydx

        # create a time array with dt steps
        dt = 0.1
        t = np.arange(0, 10, dt)

        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        theta = 80.0
        theta_dot = 0.0

        theta_2 = 25.0
        theta_dot_2 = 0.0

        # initial state
        state = np.radians([theta, theta_dot])
        state_2 = np.radians([theta_2, theta_dot_2])

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(derivs, state, t)
        y_2 = integrate.odeint(derivs, state_2, t)

        x1 = L*sin(y[:, 0])
        y1 = -L*cos(y[:, 0])

        x2 = L*sin(y_2[:, 0])
        y2 = -L*cos(y_2[:, 0])

        #Pendulum Motion

        Center = Dot()
        Circle = Dot(radius=0.04*M).move_to(x1[0]*RIGHT+y1[0]*UP).set_color(BLUE)
        Circle_2 = Dot(radius=0.04*M).move_to(x2[0]*RIGHT+y2[0]*UP).set_color(RED)

        Line = self.getline(Center,Circle)
        Line_2 = self.getline(Center,Circle_2)
        self.add(Line, Line_2)
        Line.add_updater(
                        lambda mob: mob.become(
                        self.getline(Center,Circle)
                        ))

        Line_2.add_updater(
                        lambda mob: mob.become(
                        self.getline(Center,Circle_2)
                        ))

        for i in range(len(x1)-1):
            self.play(
                Circle.animate.move_to(x1[i+1]*RIGHT + y1[i+1]*UP),
                Circle_2.animate.move_to(x2[i+1]*RIGHT + y2[i+1]*UP),
                run_time=1/10,rate_func=linear)

    def getline(self,Point1,Point2):
            start_point = Point1.get_center()
            end_point = Point2.get_center()
            line = Line(start_point,end_point).set_stroke(width=2) 
            return line
