from re import A, U, X

from manim import *


class Measurement(Scene):
    def construct(self):
        gate = Rectangle(width=3.0, height=2.0).set_fill(BLACK).scale(0.75).shift(UP*0.5)
        gate_pic = ImageMobject("measurement").scale(0.15).shift(UP*0.5)
        label = Text("Measurement gate").shift(DOWN*1.5).scale(0.75)
        self.play(Create(gate), Write(label), FadeIn(gate_pic))
        self.wait()

class MeasurementWire(Scene):
    def construct(self):
        gate = Rectangle(width=3.0, height=2.0).set_fill(BLACK).set_opacity(1.0).scale(0.75).shift(UP*0.5)
        label = Text("Measurement gate").shift(DOWN*1.5).scale(0.75)
        gate_pic = ImageMobject("measurement").scale(0.15).shift(UP*0.5)
        gate_svg = SVGMobject("measurement").scale(0.15).shift(UP*0.5)
        labelM = Text("Measurement gate").shift(DOWN).scale(0.75*0.5)

        # wire = Line(start=(-5, 0, 0), end=(5, 0, 0)).shift(UP*0.5)
        wire = Line(start=(-4, 0, 0), end=(4, 0, 0)).shift(UP*0.5)

        self.add(gate, gate_pic, label)
        self.add_foreground_mobjects(gate, gate_pic, label)

        representation = Text("Wire/ket representation").set_color(YELLOW).scale(0.5).to_corner(UP + LEFT)

        self.play(Create(wire), Write(representation), Transform(label, labelM), run_time=0.5)
        

        arrow = Arrow(start=(-5, - 2.5, 0), end=(5, -2.5, 0), stroke_width=3).set_color(BLUE)
        label2 = Text("Time").scale(0.5).next_to(arrow, DOWN, buff=0.5).set_color(BLUE)
        # arrow_group = VGroup(arrow, label).arrange(DOWN)
        
        # beautiful_colors = MathTex( r"0.6|0\rangle+0.8|1\rangle",  tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).scale(0.65).to_edge(LEFT).shift(LEFT*0.4).shift(UP*0.5)
        beautiful_colors = MathTex( r"0.6|0\rangle+0.8|1\rangle", tex_to_color_map={"0.6": BLUE, "0.8": BLUE}).to_edge(LEFT).shift(UP*0.5).scale(0.85).shift(LEFT*0.5)

        one = MathTex( r"|1\rangle").scale(1.5).to_edge(RIGHT).shift(UP*0.5).shift(LEFT*0.5)

        self.play(Create(arrow), Write(label2), Write(beautiful_colors), Write(one))

        one_2 = one.copy()
        beautiful_colors_2 = beautiful_colors.copy()
        self.play(beautiful_colors_2.animate.shift(RIGHT*3.5), rate_func=linear)
        self.play(Transform(beautiful_colors_2, one_2), run_time=2, rate_func=linear) 

        self.wait()

        # self.play(Transform(beautiful_colors.copy(), one_2), run_time=3)   
        beautiful_colors_3 = beautiful_colors.copy()
        self.play(beautiful_colors_3.animate.shift(RIGHT*3.5), rate_func=linear)
        self.play(Transform(beautiful_colors_3, one_2), run_time=2, rate_func=linear)      
        self.wait()

        # different gates
        x = Text("X")
        y = Text("Y")
        z = Text("Z")
        rx = MathTex(r"RX \left ( \dfrac{\pi}{2} \right )")
        rz = MathTex(r"RX \left ( \dfrac{\pi}{4} \right )")
        h = Text("H")
        gates = VGroup(x, y, z, rx, rz, h).shift(UP*0.5)
        self.remove_foreground_mobjects(gate)

        self.play(FadeOut(gate_pic), Transform(gate_svg, z), run_time=0.5)
        self.play(Transform(gate_svg, y), run_time=0.5)
        self.play(Transform(gate_svg, rx), run_time=0.5)
        self.play(Transform(gate_svg, h), run_time=0.5)
        self.play(Transform(gate_svg, rz), run_time=0.5)
        self.play(Transform(gate_svg, x), run_time=0.5)
        self.wait()

        # x GATE TRANSFORMATION 

