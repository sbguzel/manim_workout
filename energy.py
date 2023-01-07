from manim import *
import scipy.integrate as integrate
import numpy as np
from numpy import sin, cos

g = 9.81
L = 2.0
M = 1.0

class Energy(MovingCameraScene):

    def construct(self):
        energy_text = Text("Enerji")
        energy_forms = VGroup(Text("Mekanik"),Text("Kinetik"),Text("Isıl"),Text("Potansiyel"),Text("Nükleer"),Text("Işık"),Text("Kimyasal"),Text("Elektrik"),Text("Ses")).arrange_in_grid(3,3,buff=LARGE_BUFF).scale(0.8).move_to(0.5 * DOWN)
        self.add(energy_text)
        self.wait()
        self.play(energy_text.animate.move_to(2.5 * UP).scale(1.1))
        ul = Underline(energy_text)
        self.wait(0.3)
        self.play(Write(ul), Write(energy_forms), run_time = 2)
        self.wait()
        self.play(energy_forms[1].animate.set_color(RED), energy_forms[3].animate.set_color(BLUE))
        keep = VGroup(energy_forms[1].copy(), energy_forms[3].copy(), energy_forms[0].copy())
        self.add(keep[0], keep[1])
        self.play(Uncreate(energy_text), Uncreate(energy_forms), Uncreate(ul), run_time = 0.5)
        self.wait()
        self.play(keep[0].animate.move_to(DOWN * 2.85), keep[1].animate.move_to(LEFT * 2 + UP * 0.5))
        self.wait()
        axes = NumberPlane().set_opacity(0.2)

        self.play(FadeIn(axes), run_time = 0.3)

        dt = 0.05
        t = np.arange(0, 2.85, dt)

        theta = -80.0
        theta_dot = 0.0
        state = np.radians([theta, theta_dot])

        y = integrate.odeint(self.derivs, state, t)

        px = L*sin(y[:, 0])
        py = -L*cos(y[:, 0])

        Center = Dot()
        Mass = Dot(radius = 0.2).move_to(px[0]*RIGHT + py[0]*UP).set_color(BLUE)
        Rope = self.getline(Center,Mass)
        speed_tracker = ValueTracker()
        time_tracker = ValueTracker()

        speed_text = VGroup(
            Text("Hız =  ").scale(0.5),
            DecimalNumber(
                0,
                num_decimal_places = 1,
                include_sign = False,
            ).scale(0.75),
            Text(" m/s").scale(0.5),
        ).arrange(RIGHT, buff=0.05)

        speed_text.add_updater(
            lambda mob: mob.next_to(Mass, DOWN/2))
        
        speed_text[1].add_updater(
            lambda mob: mob.set_value(speed_tracker.get_value())
        )

        time_text = VGroup(
            Text("t =  ").scale(0.5),
            DecimalNumber(
                0,
                num_decimal_places = 2,
                include_sign = False,
            ).scale(0.75),
            Text(" s").scale(0.5),
        ).arrange(RIGHT, buff=0.05)

        time_text[1].add_updater(
            lambda mob: mob.set_value(time_tracker.get_value())
        )

        self.play(
            Create(Rope),
            Create(Center),
            Create(Mass),
            Create(speed_text),
            Create(time_text.move_to(LEFT * 4.5)),
            run_time = 0.5)
        self.wait()

        Rope.add_updater(
            lambda mob: mob.become(self.getline(Center,Mass))
        )

        mechanical_energy = (L - (L * cos(np.deg2rad(theta)))) * 9.81 * M
        potential_energy = 0
        kinetic_energy = 0

        for i in range(len(px)-1):
            potential_energy = (py[i+1] + L) * 9.81 * M
            kinetic_energy = mechanical_energy - potential_energy
            
            self.play(
                Mass.animate.move_to(px[i+1]*RIGHT + py[i+1]*UP),
                speed_tracker.animate.set_value(np.sqrt(kinetic_energy*2)),
                time_tracker.animate.set_value(i * dt),
                run_time = dt,
                rate_func=linear
            )

        self.wait()

        pot_tracker = ValueTracker()
        kin_tracker = ValueTracker()

        poly1 = SampleSpace(width=3, height=1, stroke_width=5, fill_opacity=0.1)
        pot_text = DecimalNumber()
        poly2 = SampleSpace(width=3, height=1, stroke_width=5, fill_opacity=0.1)
        kin_text = DecimalNumber()
        poly3 = SampleSpace(width=3, height=1, stroke_width=5, fill_opacity=1).set_color(GRAY)
        mec_text = DecimalNumber(mechanical_energy)
        poly_group = VGroup(
            VGroup(poly1,pot_text).arrange(DOWN),
            VGroup(poly2,kin_text).arrange(DOWN),
            VGroup(poly3,mec_text).arrange(DOWN)
            ).arrange()

        pot_text.add_updater(
            lambda mob: mob.set_value(pot_tracker.get_value())
        )

        kin_text.add_updater(
            lambda mob: mob.set_value(kin_tracker.get_value())
        )

        self.play(FadeIn(poly_group.to_edge(UP)), run_time=0.5)


        self.play(
            keep[0].animate.move_to(poly2.get_center()).set_color(WHITE),
            keep[1].animate.move_to(poly1.get_center()).set_color(WHITE),
            Create(keep[2].move_to(poly3.get_center()).set_color(WHITE)),
            run_time = 0.5
            )

        # self.play(self.camera.frame.animate.move_to(1.5 * UP))

        self.wait()

        self.bring_to_front(keep[0])
        self.bring_to_front(keep[1])
        self.bring_to_front(keep[2])

        for i in range(len(px)-1):
            potential_energy = (py[i+1] + L) * 9.81 * M
            kinetic_energy = mechanical_energy - potential_energy
            
            pot_ratio = potential_energy/mechanical_energy
            kin_ratio = kinetic_energy/mechanical_energy

            self.play(
                Mass.animate.move_to(px[i+1]*RIGHT + py[i+1]*UP),
                poly1.animate.divide_vertically(p_list=np.array([pot_ratio, 1-pot_ratio]), colors=[BLUE, BURAK], vect=RIGHT),
                pot_tracker.animate.set_value(potential_energy),
                poly2.animate.divide_vertically(p_list=np.array([kin_ratio, 1-kin_ratio]), colors=[RED, BURAK], vect=RIGHT),
                kin_tracker.animate.set_value(kinetic_energy),
                speed_tracker.animate.set_value(np.sqrt(kinetic_energy*2)),
                time_tracker.animate.set_value(i * dt),
                run_time = dt * 5,
                rate_func=linear
            )

        self.wait()


