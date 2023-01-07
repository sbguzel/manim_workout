from manim import *

class CreateCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(WHITE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI/2), Rotate(right_square, angle=PI/2), run_time=2
        )
        self.wait()

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)

        self.play(
            triangle.animate.set_stroke(color=GREEN, width=20),  run_time=2
        )

        self.wait(1)


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 5), run_time=4, rate_func=linear)

        self.wait()

class MobjectExample(Scene):
    def construct(self):
        p1= [-1,-1,0]
        p2= [1,-1,0]
        p3= [1,1,0]
        p4= [-1,1,0]
        a = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start= a.get_start()
        point_end  = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a= Square().set_color(BLUE).shift(RIGHT)
        m2b= Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)


class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(blue_circle)
        self.play(ReplacementTransform(blue_circle, orange_square, run_time=2))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(orange_square, UP))
        self.play(Create(small_dot))
        self.play(orange_square.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(orange_square))


class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)

class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)

class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorldd", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)

class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144).move_to(LEFT)
        tex2 = Tex('\\LaTeX').next_to(tex);
        self.add(tex, tex2)

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$}",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) = &3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)

class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start, dissipating_time=0.5, stroke_opacity=[0, 1])
        rolling_circle.add_updater(lambda m: m.rotate(-0.2))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)

class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.2, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.wait()
        
class Deneme(Scene):
    def construct(self):
        small_dot = Dot()
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.2, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.play(ReplacementTransform(a, orange_square, run_time=2))
        small_dot.add_updater(lambda mob: mob.next_to(orange_square, UP))
        self.play(Create(small_dot))
        self.play(orange_square.animate.shift(RIGHT))
        self.play(orange_square.animate.rotate(PI / 4))  # rotate the square
        self.wait()

class LaggedStartExample(Scene):
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP * 2,
            end=LEFT + DOWN * 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT * 4),
            dot2.animate.shift(RIGHT * 4),
            dot3.animate.shift(RIGHT * 4),
            lag_ratio=0.25,
            run_time=4
        ))

class LaggedStartMapExample(Scene):
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            *[Dot(radius=0.16) for _ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 5
            ))

class SuccessionExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeIn with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeIn(tex[0]),
            FadeIn(tex[1], shift=DOWN),
            FadeIn(tex[2], target_position=dot),
            FadeIn(tex[3], scale=1.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

class Growing(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(triangle, DOWN))
        self.play(GrowArrow(arrow))
        self.play(SpinInFromNothing(star))

class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))

class GrowFromEdgeExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.play(GrowFromEdge(squares[0], DOWN))
        self.play(GrowFromEdge(squares[1], RIGHT))
        self.play(GrowFromEdge(squares[2], UR))
        self.play(GrowFromEdge(squares[3], UP, point_color=RED))

class GrowFromPointExample(Scene):
    def construct(self):
        dot = Dot(3 * UR, color=GREEN)
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.add(dot)
        self.play(GrowFromPoint(squares[0], ORIGIN))
        self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
        self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
        self.play(GrowFromPoint(squares[3], dot, dot.get_color()))

class SpinInFromNothingExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(3)]
        VGroup(*squares).set_x(0).arrange(buff=2)
        self.play(SpinInFromNothing(squares[0]))
        self.play(SpinInFromNothing(squares[1], angle=2 * PI))
        self.play(SpinInFromNothing(squares[2], point_color=RED))

class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))

class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("WaveWaveWaveWaveWave").scale(2)
        self.play(ApplyWave(tex))
        self.play(ApplyWave(
            tex,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))
        self.play(ApplyWave(
            tex,
            rate_func=linear,
            ripples=4
        ))

class UsingCircumscribe(Scene):
    def construct(self):
        lbl = Tex(r"Circum-\\scribe").scale(2)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))

class FlashOnCircle(Scene):
    def construct(self):
        radius = 2
        circle = Circle(radius)
        self.add(circle)
        self.play(Flash(
            circle, line_length=1,
            num_lines=30, color=RED,
            flash_radius=radius+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))

class UsingIndicate(Scene):
    def construct(self):
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
        self.wait()

class TimeWidthValues(Scene):
    def construct(self):
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))

class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("Wiggle").scale(3)
        self.play(Wiggle(tex))
        self.wait()

class Homotopy_Animation(Scene):
    def construct(self):
        circle = Circle(2)
        def homotopy(x, y, z, t):
            return (x - 2*t, y ,z)
        self.add(circle)
        self.play(Homotopy(homotopy=homotopy, mobject=circle), run_time = 3)
        self.wait()

class MoveAlongPathExample(Scene):
    def construct(self):
        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)

class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )

class BroadcastExample(Scene):
    def construct(self):
        mob = Square(color=TEAL_A)
        self.play(Broadcast(mob))

class SpeedModifierExample(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        b = Dot().shift(RIGHT * 4)
        self.add(a, b)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    a.animate(run_time=1).shift(RIGHT * 8),
                    b.animate(run_time=1).shift(LEFT * 8),
                ),
                speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1},
                rate_func=linear,
            )
        )

