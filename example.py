from PIL.Image import NONE
from typing_extensions import runtime

from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class Qubit1(Scene):
    def construct(self):
        tex = MathTex(
            r"\begin{bmatrix}0\\1\end{bmatrix}",
        )
        #tex.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        tex.scale(2)
        text = Tex("Statevector notation",color=YELLOW)


        # group = VGroup(tex, text)
        # group.arrange(DOWN)
        
        tex2 = MathTex(
            r"|1\rangle",
        )
        #tex.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        tex2.scale(2)
        text2 = Tex("Ket notation",color=YELLOW)

        texts = VGroup(text, text2).shift(DOWN*1.5)
        texs = VGroup(tex, tex2).shift(UP*0.5)


        # group2 = VGroup(tex2, text2)
        # group2.arrange(DOWN)
        #group2.to_edge(RIGHT)
        tex2.shift(3*RIGHT)
        text2.shift(3*RIGHT)
        self.play(Write(tex))
        self.play(Write(text))

        self.wait(1)

        self.play(
            #group.animate.to_edge(LEFT),
            text.animate.shift(LEFT*3),
            tex.animate.shift(LEFT*3)
        )
        
        self.play(Write((Tex(":=")).shift(UP*0.5)), Write(tex2), Write(text2))

        q = Tex("The | and")
        s = Tex("are notation to")
        r = MathTex(r"\rangle")

        text3_1 = VGroup(q, r, s).arrange(RIGHT)
        text3_3 = Tex("denote that this is a quantum state")
        text3 = VGroup(text3_1, text3_3)
        text3.arrange(DOWN)

        text3.scale(0.5)
        
        text3.to_corner(DOWN, LEFT)
        #text=Tex("\\justifying {The | and > are notation  ${G}$  as a union of a finite number of line segments residing in  ${\\mathbb{{{C}}}}$ . By taking our earlier parametrization, we can create an almost trivial extension to  ${\\mathbb{{{R}}}}^{{{3}}}$ . In the following notation, we write a bicomplex number of a 2-tuple of complex numbers, the latter of which is multiplied by the constant  ${j}$ .  ${z}_{{0}}\\in{\\mathbb{{{C}}}}_{{>={0}}}$  is an arbitrary point in the upper half plane from which the contour integral begins. The function  ${\\tan{{\\left(\\frac{{{\\theta}-{\\pi}}}{{z}}\\right)}}}:{\\left[{0},{2}{\\pi}\\right)}\\to{\\left[-\\infty,\\infty\\right)}$  ensures that the vertices at  $\\infty$  for the Schwarz-Christoffel transform correspond to points along the branch cut at  ${\\mathbb{{{R}}}}_{{+}}$ .}")
        
        self.wait()
        text3.shift(RIGHT*4)
        text3.shift(UP*0.7)
        # self.play(Write(text3_1), runtime=0.5)
        # self.play(Write(text3_3), runtime=0.5)
        self.play(FadeIn(text3, shift=DOWN))
        self.wait()


class Qubit2(Scene):
    def construct(self):
        tex = MathTex(
            r"\begin{bmatrix}1\\0\end{bmatrix}",
        )
        #tex.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        tex.scale(2)
        text = Tex("Statevector notation",color=YELLOW)


        # group = VGroup(tex, text)
        # group.arrange(DOWN)
        
        tex2 = MathTex(
            r"|0\rangle",
        )
        #tex.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        tex2.scale(2)
        text2 = Tex("Ket notation",color=YELLOW)

        texts = VGroup(text, text2).shift(DOWN*1.5)
        texs = VGroup(tex, tex2).shift(UP*0.5)


        # group2 = VGroup(tex2, text2)
        # group2.arrange(DOWN)
        #group2.to_edge(RIGHT)
        tex2.shift(3*RIGHT)
        text2.shift(3*RIGHT)
        self.play(Write(tex), Write(text))

        self.wait(1)

        self.play(
            #group.animate.to_edge(LEFT),
            text.animate.shift(LEFT*3),
            tex.animate.shift(LEFT*3)
        )
        
        self.play(Write((Tex(":=")).shift(UP*0.5)), Write(tex2), Write(text2))
        self.wait()

