import math
from manim import *

class Crankshaft(Scene):

    def construct(self):
        # Crankshaft Black Box
        crankshaftGroup = VGroup()
        crankshaftBox = Rectangle(width=4, height=3).set_stroke(color=WHITE, width=2)
        crankshaftText = Text("Crankshaft")
        crankshaftGroup.add(crankshaftBox, crankshaftText)
        self.play(Create(crankshaftBox))
        self.play(Create(crankshaftText))
        self.wait(2)
        # Input
        crankshaftInputText = Text("Torque").move_to(LEFT * 5)
        self.play(FadeIn(crankshaftInputText), run_time = 0.3)
        crankshaftInputArrow = Arrow(crankshaftInputText.get_right(), crankshaftBox.get_left())
        self.play(GrowArrow(crankshaftInputArrow))
        self.wait()
        # Output
        crankshaftOutputText = Text("Rotation").move_to(RIGHT * 5)
        crankshaftOutputArrow = Arrow(crankshaftBox.get_right(),crankshaftOutputText.get_left())
        self.play(GrowArrow(crankshaftOutputArrow))
        self.play(FadeIn(crankshaftOutputText), run_time = 0.3)
        self.wait()
        # States
        thetaText = MathTex("\\theta")
        thetaDotText = MathTex("\dot{\\theta}")
        thetaDotDotText = MathTex("\ddot{\\theta}")
        crankshaftThetaStateTexts = VGroup(thetaText, thetaDotText, thetaDotDotText).arrange(DOWN, center=False, aligned_edge=LEFT).move_to(RIGHT * 4.5).scale(1.5)
        
        crankshaftOutputArrow2 = Arrow(crankshaftBox.get_right(),crankshaftThetaStateTexts.get_left())
        self.play(ReplacementTransform(crankshaftOutputText, crankshaftThetaStateTexts), ReplacementTransform(crankshaftOutputArrow, crankshaftOutputArrow2))
        self.wait(2)

        # Move BlackBox to Corner
        crankshaftBlackBoxGroup = VGroup(crankshaftGroup, crankshaftInputText, crankshaftInputArrow, crankshaftThetaStateTexts, crankshaftOutputArrow2)
        self.play(crankshaftBlackBoxGroup.animate.scale(0.5).to_corner(UL-0.5*LEFT), run_time = 0.5)
        box1 = SurroundingRectangle(crankshaftBlackBoxGroup, buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.play(Create(box1))
        self.wait()

        # Crankshaft Mathematical Model
        mathematicalModel = MathTex("I \\frac{d^{2}\\theta}{dt^{2}}", "+", "c \\frac{d\\theta}{dt}", "+", "k\\theta", "=", "T")
        self.play(Write(mathematicalModel))
        self.wait()
        for i in range(len(mathematicalModel)):
            if (i % 2) == 0:
                self.play(Indicate(mathematicalModel[i]))
        self.wait()
        mathematicalModelwok = MathTex("I \\frac{d^{2}\\theta}{dt^{2}}", "+", "c \\frac{d\\theta}{dt}", "=", "T")
        self.play(TransformMatchingTex(mathematicalModel,mathematicalModelwok))
        self.wait()
        self.play(mathematicalModelwok.animate.next_to(crankshaftBlackBoxGroup, 2 * RIGHT), run_time = 0.5)
        box2 = SurroundingRectangle(mathematicalModelwok, buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.play(Create(box2))
        self.wait()

        # Laplace
        laplaceRaw = MathTex("I(s^{2}\\theta(s)-s\, \\theta(0)-{\\theta}'(0))", "+", "c(s\\theta(s)-\\theta(0))", "=", "T(s)")
        for i in range(len(laplaceRaw)):
            self.play(TransformFromCopy(mathematicalModelwok[i], laplaceRaw[i]))
        self.wait()

        laplace1 = MathTex("I(s^{2}\\theta(s)", "-s\, \\theta(0)-{\\theta}'(0)", ")", "+", "c(s\\theta(s)", "-\\theta(0)", ")", "=", "T(s)")
        laplace1[1].set_color(YELLOW)
        laplace1[5].set_color(YELLOW)
        self.play(FadeTransform(laplaceRaw, laplace1))
        self.wait()
        laplace2 = MathTex("Is^{2}\\theta(s)", "+", "c\, s\\theta(s)", "=", "T(s)")
        self.play(FadeTransform(laplace1, laplace2))
        self.wait()
        laplace3 = MathTex("\\theta(s)(Is^{2}+ c\, s)=T(s)")
        self.play(TransformMatchingShapes(laplace2,laplace3))
        self.wait()
        transferFunction = MathTex("\\frac{\\theta(s)}{T(s)} = \\frac{1}{Is^{2}+ c\, s}")
        self.play(TransformMatchingShapes(laplace3,transferFunction))
        self.wait()
        self.play(transferFunction.animate.next_to(mathematicalModelwok, 2 * RIGHT), run_time = 0.5)
        box3 = SurroundingRectangle(transferFunction, buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.play(Create(box3))
        self.wait()

        # MATLAB c2d
        continuesTimeText = Text("Continues Time")
        discreateTimeText = Text("Discrete Time")
        c2dText = VGroup(continuesTimeText, discreateTimeText).arrange(RIGHT, buff=3)
        c2dArrow = Arrow(c2dText[0].get_right(), c2dText[1].get_left())
        self.play(FadeIn(c2dText[0]))
        self.play(GrowArrow(c2dArrow),FadeIn(c2dText[1]))
        self.wait()
        c2dText.add(c2dArrow)
        matlabc2dText = Tex("\(>\!\!>\)\, ", "sysd", " = ", "c2d(", "sysc", ", ", "Ts", ")")
        self.play(FadeTransform(c2dText, matlabc2dText))
        self.wait()
        self.play(Indicate(matlabc2dText[1]))
        self.wait()
        matlabc2dText[4].set_color(YELLOW)
        self.play(Indicate(matlabc2dText[4]))
        self.play(Circumscribe(transferFunction))
        self.wait()
        matlabc2dText[4].set_color(WHITE)
        matlabc2dText[6].set_color(YELLOW)
        self.play(Indicate(matlabc2dText[6]))
        self.wait(2)
        matlabc2dText[6].set_color(WHITE)
        self.wait()
        self.play(FadeOut(matlabc2dText))

        # Calculate Frequency
        fEquationTex = MathTex("Sampling\, Frequency", " \\geq ", "20000\, rpm", "\\cdot 2", "\\cdot 10")
        self.play(Write(fEquationTex), run_time = 3)
        self.play(Indicate(fEquationTex[2]))
        self.wait()
        fEquationTex2 = MathTex("Sampling\, Frequency", " \\geq ", "333\, rps", "\\cdot 2", "\\cdot 10")
        self.play(TransformMatchingTex(fEquationTex,fEquationTex2))
        self.wait()
        self.play(Indicate(fEquationTex2[3]))
        self.wait()
        self.play(FadeOut(fEquationTex2))

        # Show Crank-Piston Cycle
        Xoffset = 2 * DOWN
        startAngle = PI/2
        curAngle = 0
        l1 = 0.13
        l2 = 0.44
        e = 0
        d = math.sqrt(math.pow(l2 - l1, 2) - math.pow(e,2))

        crank = SVGMobject(file_name = "crank.svg").rotate(startAngle).move_to(Xoffset)
        piston = SVGMobject(file_name = "piston.svg").scale(0.5).move_to(((2*l1)*5+1.5)*UP + Xoffset)
        rod = self.getline(0*UP + 0*DOWN + Xoffset,piston)

        self.play(FadeIn(rod), FadeIn(crank), FadeIn(piston))
        self.wait()

        rod.add_updater(
            lambda mob: mob.become(self.getline(self.getPointPos(l1, curAngle, startAngle, Xoffset),piston))
        )

        for i in range(60):
            curAngle = (2 * PI) * (i / 60) + startAngle
            pistonPosition = math.sqrt(math.pow(l2,2) - math.pow(e + l1 * math.cos(curAngle),2)) + (l1 * math.sin(curAngle)) - d
            self.play(
                Rotate(crank, angle= 0.105),
                piston.animate.move_to(((pistonPosition * 5) + 1.5) * UP + Xoffset),
                run_time = 1/30)        
        self.wait(2)

        self.play(FadeOut(rod), FadeOut(crank), FadeOut(piston))

        # Continue Calculate Frequency
        self.play(FadeIn(fEquationTex2))
        self.play(Indicate(fEquationTex2[4]))
        self.wait()
        fEquationTex3 = MathTex("Sampling\, Frequency", " \\geq ", "6660\, Hz")
        self.play(TransformMatchingShapes(fEquationTex2,fEquationTex3))
        self.wait()
        fTex = MathTex("Sampling\, Frequency", "=", "10000\, Hz")
        self.play(TransformMatchingShapes(fEquationTex3, fTex))
        self.wait()
        dtText = MathTex("Sample\, Time", "=", "0.0001\, s")
        fanddtText = VGroup(fTex, dtText).arrange(DOWN)
        self.play(TransformMatchingTex(fTex, fanddtText))
        self.wait()

        # Note the frequency and Sample Time
        self.play(fanddtText.animate.scale(0.75).next_to(crankshaftBlackBoxGroup, DOWN, buff = MED_LARGE_BUFF).to_edge(0.5*LEFT))
        box4 = SurroundingRectangle(fanddtText, buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.play(Create(box4))

        # Calculate Inertia and Damping
        Itext = Tex("I")
        cText = Tex("c")
        IandcText = VGroup(Itext, cText).arrange(RIGHT, buff=LARGE_BUFF).move_to(DOWN/2)
        self.play(FadeIn(IandcText))
        self.play(Itext.animate.move_to(3 * LEFT + DOWN/2), cText.animate.move_to(3.5 * RIGHT + DOWN/2))
        self.wait()
        
        inertiaText = MathTex("(", "crankshaft", " + flywheel + 4 \\cdot piston + 4 \\cdot (piston + rod))\\cdot1.5").scale(0.6).next_to(Itext, 2 * DOWN)
        self.play(Write(inertiaText))
        self.wait()
        self.play(inertiaText[1].animate.set_color(YELLOW))
        inertiaCalculation = Text("From Fusion360 calculation, 0.04").scale(0.5).next_to(inertiaText, 2* DOWN)
        self.play(FadeIn(inertiaCalculation))
        self.wait()

        inertiaText2 = MathTex("(0.04 + ", "flywheel", "+ 4 \\cdot (piston + rod))\\cdot1.5").scale(0.6).next_to(Itext, 2 * DOWN)
        self.play(TransformMatchingTex(inertiaText,inertiaText2), FadeOut(inertiaCalculation, shift=UP))
        self.wait()
        self.play(inertiaText2[1].animate.set_color(YELLOW))
        inertiaCalculation2 = MathTex("(0.5)\\cdot7.15\\cdot0.12^{2}=0.0515").next_to(inertiaText2, 2* DOWN)
        self.play(FadeIn(inertiaCalculation2))
        self.wait()

        inertiaText3 = MathTex("(0.04 + 0.0515 + 4 \\cdot (", "piston", "+ rod))\\cdot1.5").scale(0.6).next_to(Itext, 2 * DOWN)
        self.play(TransformMatchingTex(inertiaText2,inertiaText3), FadeOut(inertiaCalculation2, shift=UP))
        self.wait()
        inertiaCalculation3 = Text("very rough estimation, 0.01").scale(0.6).next_to(inertiaText3, 2* DOWN)
        self.play(inertiaText3[1].animate.set_color(YELLOW))
        self.play(FadeIn(inertiaCalculation3))
        self.wait()

        inertiaText4 = MathTex("(0.04 + 0.0515 + 4 \\cdot (0.01 + ", "rod", "))\\cdot1.5").scale(0.6).next_to(Itext, 2 * DOWN)
        self.play(TransformMatchingTex(inertiaText3,inertiaText4), FadeOut(inertiaCalculation3, shift=UP))
        self.wait()
        inertiaCalculation4 = Text("From Fusion360 calculation, 0.0079").scale(0.5).next_to(inertiaText4, 2* DOWN)
        self.play(inertiaText4[1].animate.set_color(YELLOW))
        self.play(FadeIn(inertiaCalculation4))
        self.wait()

        inertiaText5 = MathTex("(0.04 + 0.0515 + 4 \\cdot (0.01 + 0.0079))\\cdot", "1.5").scale(0.6).next_to(Itext, 2 * DOWN)
        self.play(TransformMatchingTex(inertiaText4,inertiaText5), FadeOut(inertiaCalculation4, shift=UP))
        self.wait()

        self.play(inertiaText5[1].animate.set_color(YELLOW))
        self.wait()
        self.play(inertiaText5[1].animate.set_color(WHITE))
        self.wait()

        calculatedInertia = Text("Estimated Inertia = 0.24465").scale(0.5).next_to(inertiaText5, 2* DOWN)
        self.play(FadeIn(calculatedInertia))
        self.wait()

        frictionText = MathTex("(9\\cdot ", "Bearing Damping", "+ 4\\cdot Piston Damping)\\cdot1.5").scale(0.6).next_to(cText, 2 * DOWN)
        self.play(Write(frictionText))
        self.wait()
        self.play(frictionText[1].animate.set_color(YELLOW))
        self.wait()
        oilFriction = MathTex("T = \\frac{u \\cdot 4 \\cdot pi^{2} \\cdot r^{3} \\cdot L \\cdot \dot{\\theta}}{l \\cdot 57.2958}").scale(0.75).next_to(frictionText, 1.5*DOWN)
        self.play(Write(oilFriction))
        self.wait()
        oilFriction2 = MathTex("\\frac {T}{\dot{\\theta}} = \\frac{u \\cdot 4 \\cdot pi^{2} \\cdot r^{3} \\cdot L}{l \\cdot 57.2958}").scale(0.75).next_to(frictionText, 1.5*DOWN)
        self.play(TransformMatchingShapes(oilFriction, oilFriction2))
        self.wait()
        oilFriction3 = MathTex("\\frac {T}{\dot{\\theta}} = 0.0017").scale(0.75).next_to(frictionText, 1.5*DOWN)
        self.play(TransformMatchingShapes(oilFriction2, oilFriction3))
        self.wait()
        frictionText2 = MathTex("(9\\cdot 0.0017 + 4\\cdot ", "Piston Damping", ")\\cdot1.5").scale(0.6).next_to(cText, 2 * DOWN)
        self.play(TransformMatchingTex(frictionText, frictionText2), FadeOut(oilFriction3, shift=UP))
        self.wait()
        self.play(frictionText2[1].animate.set_color(YELLOW))
        self.wait()
        oilFriction4 = MathTex("\\frac {T}{\dot{\\theta}} = 0.05").scale(0.75).next_to(frictionText2, 1.5*DOWN)
        self.play(Write(oilFriction4))
        self.wait()
        frictionText3 = MathTex("(9\\cdot 0.0017 + 4\\cdot 0.05)\\cdot", "1.5").scale(0.6).next_to(cText, 2 * DOWN)
        self.play(TransformMatchingTex(frictionText2, frictionText3), FadeOut(oilFriction4, shift=UP))
        self.wait()

        self.play(Indicate(frictionText3[1]))
        self.wait()

        calculatedDamping = Text("Estimated Damping = 0.32236").scale(0.5).next_to(frictionText3, 2* DOWN)
        self.play(FadeIn(calculatedDamping))
        self.wait()

        # Note the I and c

        finalITex = MathTex("I = 0.24465 \, kg/m^{2}").scale(0.75).move_to(Itext.get_center())
        finalcTex = MathTex("c = 0.32236 \, Nm / \\dot{\\theta}").scale(0.75).move_to(cText.get_center())

        self.play(TransformMatchingTex(Itext, finalITex),
                  TransformMatchingTex(cText, finalcTex))
        
        self.play(FadeOut(calculatedDamping),
                  FadeOut(inertiaText5),
                  FadeOut(calculatedInertia),
                  FadeOut(frictionText3))
        
        coeffsTex = VGroup(finalITex, finalcTex)
        
        self.play(coeffsTex.animate.arrange(DOWN, buff = SMALL_BUFF).next_to(box4, RIGHT))
        self.wait()

        box5 = SurroundingRectangle(coeffsTex, buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.play(Create(box5))
        self.wait()

        # Create Discrete Model

        code = '''T = @(u, l, r, L) (u * 4 * pi^2 * r^3 * L / 57.2958) / l;
u = 0.02; % 70C SAE 30
l = 5.2e-5; %m
r = 0.05; %m
L = 0.05; %m
friction = ((T(u,l,r,L)) * 9 + 4 * 0.05) * 1.5;
inertia = (0.04 + 0.0515 + 0.01 * 4 + 0.0079 * 4) * 1.5;
dt = 0.0001;
c2d(tf(1, [inertia friction 0]), dt)
'''
        rendered_code = Code(code=code, language="matlab", line_spacing=0.5, font="Monospace", stroke_width=1.5).move_to(2*DOWN)
        self.play(Write(rendered_code))
        self.wait()
        result_code = '''ans =

  2.044e-08 z + 2.044e-08
  -----------------------
    z^2 - 2 z + 0.9999
 
Sample time: 0.0001 seconds
Discrete-time transfer function.
        '''
        rendered_result_code = Code(code=result_code, language="c", insert_line_no=False, line_spacing=0.5, font="Monospace", stroke_width=1.5).move_to(2*DOWN)
        self.play(ReplacementTransform(rendered_code, rendered_result_code))
        self.wait()

        # Note Discrete Model

        dtf = MathTex("\\frac{2.044\, e-08\, z + 2.044\, e-08}{z^2 - 2\, z + 0.9999}").move_to(rendered_result_code.get_center())
        self.play(FadeOut(rendered_result_code), FadeIn(dtf))
        self.wait()

        self.play(dtf.animate.scale(0.75).next_to(box5, RIGHT))
        box6 = SurroundingRectangle(dtf)
        self.play(Create(box6), buff=SMALL_BUFF).set_stroke(color=GREEN, width=1)
        self.wait(2)





    
    def getline(self, Point1, Point2):
        start_point = Point1
        end_point = Point2.get_center()
        line = Line(start_point,end_point).set_stroke(width=50) 
        return line

    def getPointPos(self, l1, curAngle, startAngle, Xoffset):
            curAngle += PI/30
            crankXpos = (l1 * 5) * math.cos(curAngle - startAngle)
            crankYpos = -(l1 * 5) * math.sin(curAngle - startAngle)
            return crankXpos * UP + crankYpos * RIGHT + Xoffset


class section(Scene):

    def construct(self):
        self.add(Square())
        