class SpeedModifierUpdaterExample(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.play(
            ChangeSpeed(
                Wait(2),
                speedinfo={0.4: 1, 0.5: 0.2, 0.8: 0.2, 1: 1},
                affects_speed_updaters=True,
            )
        )

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()

class CounterclockwiseTransform_vs_Transform(Scene):
    def construct(self):
        # set up the numbers
        c_transform = VGroup(DecimalNumber(number=3.141, num_decimal_places=3), DecimalNumber(number=1.618, num_decimal_places=3))
        text_1 = Text("CounterclockwiseTransform", color=RED)
        c_transform.add(text_1)

        transform = VGroup(DecimalNumber(number=1.618, num_decimal_places=3), DecimalNumber(number=3.141, num_decimal_places=3))
        text_2 = Text("Transform", color=BLUE)
        transform.add(text_2)

        ints = VGroup(c_transform, transform)
        texts = VGroup(text_1, text_2).scale(0.75)
        c_transform.arrange(direction=UP, buff=1)
        transform.arrange(direction=UP, buff=1)

        ints.arrange(buff=2)
        self.add(ints, texts)

        # The mobs move in clockwise direction for ClockwiseTransform()
        self.play(CounterclockwiseTransform(c_transform[0], c_transform[1]))

        # The mobs move straight up for Transform()
        self.play(Transform(transform[0], transform[1]))

class CyclicReplaceExample(Scene):
    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(), Star())
        group.arrange(RIGHT)
        self.add(group)

        for _ in range(4):
            self.play(CyclicReplace(*group))

class FadeToColorExample(Scene):
    def construct(self):
        self.play(FadeToColor(Text("Hello World!"), color=RED))

class DifferentFadeTransforms(Scene):
    def construct(self):
        starts = [Rectangle(width=4, height=1) for _ in range(3)]
        VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
        targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
        VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

        self.play(*[FadeIn(s) for s in starts])
        self.play(
            FadeTransform(starts[0], targets[0], stretch=True),
            FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
            FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
        )

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

class MoveToTargetExample(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)

        self.add(c)
        self.play(MoveToTarget(c))

class ReplacementTransformOrTransform(Scene):
    def construct(self):
        # set up the numbers
        r_transform = VGroup(*[Integer(i) for i in range(1,4)])
        text_1 = Text("ReplacementTransform", color=RED)
        r_transform.add(text_1)

        transform = VGroup(*[Integer(i) for i in range(4,7)])
        text_2 = Text("Transform", color=BLUE)
        transform.add(text_2)

        ints = VGroup(r_transform, transform)
        texts = VGroup(text_1, text_2).scale(0.75)
        r_transform.arrange(direction=UP, buff=1)
        transform.arrange(direction=UP, buff=1)

        ints.arrange(buff=2)
        self.add(ints, texts)

        # The mobs replace each other and none are left behind
        self.play(ReplacementTransform(r_transform[0], r_transform[1]))
        self.play(ReplacementTransform(r_transform[1], r_transform[2]))

        # The mobs linger after the Transform()
        self.play(Transform(transform[0], transform[1]))
        self.play(Transform(transform[1], transform[2]))
        self.wait()

class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

class ScaleInPlaceExample(Scene):
    def construct(self):
        self.play(ScaleInPlace(Text("Hello World!"), 2))

class ShrinkToCenterExample(Scene):
    def construct(self):
        self.play(ShrinkToCenter(Text("Hello World!")))

class Anagram(Scene):
    def construct(self):
        src = Text("the morse code")
        tar = Text("here come dots")
        self.play(Write(src))
        self.wait(0.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait(0.5)

class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)

class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))

class AnnularSectorExample(Scene):
    def construct(self):
        # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
        s1 = AnnularSector(color=YELLOW).move_to(2 * UL)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 * DEGREES, color=RED).move_to(2 * UR)

        # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
        s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 * DL)

        # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
        s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 * PI / 2, color=GREEN).move_to(2 * DR)

        annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)

        annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).next_to(annulus_1, DOWN)

        self.add(s1, s2, s3, s4, annulus_1, annulus_2)

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))

class SeveralArcPolygons(Scene):
    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    arc_config=[{'radius': 1.7, 'color': RED},
                                    {'angle': 20*DEGREES, 'color': BLUE},
                                    {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()

class ArcPolygonExample2(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
            "fill_opacity": 0.5, "color": GREEN}
        poly_conf = {"color": None}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)

class CircleFromPointsExample(Scene):
    def construct(self):
        circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
        dots = VGroup(
            Dot(LEFT),
            Dot(LEFT + UP),
            Dot(UP * 2),
        )
        self.add(NumberPlane(), circle, dots)

        circle2 = Circle.from_three_points(3 * LEFT, LEFT + UP, UP * 2, color=RED)
        dots2 = VGroup(
            Dot(3 * LEFT),
            Dot(LEFT + UP),
            Dot(UP * 2),
        )
        self.play(Transform(dots, dots2))
        self.play(Transform(circle, circle2))

class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270*DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)

class CircleSurround(Scene):
    def construct(self):
        triangle1 = Triangle()
        circle1 = Circle().surround(triangle1)
        group1 = Group(triangle1,circle1) # treat the two mobjects as one

        line2 = Line()
        circle2 = Circle().surround(line2, buffer_factor=2.0)
        group2 = Group(line2,circle2)

        # buffer_factor < 1, so the circle is smaller than the square
        square3 = Square()
        circle3 = Circle().surround(square3, buffer_factor=0.5)
        group3 = Group(square3, circle3)

        group = Group(group1, group2, group3).arrange(buff=1)
        self.add(group)

class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b).set_color(YELLOW)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(l1, d1, l2, d2, bezier)

class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        self.add(ellipse_group)

class SeveralLabeledDots(Scene):
    def construct(self):
        sq = Square(fill_color=RED, fill_opacity=1)
        self.add(sq)
        dot1 = LabeledDot(Tex("42", color=RED))
        dot2 = LabeledDot(MathTex("a", color=GREEN))
        dot3 = LabeledDot(Text("ii", color=BLUE))
        dot4 = LabeledDot("3")
        dot1.next_to(sq, UL)
        dot2.next_to(sq, UR)
        dot3.next_to(sq, DL)
        dot4.next_to(sq, DR)
        self.add(dot1, dot2, dot3, dot4)