class XMatrix(Scene):
    def construct(self):
        representation = Text("Statevector representation").scale(0.5).set_color(YELLOW).to_corner(UP + LEFT)

        # x_matrix = MathTex(r"\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}").shift(UP)
        x_matrix= Matrix([[0, 1], [1, 0]])
        x_label = Text("X").next_to(x_matrix, DOWN, buff=1).set_color(YELLOW)
        x_group = VGroup(x_matrix, x_label)

        self.play(Write(representation), Write(x_matrix), Write(x_label))
        # X is created.

        self.wait(2)

        # equation it 
        # qubit_matrix = MathTex(r"\begin{bmatrix}0.6\\0.8\end{bmatrix}")
        # qubit_matrix = MathTex("{\\left(","{x","\\over","y}","\\right)}")
        qubit_matrix = Matrix([[0.6], [0.8]])
        print(qubit_matrix[0])
        # qubit_matrix = MathTex(r"{\begin{bmatrix}",r"{0.6",r"\\",r"0.8}",r"\end{bmatrix}}")
        # qubit_matrix = MathTex("\\begin{bmatrix}","0.6","\\\\0.8","\\end{bmatrix}")
        qubit_label = Text("Qubit").next_to(qubit_matrix, DOWN, buff=1).set_color(YELLOW)
        qubit_group = VGroup(qubit_matrix, qubit_label).shift(RIGHT*2)

        multiply = MathTex(r"\times").shift(RIGHT*0.5)

        self.play(x_group.animate.shift(LEFT*1.25), Write(qubit_group), Write(multiply))

        # eq_2 = Matrix([[r"0.6 * 0 + 0.8 * 1"], ["0.6 * 1 + 0.8 * 0"]]).shift(DOWN*1.5) # cmon there gotta be a way to use •
        # eq_2 = Matrix([[0.6,"\\times",0, +, 0.6,"\\times",0,], ["0.6 * 1 + 0.8 * 0"]]).shift(DOWN*1.5) # cmon there gotta be a way to use •
        eq_2_1 = MathTex(0.6,"\\times",0, "+", 0.6,"\\times",0)
        eq_2 = Matrix([[0.6,"\\times",0, "+", 0.8,"\\times",1,], [0.6,"\\times",1, "+", 0.8,"\\times",0,]], h_buff=0.65).shift(DOWN*1.25) # cmon there gotta be a way to use •
        # eq_2 = Matrix([[2, "\\pi"], [-1, 1]])

        equals = MathTex(r"=").shift(LEFT*3.25).shift(DOWN*1.25)
        
        s = qubit_matrix[0][0].copy()
        e = x_matrix[0][0].copy()

        u = eq_2[0][1].copy()
        b = eq_2[0][3].copy()
        f = eq_2[0][5].copy()
        d = eq_2[0][8].copy()

        self.play(Transform(s, eq_2[0][0]), Transform(e, eq_2[0][2]), qubit_group.animate.shift(UP*1), x_group.animate.shift(UP*1), multiply.animate.shift(UP*1), Unwrite(x_label), Unwrite(qubit_label))
        
        a = qubit_matrix[0][1].copy()
        c = qubit_matrix[0][0].copy()
        r = qubit_matrix[0][1].copy()
        l = x_matrix[0][1].copy()
        i = x_matrix[0][2].copy()
        g = x_matrix[0][3].copy()
        
        self.play(Transform(a, eq_2[0][4]), Transform(l, eq_2[0][6]), Write(u))
        self.play(Transform(c, eq_2[0][7]), Transform(i, eq_2[0][9]), Write(b), Write(f))
        self.play(Transform(r, eq_2[0][11]), Transform(g, eq_2[0][13]), Write(d))#, Write(eq_2[0][12]), Write(eq_2[0][10]))
        self.play(Write(equals), Write(eq_2),
            # Unwrite(s),
            # Unwrite(a),
            # Unwrite(c),
            # Unwrite(r),
            # Unwrite(i),
            # Unwrite(l),
            # Unwrite(e),
            # Unwrite(g),
        )
        self.remove(s, a, c, r, e, l, i, g, u, b, f, d)

        eq_3 = Matrix([[0.8], [0.6]]).shift(DOWN*1.25)

        self.wait(0.5)
        self.play(Transform(eq_2, eq_3), equals.animate.shift(RIGHT*1.75))
        self.wait()


