from manim import *


class ArrowMorphing(Scene):
    def construct(self):
        arrow = Arrow(ORIGIN, (3*0.8, 3*0.6, 0)) #scale(3)
        beautiful_colors = MathTex( r"0.6|0\rangle+0.8|1\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).shift(RIGHT*2.5, UP*2.5)
        arrow_group = VGroup(arrow, beautiful_colors)

        arrow_ketone = Arrow(ORIGIN, (3, 0, 0)) #scale(3)
        one = MathTex( r"|1\rangle").shift(RIGHT*4)
        arrow_ketone_group = VGroup(arrow_ketone, one)

        self.play(Write(arrow_group))
        self.play(Transform(arrow_group, arrow_ketone_group))
        self.wait()

class Probability(Scene):
    def construct(self):
        arrow = Arrow((-3-10*0.8, 0.5-10*0.6, 0), (-3, 0.5, 0))

        zero_point_six = MathTex(r"0.6", tex_to_color_map={"0.6": BLUE})
        zero_point_eight = MathTex(r"0.8", tex_to_color_map={"0.8": BLUE})
        one_2 = MathTex(
            r"|1\rangle",
        )
        zero_2 = MathTex(
            r"|0\rangle +",
        )
        ket_group = VGroup(zero_point_six, zero_2, zero_point_eight, one_2).arrange(RIGHT).shift(UP*0.5)
        ket_group.scale(1.5)
        # self.play(Write(ket_group))
        self.add(ket_group, arrow, zero_point_eight, zero_point_six)
        # Draw the initial starting ket

        self.wait()

        zero_point_six_eq_2 = MathTex(r"0.6^{2}", tex_to_color_map={"0.6": BLUE})
        zero_point_eight_eq_2 = MathTex(r"0.8^{2}", tex_to_color_map={"0.8": BLUE})
        plus = MathTex(r"+")
        eq_2_group = VGroup(zero_point_six_eq_2, plus, zero_point_eight_eq_2).arrange(RIGHT).scale(1).shift(DOWN*0.5)

        zero_point_six_2 = zero_point_six.copy()
        zero_point_eight_2 = zero_point_eight.copy()

        self.add(zero_point_six_2, zero_point_eight_2)

        self.play(
            Transform(zero_point_six, zero_point_six_eq_2)
        )
        self.play(Transform(zero_point_eight, zero_point_eight_eq_2))
        self.play(Write(plus))

        # self.wait()
        
        equals = MathTex(r"=").scale(0.5).shift(LEFT*2, DOWN*0.5)
        eq_3_2 = MathTex(r"+")
        zero_point36 = MathTex(r"0.36").set_color(BLUE)
        zero_point64 = MathTex(r"0.64").set_color(BLUE)
        eq_3_group = VGroup(zero_point36, eq_3_2, zero_point64).arrange(RIGHT).scale(1).shift(DOWN*0.5)

        self.play(Transform(zero_point_six, zero_point36), Transform(zero_point_eight, zero_point64), Write(equals))

        # here we add brackets to the bottom about this is probability 1 and that is probability 0
        b1 = Brace(zero_point_six).set_opacity(0.5)
        b1text = b1.get_text("""Probability of\\\\
        measuring 0\\\\""").scale(0.4).shift(UP*0.25).set_opacity(0.5)

        b2 = Brace(zero_point_eight).set_opacity(0.5)
        b2text = b2.get_text("Probability of\\\\", "measuring 1\\\\").scale(0.4).shift(UP*0.25).set_opacity(0.5)


        self.play(Create(b1), Write(b1text))

        self.wait()

        self.play(Create(b2), Write(b2text))
        self.wait()

        # line2 = Line(zero_point_eight.get_start(), zero_point_eight.get_end())
        # b2 = Brace()
        # b2text = b2.get_text("Probability of measuring 0")
        # self.play(Create(b2), Write(b1text))