class ExampleSector(Scene):
    def construct(self):
        sector = Sector(outer_radius=2, inner_radius=1)
        sector2 = Sector(outer_radius=2.5, inner_radius=0.8).move_to([-3, 0, 0])
        sector.set_color(RED)
        sector2.set_color(PINK)
        self.add(sector, sector2)

class DifferenceExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Difference(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0, 0])
        self.add(sq, cr, un)

class ExclusionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0.4, 0])
        self.add(sq, cr, un)

class IntersectionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0, 0])
        self.add(sq, cr, un)

class UnionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Union(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0.3, 0])
        self.add(sq, cr, un)

class AngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN )
        line2 = Line( DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT )
        angles = [
            Angle(line1, line2, dot=True),
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), other_angle=True),
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, other_angle=True),
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED),
            Angle(line1, line2, other_angle=True),
            Angle(line1, line2, radius=0.4, quadrant=(1,-1)),
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8),
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, other_angle=True),
        ]
        plots = VGroup()
        for angle in angles:
            plot=VGroup(line1.copy(),line2.copy(), angle)
            plots.add(VGroup(plot,SurroundingRectangle(plot, buff=0.3)))
        plots.arrange_in_grid(rows=2,buff=1)
        self.add(plots)

class GetValueExample(Scene):
    def construct(self):
        line1 = Line(LEFT+(1/3)*UP, RIGHT+(1/3)*DOWN)
        line2 = Line(DOWN+(1/3)*RIGHT, UP+(1/3)*LEFT)

        angle = Angle(line1, line2, radius=0.4)

        value = DecimalNumber(angle.get_value(degrees=True), unit="^{\circ}")
        value.next_to(angle, UR)

        self.add(line1, line2, angle, value)

class FilledAngle(Scene):
    def construct(self):
        l1 = Line(ORIGIN, 2 * UP + RIGHT).set_color(GREEN)
        l2 = (
            Line(ORIGIN, 2 * UP + RIGHT)
            .set_color(GREEN)
            .rotate(-20 * DEGREES, about_point=ORIGIN)
        )
        norm = l1.get_length()
        a1 = Angle(l1, l2, other_angle=True, radius=norm - 0.5).set_color(GREEN)
        a2 = Angle(l1, l2, other_angle=True, radius=norm).set_color(GREEN)
        q1 = a1.points #  save all coordinates of points of angle a1
        q2 = a2.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)])  # adds points and ensures that path starts and ends at same point
        mfill = VMobject().set_color(ORANGE)
        mfill.set_points_as_corners(pnts).set_fill(GREEN, opacity=1)
        self.add(l1, l2)
        self.add(mfill)

class ArrowExample(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)

        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        self.add(Group(g1, g2, g3).arrange(buff=2))

class ArrowExample(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)

class DashedLineExample(Scene):
    def construct(self):
        # dash_length increased
        dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
        # normal
        dashed_2 = DashedLine(config.left_side, config.right_side)
        # dashed_ratio decreased
        dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
        self.add(dashed_1, dashed_2, dashed_3)

class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        group = Group(circle, d_arrow).arrange(UP, buff=1)
        self.add(group)

class ElbowExample(Scene):
    def construct(self):
        elbow_1 = Elbow()
        elbow_2 = Elbow(width=2.0)
        elbow_3 = Elbow(width=2.0, angle=5*PI/4)

        elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
        self.add(elbow_group)

class LineExample(Scene):
    def construct(self):
        d = VGroup()
        for i in range(0,10):
            d.add(Dot())
        d.arrange_in_grid(buff=1)
        self.add(d)
        l= Line(d[0], d[1])
        self.add(l)
        self.wait()
        l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
        self.wait()
        l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
        self.wait()

class RightAngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT, RIGHT )
        line2 = Line( DOWN, UP )
        rightangles = [
            RightAngle(line1, line2),
            RightAngle(line1, line2, length=0.4, quadrant=(1,-1)),
            RightAngle(line1, line2, length=0.5, quadrant=(-1,1), stroke_width=8),
            RightAngle(line1, line2, length=0.7, quadrant=(-1,-1), color=RED),
        ]
        plots = VGroup()
        for rightangle in rightangles:
            plot=VGroup(line1.copy(),line2.copy(), rightangle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)

class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
        line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
        self.add(circle, line_1, line_2)

class VectorCoordinateLabel(Scene):
    def construct(self):
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2])
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)

        self.add(plane, vec_1, vec_2, label_1, label_2)

class CutoutExample(Scene):
    def construct(self):
        s1 = Square().scale(2.5)
        s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
        s3 = Square().shift(UP + RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
        s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
        self.play(Write(c), run_time=4)
        self.wait()

class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)

class PolygramExample(Scene):
    def construct(self):
        hexagram = Polygram(
            [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
            [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
        )
        self.add(hexagram)

        dot = Dot()
        self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
        self.remove(dot)
        self.wait()

class PolygramRoundCorners(Scene):
    def construct(self):
        star = Star(outer_radius=2)

        shapes = VGroup(star)
        shapes.add(star.copy().round_corners(radius=0.1))
        shapes.add(star.copy().round_corners(radius=0.25))

        shapes.arrange(RIGHT)
        self.add(shapes)

class RectangleExample(Scene):
    def construct(self):
        rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
        rect2 = Rectangle(width=1.0, height=4.0)

        rects = Group(rect1,rect2).arrange(buff=1)
        self.add(rects)

class RegularPolygonExample(Scene):
    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)

class RegularPolygramExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        self.add(pentagram)

class RoundedRectangleExample(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)

class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)

class StarExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        star = Star(outer_radius=2, color=RED)

        self.add(pentagram)
        self.play(Create(star), run_time=3)
        self.play(FadeOut(star), run_time=2)

class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)

