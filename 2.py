from manim import *


class WriteEquation(Scene):
    def construct(self):
        text = MathTex(
            r"\begin{bmatrix}0\\0\end{bmatrix}",
        )
        self.play(Write(text))

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

class TwoDVectors(Scene):
    def construct(self):
        text = Tex("2D Vectors",color=YELLOW)
        text.to_edge(UP)

        vector_one = MathTex(
            r"\begin{bmatrix}0\\0\end{bmatrix}",
        )
        cross_1_1 = Line((-0.5, 1, 0), (0.5, -1, 0))
        cross_1_2 = Line((-0.5, -1, 0), (0.5, 1, 0))
        group_1 = VGroup(vector_one, cross_1_1, cross_1_2)
        cross_1_1.set_color(BLUE)
        cross_1_2.set_color(BLUE)

        vector_two = MathTex(
            r"\begin{bmatrix}1\\4\end{bmatrix}",
        )
        cross_2_1 = Line((-0.5, 1, 0), (0.5, -1, 0))
        cross_2_2 = Line((-0.5, -1, 0), (0.5, 1, 0))
        group_2 = VGroup(vector_two, cross_2_1, cross_2_2)
        cross_2_1.set_color(BLUE)
        cross_2_2.set_color(BLUE)

        vector_three = MathTex(
            r"\begin{bmatrix}1\\0\end{bmatrix}",
        )
        group_3 = VGroup(vector_three)

        vector_four = MathTex(
            r"\begin{bmatrix}\dfrac{1}{\sqrt2}\\\dfrac{1}{\sqrt2}\end{bmatrix}",
        )
        group_4 = VGroup(vector_four)

        vector_five = MathTex(
            r"\begin{bmatrix}0.6\\0.9\end{bmatrix}",
        )
        cross_5_1 = Line((-0.5, 1, 0), (0.5, -1, 0))
        cross_5_2 = Line((-0.5, -1, 0), (0.5, 1, 0))
        group_5 = VGroup(vector_five, cross_5_1, cross_5_2)
        cross_5_1.set_color(BLUE)
        cross_5_2.set_color(BLUE)

        vector_six = MathTex(
            r"\begin{bmatrix}0.2\\1\end{bmatrix}",
        )
        cross_6_1 = Line((-0.5, 1, 0), (0.5, -1, 0))
        cross_6_2 = Line((-0.5, -1, 0), (0.5, 1, 0))
        group_6 = VGroup(vector_six, cross_6_1, cross_6_2)
        cross_6_1.set_color(BLUE)
        cross_6_2.set_color(BLUE)

        group_1.scale(1.5)
        group_2.scale(1.5)
        group_3.scale(1.5)
        group_4.scale(1)
        group_5.scale(1.5)
        group_6.scale(1.5)

        group_1.shift(LEFT*4, UP*2.5)
        group_2.shift(RIGHT*1.5, UP*1.5)
        group_3.shift(RIGHT*5, UP*2.2)
        group_4.shift(LEFT*6, DOWN*2.5)
        group_5.shift(LEFT*1.5, DOWN*1.5)
        group_6.shift(RIGHT*4, DOWN*2.2)


        vectors = VGroup(vector_one, vector_two, vector_three, vector_four, vector_five, vector_six)
        cross_1s = VGroup(cross_1_1, cross_2_1, cross_5_1, cross_6_1)
        cross_2s = VGroup(cross_1_2, cross_2_2, cross_5_2, cross_6_2)
        self.play(Write(text))
        self.play(Write(vectors))
        self.wait()
        self.play(Create(cross_1s))
        self.play(Create(cross_2s))