class Intro(Scene):
    def construct(self):
        classical_bits = Tex("Classical bits")
        one = Tex("1").set_color(YELLOW)
        zero = Tex("0").set_color(YELLOW)
        classical_bits.shift(UP*3)
        one.shift(UP*2)
        zero.shift(UP*2)
        zero.shift(LEFT*2)
        one.shift(RIGHT*2)
        zero.scale(2)
        one.scale(2)
        quantum_bits_1 = Tex('Quantum bits')
        qubits = Tex(' ("qubits")')
        quantum_bits = VGroup(quantum_bits_1, qubits).arrange(RIGHT)
        tex = MathTex(
            r"\begin{bmatrix}\alpha \\\beta \end{bmatrix}",
        ).set_color(YELLOW)

        classical_bits.scale(0.85)
        quantum_bits.scale(0.85)
        quantum_bits.to_edge(LEFT)
        tex.scale(1.5)

        classical_group = VGroup(classical_bits, zero, one)
        quantum_group = VGroup(quantum_bits, tex)
        quantum_group.arrange(DOWN)
        quantum_group.shift(DOWN*2)
        
        quantum_bits.shift(UP*0.5)
        
        # self.play(
        #     Transform(classical_bits, one, zero, quantum_bits, tex),
        #     LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in tex]),
        # )
        self.play(Write(classical_group))
        self.wait()
        self.play(Write(quantum_bits_1))
        self.play(Write(qubits), Write(tex))

        text3 = Tex('known as "statevectors"').scale(0.65)
        text4 = Tex('for quantum state"').scale(0.5)

        footnote = VGroup(text3, text4).arrange(DOWN).set_opacity(0.5)
        footnote.to_corner(DOWN, RIGHT)
        footnote.to_edge(RIGHT)
        footnote.shift(UP)
        self.play(FadeIn(footnote, shift=DOWN),)
        self.wait()


class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))

class Graph1(MovingCameraScene):
    def construct(self):
        zero = MathTex(
            r"|0\rangle",
        )
        one = MathTex(
            r"|1\rangle",
        )
        zero.to_edge(UP)
        zero.shift(LEFT*2)

        START = np.array([-4,-4,0])
        END =  np.array([4,-4,0])
        line = Arrow(START, END)
        self.play(Create(line))
        self.play(Write(one))

        self.wait()

        START2 = np.array([-4,-4,0])
        END2 =  np.array([-4,4,0])
        arrow2 = Arrow(START2, END2)
        self.play(Create(arrow2))

        self.wait()

        arrow_diag = Arrow(np.array([-4,-4,0]), np.array([0.8,2.4,0]))
        self.play(Create(arrow_diag))
        ket = MathTex(
            r"0.6|0\rangle+0.8|1\rangle",
        )
        equation_line_2 = MathTex(
            r"= 0.6\begin{bmatrix}0\\1\end{bmatrix} + 0.8\begin{bmatrix}1\\0\end{bmatrix}",
        )
        equation_line_3 = MathTex(
            r"= \begin{bmatrix}0.6\\0.8\end{bmatrix}",
        )
        
        group = VGroup(ket, equation_line_2, equation_line_3)
        group.arrange(DOWN)

        self.play(Write(ket))
        self.wait()
        self.camera.frame.save_state()
        self.play(self.camera.frame.frame.animate.scale(0.5).move_to(np.array([-4,-4,0]), np.array([0.8,2.4,0])))
        #self.camera.moving_camera.MovingCamera
        #self.play(self.camera.moving_camera.MovingCamera.frame.animate.scale(0.5).move_to(np.array([-4,-4,0]), np.array([0.8,2.4,0])))

        #self.play(self.camera.frame.animate.scale(0.5).move_to(np.array([-4,-4,0]), np.array([0.8,2.4,0])))

        
        self.play(Write(equation_line_2))
        self.play(Write(equation_line_3))
        self.wait()


class RotateFunction1(Scene):
    def construct(self):
        dot_center=Dot()
        dot_below=Dot(color=RED).next_to(dot_center,DOWN*3)
 
        self.add(dot_center,dot_below)
        # self.play(dot_below.rotate,50*DEGREES,{"about_point":dot_center.get_center()})
        #                                                    np.array([0,0,0])
        # dot_below.animate(Rotate(50*DEGREES,{"about_point":dot_center.get_center()}))
        # dot_below.animate.
        self.wait()

class AnimateExample(Scene):
    def construct(self):
        arrow_diag = Arrow(np.array([-4, -4, 0]), np.array([0.8,2.4,0])).set_opacity(0.5)
        s = Square()
        self.play(Create(s))
        self.play(Create(arrow_diag))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(arrow_diag.animate.rotate(PI / 2))
        self.play(Uncreate(s))



class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,60,10),
        "x_labeled_nums": list(np.arange(2, 7.0+0.5, 0.5)),
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":3,
        "y_axis_label": MathTex(r"|0\rangle"),
        "x_axis_label": MathTex(r"|1\rangle"),
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
        	Create(graph),
            run_time = 2
        )
        self.wait()






class SimpleAnimation(Scene):
    def construct(self):
        triangle = Triangle()
        self.play(Create(triangle))
        self.wait(2)


class WriteStuff(Scene):
    def construct(self):
        example_text = Tex("This is some text", tex_to_color_map={"text": YELLOW})
        example_tex = MathTex(
            r"\begin{bmatrix}1\\2\end{bmatrix}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