class SurroundingRectExample(Scene):
    def construct(self):
        title = Title("A Quote from Newton")
        quote = Text(
            "If I have seen further than others, \n"
            "it is by standing upon the shoulders of giants.",
            color=BLUE,
        ).scale(0.75)
        box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

        t2 = Tex(r"Hello World").scale(1.5)
        box2 = SurroundingRectangle(t2, corner_radius=0.2)
        mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
        self.add(title, mobjects)

class UnderLine(Scene):
    def construct(self):
        man = Tex("Manim")  # Full Word
        ul = Underline(man)  # Underlining the word
        self.add(man, ul)

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.add(ax, graph)

class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2,2,0), color=RED)

        self.add(plane, dot_scene, ax, dot_axes, lines)

class LineGraphExample(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (0, 7),
            y_range = (0, 5),
            x_length = 7,
            axis_config={"include_numbers": True},
        )
        plane.center()
        line_graph = plane.plot_line_graph(
            x_values = [0, 1.5, 2, 2.8, 4, 6.25],
            y_values = [1, 3, 2.25, 4, 2.5, 1.75],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        self.add(plane, line_graph)

class PointToCoordsExample(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 2]).add_coordinates()
        circ = Circle(radius=0.5).shift(UR * 2)

        # get the coordinates of the circle with respect to the axes
        coords = np.around(ax.point_to_coords(circ.get_right()), decimals=2)

        label = (
            Matrix([[coords[0]], [coords[1]]]).scale(0.75).next_to(circ, RIGHT)
        )

        self.add(ax, circ, label, Dot(circ.get_right()))

class ComplexPlaneExample(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        label1 = MathTex("2+i").next_to(d1, UR, 0.1)
        label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
        self.add(
            d1,
            label1,
            d2,
            label2,
        )

class CoordSysExample(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 1, 0.05],  # step size determines num_decimal_places.
            y_range=[0, 1, 0.05],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.1, 0.1),
                "font_size": 24,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        graphs = VGroup()
        for n in np.arange(1, 20 + 0.5, 0.5):
            graphs += grid.plot(lambda x: x ** n, color=WHITE)
            graphs += grid.plot(
                lambda x: x ** (1 / n), color=WHITE, use_smoothing=False
            )

        # Extra lines and labels for point (1,1)
        graphs += grid.get_horizontal_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += grid.get_vertical_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += Dot(point=grid.c2p(1, 1, 0), color=YELLOW)
        graphs += Tex("(1,1)").scale(0.75).next_to(grid.c2p(1, 1, 0))
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Graphs of $y=x^{ {1}\over{n} }$ and $y=x^n (n=1,2,3,...,20)$",
            include_underline=False,
            font_size=40,
        )

        self.add(title, graphs, grid, grid_labels)

class TLabelExample(Scene):
    def construct(self):
        # defines the axes and linear function
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], x_length=9, y_length=6)
        func = axes.plot(lambda x: x, color=BLUE)
        # creates the T_label
        t_label = axes.get_T_label(x_val=4, graph=func, label=Tex("x-value"))
        self.add(axes, func, t_label)

class GetAreaExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        curve = ax.plot(lambda x: 2 * np.sin(x), color=DARK_BLUE)
        area = ax.get_area(
            curve,
            x_range=(PI / 2, 3 * PI / 2),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )

        self.add(ax, curve, area)

class GetGraphLabelExample(Scene):
    def construct(self):
        ax = Axes()
        sin = ax.plot(lambda x: np.sin(x), color=PURPLE_B)
        label = ax.get_graph_label(
            graph=sin,
            label= MathTex(r"\frac{\pi}{2}"),
            x_val=PI / 2,
            dot=True,
            direction=UR,
        )

        self.add(ax, sin, label)

class GetHorizontalLineExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        point = ax.c2p(-4, 1.5)

        dot = Dot(point)
        line = ax.get_horizontal_line(point, line_func=Line)

        self.add(ax, line, dot)

class GetVerticalLineExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        point = ax.coords_to_point(-3.5, 2)

        dot = Dot(point)
        line = ax.get_vertical_line(point, line_config={"dashed_ratio": 0.85})

        self.add(ax, line, dot)

class GetLinesToPointExample(Scene):
    def construct(self):
        ax = Axes()
        circ = Circle(radius=0.5).move_to([-4, -1.5, 0])

        lines_1 = ax.get_lines_to_point(circ.get_right(), color=GREEN_B)
        lines_2 = ax.get_lines_to_point(circ.get_corner(DL), color=BLUE_B)
        self.add(ax, lines_1, lines_2, circ)

class GetSecantSlopeGroupExample(Scene):
    def construct(self):
        ax = Axes(y_range=[-1, 7])
        graph = ax.plot(lambda x: 1 / 4 * x ** 2, color=BLUE)
        slopes = ax.get_secant_slope_group(
            x=2.0,
            graph=graph,
            dx=1.0,
            dx_label=Tex("dx = 1.0"),
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=4,
            secant_line_color=RED_D,
        )

        self.add(ax, graph, slopes)

class GetVerticalLinesToGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 8.0, 1],
            y_range=[-1, 1, 0.2],
            axis_config={"font_size": 24},
        ).add_coordinates()

        curve = ax.plot(lambda x: np.sin(x) / np.e ** 2 * x)

        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 4], num_lines=30, color=BLUE
        )

        self.add(ax, curve, lines)

class GetXYAxisLabelExample(Scene):
    def construct(self):
        ax = Axes(x_range=(0, 8), y_range=(0, 5), x_length=8, y_length=5)
        x_label = ax.get_x_axis_label(
            Tex("$x$-values").scale(0.65), edge=DOWN, direction=DOWN, buff=0.5
        )
        y_label = ax.get_y_axis_label(
            Tex("$y$-values").scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )
        self.add(ax, x_label, y_label)

