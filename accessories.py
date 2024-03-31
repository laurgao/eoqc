from manim import *


class Questions(Scene):
    def construct(self):
        question = Text("?").scale(5)
        self.play(Write(question))
        self.wait(3)

class Title(Scene):
    def construct(self):
        x = Tex("By the end of this video,\\\\ you will know enough math to\\\\ program a quantum computer")
        y = Tex("Welcome to").scale(0.7)
        a = Tex("The essence of", tex_to_color_map={"essence": BLUE})
        b = Tex("the math behind").scale(0.4)
        c = Tex("quantum computing", tex_to_color_map={"quantum computing": BLUE})
        title = VGroup(y, a, b, c).arrange(DOWN).scale(1.25)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Transform(title, x))
        # self.wait(0.5)

        triangle = Triangle().set_color(BLACK).to_edge(UP + LEFT).set_fill(color=BLACK, opacity=1.0).shift(UP*3)
        self.add(triangle)
        self.play(triangle.animate.scale(25), run_time=5)
        self.wait()

class HadamardProbs(Scene):
    def construct(self):
        aa = Text("Probability of measuring 0: ").scale(0.75)
        bb = Text("Probability of measuring 1: ").scale(0.75)
        a = MathTex(r"\left ( \dfrac{1}{\sqrt{2}} \right ) ^2", "=", "\\dfrac{1}{2}")
        # b = MathTex(r"Probability of measuring 1: \left ( \dfrac{1}{\sqrt{2}} \right ) ^2", "=", "\\dfrac{1}{2}")
        
        a.set_color_by_tex("\\dfrac{1}{2}",YELLOW)
        b = a.copy()

        agroup = VGroup(aa, a).arrange(RIGHT, buff=0.5)
        bgroup = VGroup(bb, b).arrange(RIGHT, buff=0.5)

        group = VGroup(agroup, bgroup).arrange(DOWN, buff=1).scale(0.75)
        self.play(Write(group))

        self.wait(3)

class ColorByCaracter(Scene):
	def construct(self):
		text = MathTex("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		self.play(Write(text))
		self.wait(2)

class completeDefinition(Scene):
    def construct(self):
        a = Tex("What are quantum states? A complete definition:", tex_to_color_map={"complete definition": YELLOW}).scale(0.75)
        b = Text("- 2D")
        c = Text("- Vectors")
        d = Text("- Length 1")
        e = Text("- Can be complex")

        g = VGroup(a, b, c, d, e).arrange(DOWN, buff=0.5)
        self.play(Write(g))
        self.wait(2)

class OOOH(Scene):
    def construct(self):
        # self.camera.background_color = "#00FF00"

        a = Tex("Oooh that makes\\\\sense now!").shift(UP*0.25)

        # speech bubble
        speech_bubble = ImageMobject("speech bubble_2").scale(0.75)
        
        self.play(Write(a), FadeIn(speech_bubble))

        self.wait(0.5)

class Intro(Scene):
    def construct(self):
        # self.camera.background_color = "#00FF00"

        a = Tex("To all the cool kids that want to program quantum computers...").to_edge(DOWN).scale(0.9)
        b = Tex("This is what you have to learn:").to_edge(UP).scale(0.75)
        
        self.play(Write(a))
        self.wait(1)
        self.play(Write(b))
        self.wait(10)

class labels(Scene):
    def construct(self):
        a = Rectangle()
        a_label = Text("2D")
        a_label.next_to(a, RIGHT, buff=0.5)
        g = VGroup(a, a_label).set_color(YELLOW)
        self.play(Create(a), Write(a_label))
        self.wait(10)

class labelt(Scene):
    def construct(self):
        a = Rectangle(width=6)
        a_label = Text("complex")
        a_label.next_to(a, DOWN, buff=0.5).shift(LEFT*2)
        g = VGroup(a, a_label).set_color(YELLOW)
        self.play(Create(a), Write(a_label))
        self.wait(10)

class labelu(Scene):
    def construct(self):
        a = Rectangle().shift(LEFT*2)
        a_label = Text("unit length")
        a_label.next_to(a, RIGHT, buff=1.5)
        g = VGroup(a, a_label).set_color(BLUE)
        self.play(Create(a), Write(a_label))
        self.wait(10)