#########################################################################
    def derivs(self, state, t):
        dydx = np.zeros_like(state)

        dydx[0] = state[1]
        dydx[1] = (-g/L) * state[0]

        return dydx

    def getline(self, Point1,Point2):
        start_point = Point1.get_center()
        end_point = Point2.get_center()
        line = Line(start_point,end_point).set_stroke(width=2) 

        return line



M1 = 3.0
M2 = 1.0
D1 = 0.3
D2 = 0.5
K = 4.0

class System(MovingCameraScene):

    def construct(self):

        dt = 0.05
        t = np.arange(0, 20, dt)

        x_1 = 0.9
        x_2 = 2.0
        x_1_dot = 0.0
        x_2_dot = 0.0
        state = np.array([x_1, x_1_dot, x_2, x_2_dot])
        y = integrate.odeint(self.system, state, t)

        m1x = y[:, 0]
        m2x = y[:, 2]

        m1mob = Square(0.5).set_fill(BLUE, opacity=0.5)
        m2mob = Square(0.5).set_fill(RED, opacity=0.5)

        self.camera.frame.set(width=8).move_to(UP * 1.75)

        self.add(m1mob.move_to(m1x[0]*UP), m2mob.move_to(m2x[0]*UP), NumberPlane().set_opacity(0.3), Line(LEFT,RIGHT).move_to(ORIGIN).set_color(WHITE))
        
        self.play(m1mob.animate.move_to(m1x[0]*UP + UP), m2mob.animate.move_to(m2x[0]*UP + UP), run_time = 1)

        for i in range(len(m1x)-1):
            
            self.play(
                m1mob.animate.move_to(m1x[i+1]*UP + UP),
                m2mob.animate.move_to(m2x[i+1]*UP + UP),
                run_time = dt / 2,
                rate_func=linear
            )

        self.wait()


    def system(self, state, t):
        dydx = np.zeros_like(state)

        dydx[0] = state[1]
        dydx[1] = (-K/M1) * state[0] + (-(D1+D2)/M1) * state[1] + (D2/M1) * state[3]
        dydx[2] = state[3]
        dydx[3] = (D2/M2) * state[1] + (-D2/M2) * state[3]

        return dydx