class InputToGraphPointExample(Scene):
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x : np.cos(x))

        # move a square to PI on the cosine curve.
        position = ax.input_to_graph_point(x=PI, graph=curve)
        sq = Square(side_length=1, color=YELLOW).move_to(position)

        self.add(ax, curve, sq)

class AntiderivativeExample(Scene):
    def construct(self):
        ax = Axes()
        graph1 = ax.plot(
            lambda x: (x ** 2 - 2) / 3,
            color=RED,
        )
        graph2 = ax.plot_antiderivative_graph(graph1, color=BLUE)
        self.add(ax, graph1, graph2)

class DerivativeGraphExample(Scene):
    def construct(self):
        ax = NumberPlane(y_range=[-1, 7], background_line_style={"stroke_opacity": 0.4})

        curve_1 = ax.plot(lambda x: x ** 2, color=PURPLE_B)
        curve_2 = ax.plot_derivative_graph(curve_1)
        curves = VGroup(curve_1, curve_2)

        label_1 = ax.get_graph_label(curve_1, "x^2", x_val=-2, direction=DL)
        label_2 = ax.get_graph_label(curve_2, "2x", x_val=3, direction=RIGHT)
        labels = VGroup(label_1, label_2)

        self.add(ax, curves, labels)

class ImplicitExample(Scene):
    def construct(self):
        ax = Axes()
        a = ax.plot_implicit_curve(
            lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE
        )
        self.add(ax, a)

class ParametricCurveExample(Scene):
    def construct(self):
        ax = Axes()
        cardioid = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                    np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                    0,
                ]
            ),
            t_range=[0, 2 * PI],
            color="#0FF1CE",
        )
        self.add(ax, cardioid)

class PolarGraphExample(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: 2 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)
        self.add(plane, graph)

class PlotSurfaceExample(ThreeDScene):
    def construct(self):
        resolution_fa = 16
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        axes = ThreeDAxes(x_range=(-3, 3, 1), y_range=(-3, 3, 1), z_range=(-5, 5, 1))
        def param_trig(u, v):
            x = u
            y = v
            z = 2 * np.sin(x) + 2 * np.cos(y)
            return z
        trig_plane = axes.plot_surface(
            param_trig,
            resolution=(resolution_fa, resolution_fa),
            u_range = (-3, 3),
            v_range = (-3, 3),
            colorscale = [BLUE, GREEN, YELLOW, ORANGE, RED],
            )
        self.add(axes, trig_plane)
        self.wait()
        self.move_camera(phi=50 * DEGREES, theta=-80 * DEGREES, zoom= 0.5)
        self.wait()

class PolarToPointExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(azimuth_units="PI radians", size=6)
        polartopoint_vector = Vector(polarplane_pi.polar_to_point(3, PI/4))
        self.add(polarplane_pi)
        self.add(polartopoint_vector)

class NumberPlaneExample(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(number_plane)

class NumberPlaneScaled(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=5,
            y_length=2,
        ).move_to(LEFT*3)

        number_plane_scaled_y = NumberPlane(
            x_range=(-4, 11, 1),
            x_length=5,
            y_length=4,
        ).move_to(RIGHT*3)

        self.add(number_plane)
        self.add(number_plane_scaled_y)

class PolarPlaneExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
        ).add_coordinates()
        self.add(polarplane_pi)

class GetZAxisLabelExample(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        lab = ax.get_z_axis_label(Tex("$z$-label"))
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.add(ax, lab)

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)

class PlotParametricFunction(Scene):
    def func(self, t):
        return np.array((np.sin(2 * t), np.sin(3 * t), 0))

    def construct(self):
        func = ParametricFunction(self.func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ]), color=RED, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        num6 = l1.numbers[8]
        num6.set_color(RED)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
        self.add(line_group)

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.add(chart, c_bar_lbls)

class ExampleSampleSpace(Scene):
    def construct(self):
        poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
        poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
        poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
        poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
        poly_group = VGroup(poly1, poly2, poly3).arrange()
        self.add(poly_group)

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)

class DeterminantOfAMatrix(Scene):
    def construct(self):
        matrix = Matrix([
            [2, 0],
            [-1, 1]
        ])

        # scaling down the `det` string
        det = get_det_text(matrix,
                    determinant=3,
                    initial_scale_factor=1)

        # must add the matrix
        self.add(matrix)
        self.add(det)

class IntegerMatrixExample(Scene):
    def construct(self):
        m0 = IntegerMatrix(
            [[3.7, 2], [42.2, 12]],
            left_bracket="(",
            right_bracket=")")
        self.add(m0)

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, "\pi"], [-1, 1]])
        m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
            v_buff=1.3,
            h_buff=0.8,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF,
            left_bracket="\{",
            right_bracket="\}")
        m1.add(SurroundingRectangle(m1.get_columns()[1]))
        m2 = Matrix([[2, 1], [-1, 3]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        m3 = Matrix([[2, 1], [-1, 3]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        m4 = Matrix([[2, 1], [-1, 3]],
        ).set_column_colors(RED, GREEN)
        m5 = Matrix([[2, 1], [-1, 3]],
        ).set_row_colors(RED, GREEN)
        g = Group(
            m0,m1,m2,m3,m4,m5
        ).arrange_in_grid(buff=2)
        self.add(g)

class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)

class GetRowsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_rows()[1]))
        self.add(m0)

class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)

class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))

class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)

class ArrangeInGrid(Scene):
    def construct(self):
        boxes = VGroup(*[
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))
            for i in range(24)
        ])
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr"
        )

class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)

