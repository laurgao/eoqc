from manim import *


class HadamardWire(Scene):
    def construct(self):
        gate = Rectangle(width=3.0, height=2.0).set_fill(BLACK).set_opacity(1.0).scale(0.75).shift(UP*0.5)
        h = Text("H").shift(UP*0.5)
        gate_group = VGroup(gate, h)
        self.add_foreground_mobjects(gate_group)
        labelH = Text("Hadamard gate").shift(DOWN*1).scale(0.75*0.5)
        self.add(gate_group, labelH)
        wire = Line(start=(-5, 0, 0), end=(5, 0, 0)).shift(UP*0.5)

        representation = Text("Wire/ket representation").set_color(YELLOW).scale(0.5).to_corner(UP + LEFT)

        arrow = Arrow(start=(-5, - 2.5, 0), end=(5, -2.5, 0), stroke_width=3).set_color(BLUE)
        label = Text("Time").scale(0.5).next_to(arrow, DOWN, buff=0.5).set_color(BLUE)
        # arrow_group = VGroup(arrow, label).arrange(DOWN)
        
        beautiful_colors = MathTex( r"|0\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).to_edge(LEFT).shift(UP*0.5).shift(RIGHT*0.25).scale(1.5)
        one = MathTex( r"\dfrac{|0\rangle + |1\rangle}{\sqrt{2}}").to_edge(RIGHT).shift(UP*0.5).scale(0.85).shift(RIGHT*0.25)

        
        self.add(wire, arrow, label, representation, beautiful_colors, one)

        self.play(Create(arrow), Write(label), Write(beautiful_colors), Write(one))

        one_2 = one.copy()
        beautiful_colors_2 = beautiful_colors.copy()
        self.play(beautiful_colors_2.animate.shift(RIGHT*3.5), rate_func=linear)
        self.play(Transform(beautiful_colors_2, one_2), run_time=2, rate_func=linear) 

        self.wait()

        beautiful_colors_3 = beautiful_colors.copy()
        self.play(beautiful_colors_3.animate.shift(RIGHT*3.5), rate_func=linear)
        self.play(Transform(beautiful_colors_3, one_2), run_time=2, rate_func=linear)      
        self.wait()


class XWire(Scene):
    def construct(self):
        gate = Rectangle(width=3.0, height=2.0).set_fill(BLACK).set_opacity(1.0).scale(0.75).shift(UP*0.5)
        h = Text("X").shift(UP*0.5)
        gate_group = VGroup(gate, h)
        self.add_foreground_mobjects(gate_group)
        self.add(gate_group)
        labelM = Text("Measurement gate").shift(DOWN*1).scale(0.75*0.5)
        labelX = Text("Pauli-X gate").shift(DOWN*1).scale(0.75*0.5)
        wire = Line(start=(-4, 0, 0), end=(4, 0, 0)).shift(UP*0.5)

        representation = Text("Wire/ket representation").set_color(YELLOW).scale(0.5).to_corner(UP + LEFT)

        arrow = Arrow(start=(-5, - 2.5, 0), end=(5, -2.5, 0), stroke_width=3).set_color(BLUE)
        label = Text("Time").scale(0.5).next_to(arrow, DOWN, buff=0.5).set_color(BLUE)
        # arrow_group = VGroup(arrow, label).arrange(DOWN)
        
        beautiful_colors = MathTex( r"0.6|0\rangle+0.8|1\rangle", tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).to_edge(LEFT).shift(UP*0.5).scale(0.85).shift(LEFT*0.5)
        one = MathTex( r"0.8|0\rangle+0.6|1\rangle", tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).to_edge(RIGHT).shift(UP*0.5).scale(0.85).shift(RIGHT*0.5)
        
        
        self.add(wire, arrow, label, representation, beautiful_colors, one, labelX)
        # self.play(Transform(labelM, labelX))

        # self.play(Create(arrow), Write(label), Write(beautiful_colors), Write(one))

        # one_2 = one.copy()
        # beautiful_colors_2 = beautiful_colors.copy()
        # self.play(beautiful_colors_2.animate.shift(RIGHT*3.5), rate_func=linear)
        # self.play(Transform(beautiful_colors_2, one_2), run_time=2, rate_func=linear) 

        # self.wait()

        # beautiful_colors_3 = beautiful_colors.copy()
        # self.play(beautiful_colors_3.animate.shift(RIGHT*3.5), rate_func=linear)
        # self.play(Transform(beautiful_colors_3, one_2), run_time=2, rate_func=linear)      
        # self.wait()

class HadamardBloch(Scene):
    def construct(self):
        representation = Text("Bloch sphere representation").set_color(YELLOW).scale(0.5).to_corner(UP + LEFT)
        arrow = Arrow(ORIGIN, (0, 3, 0)) #scale(3)
        beautiful_colors = MathTex( r"|0\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).shift(UP*3.5)
        arrow_group = VGroup(arrow, beautiful_colors)

        arrow_ketone = Arrow(ORIGIN, (3, 0, 0)) #scale(3)
        one = MathTex( r"\dfrac{|0\rangle + |1\rangle}{\sqrt{2}}").shift(RIGHT*4.25)
        arrow_ketone_group = VGroup(arrow_ketone, one)

        self.add(representation, arrow_group)
        self.play(Transform(beautiful_colors, one), Rotate(arrow, about_point=arrow.get_start(), angle=-PI/2))
        self.wait()

class XBloch(Scene):
    def construct(self):
        representation = Text("Bloch sphere representation").set_color(YELLOW).scale(0.5).to_corner(UP + LEFT)
        arrow = Arrow(ORIGIN, (3*0.8, 3*0.6, 0)) #scale(3)
        beautiful_colors = MathTex( r"0.6|0\rangle+0.8|1\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).shift(RIGHT*2.5, UP*2.5)
        arrow_group = VGroup(arrow, beautiful_colors)

        arrow_ketone = Arrow(ORIGIN, (-3*0.8, -3*0.6, 0)) #scale(3)
        one = MathTex( r"0.8|0\rangle+0.6|1\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).shift(RIGHT*2.5, UP*2.5)#.rotate_in_place(PI)
        arrow_ketone_group = VGroup(arrow_ketone, one)

        self.add(representation, arrow_group)
        # self.play(Transform(beautiful_colors, one), Rotate(arrow, about_point=arrow.get_start(), angle=-PI))
        self.play(Rotate(arrow_group, about_point=arrow.get_start(), angle=-PI), Transform(beautiful_colors, one),)#  # Rotate(beautiful_colors, about_point=beautiful_colors.get_center(), angle=-PI), 

        self.wait()

class Multipel(Scene):
    def construct(self):
        # arrow = Line(-4, 4)
        # self.play(Rotate(arrow.animate.rotate_in_place(PI), about_point=arrow.get_start(), angle=-PI))
        text = Text('X "flips"')
        text2 = Text("the qubit")
        group = VGroup(text, text2).arrange(DOWN)
        self.add(group)