class HadamardMatrix(Scene):
    def construct(self):
        representation = Text("Statevector representation").scale(0.5).set_color(YELLOW).to_corner(UP + LEFT)

        # x_matrix = MathTex(r"\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}").shift(UP)
        hadamard_matrix = Matrix([[1, 1], [1, -1]])
        prefix = MathTex(r"\dfrac{1}{\sqrt{2}}").next_to(hadamard_matrix, LEFT, buff=0.25)
        hadamard_label = Text("Hadamard gate").next_to(hadamard_matrix, DOWN, buff=0.5).scale(0.5).set_color(YELLOW)
        hadamard_group = VGroup(hadamard_matrix, prefix, hadamard_label)

        self.play(Write(representation), Write(hadamard_matrix), Write(hadamard_label), Write(prefix))

        qubit_matrix = Matrix([[1], [0]])
        qubit_label = MathTex(r"|0\rangle").next_to(qubit_matrix, DOWN, buff=0.5).set_color(YELLOW)
        qubit_group = VGroup(qubit_matrix, qubit_label).shift(RIGHT*2)
        multiply = MathTex(r"\times").shift(RIGHT*0.5)
        self.play(hadamard_group.animate.shift(LEFT*1.5), Write(qubit_group), FadeIn(multiply, shift=LEFT))

        # OG setup done.
        self.wait(2)

        eq_2 = Matrix([[1,"\\times",r"\dfrac{1}{\sqrt{2}}", "+", 0,"\\times",r"\dfrac{1}{\sqrt{2}}",], [1,"\\times",r"\dfrac{1}{\sqrt{2}}", "+", 0,"\\times",r"-\dfrac{1}{\sqrt{2}}",]], v_buff=1.75, h_buff=1).shift(DOWN*1.5) # cmon there gotta be a way to use •
        # eq_2 = Matrix([[2, "\\pi"], [-1, 1]])

        equals = MathTex(r"=").shift(LEFT*4.25).shift(DOWN*1.5)

        gropu = VGroup(eq_2[0][0:2], eq_2[0][3:6], eq_2[0][7:9], eq_2[0][10:13])
        gropu.shift(UP*0.5)

        X_s = VGroup(eq_2[0][1], eq_2[0][5], eq_2[0][8], eq_2[0][12])
        X_s.shift(LEFT*0.25)
        
        s = qubit_matrix[0][0].copy()
        e = hadamard_matrix[0][0].copy()

        u = eq_2[0][1].copy()
        b = eq_2[0][3].copy()
        f = eq_2[0][5].copy()
        d = eq_2[0][8].copy()
        v = prefix.copy()

        self.play(Transform(s, eq_2[0][0]), Transform(e, eq_2[0][2]), Transform(v, eq_2[0][2]), qubit_group.animate.shift(UP*1.5), hadamard_group.animate.shift(UP*1.5), multiply.animate.shift(UP*1.5), Unwrite(hadamard_label), Unwrite(qubit_label))

        p = prefix.copy()
        q = prefix.copy()
        t = prefix.copy()

        a = qubit_matrix[0][1].copy()
        c = qubit_matrix[0][0].copy()
        r = qubit_matrix[0][1].copy()
        l = hadamard_matrix[0][1].copy()
        i = hadamard_matrix[0][2].copy()
        g = hadamard_matrix[0][3].copy()
        
        self.play(Transform(a, eq_2[0][4]), Transform(l, eq_2[0][6]), Transform(p, eq_2[0][6]), Write(u))
        self.play(Transform(c, eq_2[0][7]), Transform(i, eq_2[0][9]), Transform(q, eq_2[0][9]), Write(b), Write(f))
        self.play(Transform(r, eq_2[0][11]), Transform(g, eq_2[0][13]), Transform(t, eq_2[0][13]), Write(d))#, Write(eq_2[0][12]), Write(eq_2[0][10]))
        self.play(Write(equals), Write(eq_2),
            # Unwrite(s),
            # Unwrite(a),
            # Unwrite(c),
            # Unwrite(r),
            # Unwrite(i),
            # Unwrite(l),
            # Unwrite(e),
            # Unwrite(g),
        )
        self.remove(s, a, c, r, e, l, i, g, u, b, f, d, p, q, t, v)

        eq_3 = Matrix([[r"\dfrac{1}{\sqrt{2}}"], [r"\dfrac{1}{\sqrt{2}}"]], v_buff=1.75).shift(DOWN*1.5)

        self.play(Transform(eq_2, eq_3), equals.animate.shift(RIGHT*2.75))
        self.wait()
















class PleaseSubMatrix(Scene):
    def construct(self):
        matrix = Matrix([[1, 2], [5, 4]])
        self.play(Write(matrix[0][0])) # this gets 1
        self.play(Write(matrix))
        self.wait()


class FormulaColor4(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)