class ArcBraceExample(Scene):
    def construct(self):
        arc_1 = Arc(radius=1.5,start_angle=0,angle=2*PI/3).set_color(RED)
        brace_1 = ArcBrace(arc_1,LEFT)
        group_1 = VGroup(arc_1,brace_1)

        arc_2 = Arc(radius=3,start_angle=0,angle=5*PI/6).set_color(YELLOW)
        brace_2 = ArcBrace(arc_2)
        group_2 = VGroup(arc_2,brace_2)

        arc_3 = Arc(radius=0.5,start_angle=-0,angle=PI).set_color(BLUE)
        brace_3 = ArcBrace(arc_3)
        group_3 = VGroup(arc_3,brace_3)

        arc_4 = Arc(radius=0.2,start_angle=0,angle=3*PI/2).set_color(GREEN)
        brace_4 = ArcBrace(arc_4)
        group_4 = VGroup(arc_4,brace_4)

        arc_group = VGroup(group_1, group_2, group_3, group_4).arrange_in_grid(buff=1.5)
        self.add(arc_group.center())

class BraceExample(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        for i in np.linspace(0.1,1.0,4):
            br = Brace(s, sharpness=i)
            t = Text(f"sharpness= {i}").next_to(br, RIGHT)
            self.add(t)
            self.add(br)
        VGroup(*self.mobjects).arrange(DOWN, buff=0.2)

class BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)

class svg_example(Scene):
    def construct(self):
        filament = SVGMobject(file_name='C:/Users/saidb/Documents/ManimCE/project/filament.svg')
        self.add(filament)

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        t0.add_highlighted_cell((2,2), color=GREEN)
        x_vals = np.linspace(-2,2,5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [["+", 0, 5, 10],
            [0, 0, 5, 10],
            [2, 2, 7, 12],
            [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(BLUE)
        t2.get_vertical_lines()[:3].set_color(BLUE)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT))
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t3 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],
            [b.copy(),a.copy(),a.copy()],
            [a.copy(),b.copy(),b.copy()]])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1,21).reshape(5,4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.add(g1, g2)

class DecimalTableExample(Scene):
    def construct(self):
        x_vals = [-2,-1,0,1,2]
        y_vals = np.exp(x_vals)
        t0 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
            h_buff=1,
            element_to_mobject_config={"num_decimal_places": 2})
        self.add(t0)

class IntegerTableExample(Scene):
    def construct(self):
        t0 = IntegerTable(
            [[0,30,45,60,90],
            [90,60,45,30,0]],
            col_labels=[
                MathTex("\\frac{\sqrt{0}}{2}"),
                MathTex("\\frac{\sqrt{1}}{2}"),
                MathTex("\\frac{\sqrt{2}}{2}"),
                MathTex("\\frac{\sqrt{3}}{2}"),
                MathTex("\\frac{\sqrt{4}}{2}")],
            row_labels=[MathTex("\sin"), MathTex("\cos")],
            h_buff=1,
            element_to_mobject_config={"unit": "^{\circ}"})
        self.add(t0)

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["This", "is a"],
            ["simple", "Table in \n Manim."]])
        t1 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        t1.add_highlighted_cell((2,2), color=YELLOW)
        t2 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT})
        t2.add(t2.get_cell((2,2), color=RED))
        t3 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW})
        t3.remove(*t3.get_vertical_lines())
        g = Group(
            t0,t1,t2,t3
        ).scale(0.7).arrange_in_grid(buff=1)
        self.add(g)

class CreateTableExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            include_outer_lines=True)
        self.play(table.create())
        self.wait()

class GetColumnsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_columns()[1]))
        self.add(table)

class GetRowsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_rows()[1]))
        self.add(table)

class GetEntriesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries()
        for item in ent:
            item.set_color(random_bright_color())
        table.get_entries((2,2)).rotate(PI)
        self.add(table)

class GetEntriesWithoutLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries_without_labels()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        table.get_entries_without_labels((2,2)).rotate(PI)
        self.add(table)

class GetHighlightedCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        highlight = table.get_highlighted_cell((2,2), color=GREEN)
        table.add_to_back(highlight)
        self.add(table)

class GetHorizontalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_horizontal_lines().set_color(RED)
        self.add(table)

class GetVerticalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_vertical_lines()[0].set_color(RED)
        self.add(table)

class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(table)

class SetRowColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(table)

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.add(rendered_code)

class MovingSquareWithUpdaters(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.animate.to_edge(DOWN),
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class IntegerExample(Scene):
    def construct(self):
        self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
        self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
        self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
        self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))

class VariablesWithValueTracker(Scene):
    def construct(self):
        var = 0.5
        on_screen_var = Variable(var, Text("var"), num_decimal_places=3)

        # You can also change the colours for the label and value
        on_screen_var.label.set_color(RED)
        on_screen_var.value.set_color(GREEN)

        self.play(Write(on_screen_var))
        # The above line will just display the variable with
        # its initial value on the screen. If you also wish to
        # update it, you can do so by accessing the `tracker` attribute
        self.wait()
        var_tracker = on_screen_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        int_var = 0
        on_screen_int_var = Variable(
            int_var, Text("int_var"), var_type=Integer
        ).next_to(on_screen_var, DOWN)
        on_screen_int_var.label.set_color(RED)
        on_screen_int_var.value.set_color(GREEN)

        self.play(Write(on_screen_int_var))
        self.wait()
        var_tracker = on_screen_int_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        # If you wish to have a somewhat more complicated label for your
        # variable with subscripts, superscripts, etc. the default class
        # for the label is MathTex
        subscript_label_var = 10
        on_screen_subscript_var = Variable(subscript_label_var, "{a}_{i}").next_to(
            on_screen_int_var, DOWN
        )
        self.play(Write(on_screen_subscript_var))
        self.wait()

class VariableExample(Scene):
    def construct(self):
        start = 2.0

        x_var = Variable(start, 'x', num_decimal_places=3)
        sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
        Group(x_var, sqr_var).arrange(DOWN)

        sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))

        self.add(x_var, sqr_var)
        self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
        self.wait(0.1)

class BulletedListExample(Scene):
    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)

class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)

class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version 0.17.2")
        self.add(banner, title)

class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)

        t2 = Text("2. Clustering").set_color(WHITE)

        t3 = Text("3. Regression").set_color(WHITE)

        t4 = Text("4. Prediction").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)

class MarkupExample(Scene):
    def construct(self):
        text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        self.add(text)
        self.wait()
        text2 = MarkupText('Blue text is <i>cool</i>!"')
        self.play(Transform(text, text2))
        self.wait()

class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

class UnderlineExample(Scene):
    def construct(self):
        text1 = MarkupText(
            '<span underline="double" underline_color="green">bla</span>'
        )
        text2 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text3 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        )
        text4 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text5 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

class FontExample(Scene):
    def construct(self):
        text1 = MarkupText(
            'all in sans <span font_family="serif">except this</span>', font="sans"
        )
        text2 = MarkupText(
            '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
        )
        text3 = MarkupText("special char > or &gt;")
        text4 = MarkupText("special char &lt; and &amp;")
        group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.add(group)


class JustifyText(Scene):
    def construct(self):
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            FadeOut(not_justified_text),
            FadeIn(justified_text),
            FadeOut(njust_title),
            FadeIn(just_title),
        )
        self.wait(1)

class ParagExample(Scene):
    def construct(self):
        paragraph = Paragraph('this is a awesome', 'paragraph',
                      'With \nNewlines', '\tWith Tabs',
                      '  With Spaces', 'With Alignments',
                      'center', 'left', 'right')
        self.add(paragraph)
        self.wait()


class TextItalicAndBoldExample(Scene):
    def construct(self):
        text1 = Text("Hello world", slant=ITALIC)
        text2 = Text("Hello world", t2s={'world':ITALIC})
        text3 = Text("Hello world", weight=BOLD)
        text4 = Text("Hello world", t2w={'world':BOLD})
        text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
        text6 = Text(
            "Visit us at docs.manim.community",
            t2c={"docs.manim.community": YELLOW},
            disable_ligatures=True,
       )
        text6.scale(1.3).shift(DOWN)
        self.add(text1, text2, text3, text4, text5 , text6)
        Group(*self.mobjects).arrange(DOWN, buff=.8).set_height(config.frame_height-LARGE_BUFF)

class TextMoreCustomization(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)

class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Dodecahedron()
        self.add(obj)

class IcosahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Icosahedron()
        self.add(obj)

class OctahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Octahedron()
        self.add(obj)

class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)

class PolyhedronSubMobjects(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        octahedron = Octahedron(edge_length = 3)
        octahedron.graph[0].set_color(RED)
        octahedron.faces[2].set_color(YELLOW)
        self.add(octahedron)

class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Tetrahedron()
        self.add(obj)

class ExampleArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, arrow)

class ExampleCone(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
        self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
        self.add(axes, cone)

class CubeExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.add(cube)

class ExampleCylinder(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = Cylinder(radius=2, height=3)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, cylinder)

class Dot3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(axes, dot_1, dot_2,dot_3)

class ExampleLine3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, line)

class ParallelLineExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(PI / 3, -PI / 4)
        ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
        line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
        line2 = Line3D.parallel_to(line1, color=YELLOW)
        self.add(ax, line1, line2)

class PerpLineExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(PI / 3, -PI / 4)
        ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
        line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
        line2 = Line3D.perpendicular_to(line1, color=BLUE)
        self.add(ax, line1, line2)

class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)

class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color(RED)
        self.add(sphere1)
        sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
        sphere2.set_color(GREEN)
        self.add(sphere2)
        sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
        sphere3.set_color(BLUE)
        self.add(sphere3)

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            resolution=8,
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(axes, surface)

class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, surface_plane)

class ExampleTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, torus)

class ImageFromArray(Scene):
    def construct(self):
        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.height = 7
        self.add(image)

class ImageInterpolationEx(Scene):
    def construct(self):
        img = ImageMobject(np.uint8([[63, 0, 0, 0],
                                        [0, 127, 0, 0],
                                        [0, 0, 191, 0],
                                        [0, 0, 0, 255]
                                        ]))

        img.height = 2
        img1 = img.copy()
        img2 = img.copy()
        img3 = img.copy()
        img4 = img.copy()
        img5 = img.copy()

        img1.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        img2.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])
        img3.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        img4.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
        img5.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        img1.add(Text("nearest").scale(0.5).next_to(img1,UP))
        img2.add(Text("lanczos").scale(0.5).next_to(img2,UP))
        img3.add(Text("linear").scale(0.5).next_to(img3,UP))
        img4.add(Text("cubic").scale(0.5).next_to(img4,UP))
        img5.add(Text("box").scale(0.5).next_to(img5,UP))

        x= Group(img1,img2,img3,img4,img5)
        x.arrange()
        self.add(x)

class PgroupExample(Scene):
    def construct(self):

        p1 = PointCloudDot(radius=1, density=20, color=BLUE)
        p1.move_to(4.5 * LEFT)
        p2 = PointCloudDot()
        p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
        p3.move_to(4.5 * RIGHT)
        pList = PGroup(p1, p2, p3)

        self.add(pList)

class PMobjectExample(Scene):
    def construct(self):

        pG = PGroup()  # This is just a collection of PMobject's

        # As the scale factor increases, the number of points
        # removed increases.
        for sf in range(1, 9 + 1):
            p = PointCloudDot(density=20, radius=1).thin_out(sf)
            # PointCloudDot is a type of PMobject
            # and can therefore be added to a PGroup
            pG.add(p)

        # This organizes all the shapes in a grid.
        pG.arrange_in_grid()

        self.add(pG)

class PointCloudDotExample(Scene):
    def construct(self):
        cloud_1 = PointCloudDot(color=RED)
        cloud_2 = PointCloudDot(stroke_width=4, radius=1)
        cloud_3 = PointCloudDot(density=15)

        group = Group(cloud_1, cloud_2, cloud_3).arrange()
        self.add(group)

class PointCloudDotExample2(Scene):
    def construct(self):
        plane = ComplexPlane()
        cloud = PointCloudDot(color=RED)
        self.add(
            plane, cloud
        )
        self.wait()
        self.play(
            cloud.animate.apply_complex_function(lambda z: np.exp(z))
        )

class LineGradientExample(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)

class DashedVMobjectExample(Scene):
    def construct(self):
        r = 0.5

        top_row = VGroup()  # Increasing num_dashes
        for dashes in range(1, 12):
            circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
            top_row.add(circ)

        middle_row = VGroup()  # Increasing dashed_ratio
        for ratio in np.arange(1 / 11, 1, 1 / 11):
            circ = DashedVMobject(
                Circle(radius=r, color=WHITE), dashed_ratio=ratio
            )
            middle_row.add(circ)

        func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
        func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
        func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
        bottom_row = VGroup(func_even,func_stretched)

        top_row.arrange(buff=0.3)
        middle_row.arrange()
        bottom_row.arrange(buff=1)
        everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
        self.add(everything)

class ShapesWithVDict(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(pairs, show_keys=True)

        # display it just like a VGroup
        self.play(Create(my_dict))
        self.wait()

        text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # add a key-value pair by wrapping it in a single-element list of tuple
        # after attrs branch is merged, it will be easier like `.add(t=text)`
        my_dict.add([("t", text)])
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].animate.scale(3))
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = Tex("Some other text").set_color(BLUE)
        self.wait()

        # remove submobject by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOut(my_dict["r"], shift=DOWN))
        self.wait()

        # you can also make a VDict from an existing dict of mobjects
        plain_dict = {
            1: Integer(1).shift(DOWN),
            2: Integer(2).shift(2 * DOWN),
            3: Integer(3).shift(3 * DOWN),
        }

        vdict_from_plain_dict = VDict(plain_dict)
        vdict_from_plain_dict.shift(1.5 * (UP + LEFT))
        self.play(Create(vdict_from_plain_dict))

        # you can even use zip
        vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        vdict_using_zip.shift(1.5 * RIGHT)
        self.play(Create(vdict_using_zip))
        self.wait()

class ArcShapeIris(Scene):
    def construct(self):
        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        self.add(circles_group)

class AddToVGroup(Scene):
    def construct(self):
        circle_red = Circle(color=RED)
        circle_green = Circle(color=GREEN)
        circle_blue = Circle(color=BLUE)
        circle_red.shift(LEFT)
        circle_blue.shift(RIGHT)
        gr = VGroup(circle_red, circle_green)
        gr2 = VGroup(circle_blue) # Constructor uses add directly
        self.add(gr,gr2)
        self.wait()
        gr += gr2 # Add group to another
        self.play(
            gr.animate.shift(DOWN),
        )
        gr -= gr2 # Remove group
        self.play( # Animate groups separately
            gr.animate.shift(LEFT),
            gr2.animate.shift(UP),
        )
        self.play( #Animate groups without modification
            (gr+gr2).animate.shift(RIGHT)
        )
        self.play( # Animate group without component
            (gr-circle_red).animate.shift(RIGHT)
        )

class ChangeOfDirection(Scene):
    def construct(self):
        ccw = RegularPolygon(5)
        ccw.shift(LEFT)
        cw = RegularPolygon(5)
        cw.shift(RIGHT).reverse_direction()

        self.play(Create(ccw), Create(cw),
        run_time=4)

class SetSheen(Scene):
    def construct(self):
        circle = Circle(fill_opacity=1).set_sheen(-0.3, DR)
        self.add(circle)

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

class ValueTrackerExample(Scene):
    def construct(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(0)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        tracker += 1.5
        self.wait(1)
        tracker -= 4
        self.wait(0.5)
        self.play(tracker.animate.set_value(5)),
        self.wait(0.5)
        self.play(tracker.animate.set_value(3))
        self.play(tracker.animate.increment_value(-2))
        self.wait(0.5)

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))

class SizingAndSpacing(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()

class Coloring(Scene):
    def construct(self):
        func = lambda pos: pos - LEFT * 5
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
        max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
        vf = ArrowVectorField(
            func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf, min_radius, max_radius)

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(StreamLines(func))

class StreamLineCreation(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()

class EndAnimation(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

class Nudging(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )
        self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)

        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)

        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(circle, dot)
        self.wait(6)

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))

class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))

class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))

class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()

class UseZoomedScene(ZoomedScene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT))

class ChangingZoomScale(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):
        dot = Dot().set_color(GREEN)
        sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
        self.add(dot, sq)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT * 0.3))

        self.play(self.zoomed_camera.frame.animate.scale(4))
        self.play(self.zoomed_camera.frame.animate.shift(0.5 * DOWN))

class CounterclockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.counterclockwise_path(),
                run_time=2,
            )
        )
        self.wait()

class PathAlongArcExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_arc(TAU * 2 / 3),
                run_time=3,
            )
        )
        self.wait()

class PathAlongCirclesExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        circle_center = Dot(3 * LEFT)
        self.add(circle_center)

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_circles(
                    2 * PI, circle_center.get_center()
                ),
                run_time=3,
            )
        )
        self.wait()

class StraightPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.straight_path(),
                run_time=2,
            )
        )
        self.wait()

class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)

class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()



        
# manim -pql scene.py CreateCircle