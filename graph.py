from manim import *
from manim.mobject.svg import tex_mobject


class MovingCameraOnGraph(GraphScene, MovingCameraScene):
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
        "y_label_decimal":3
    }
    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        self.camera.frame.save_state()

        self.setup_axes(animate=False)
        graph = self.get_graph(
            lambda x: 0.08,
                               color=BLACK,
                               x_min=0.06,
                               x_max=0.06,
                               )
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])

        # zero and 1
        zero = MathTex(
            r"|0\rangle",
        ).set_opacity(0.5)
        zero.bg=BackgroundRectangle(zero,fill_opacity=1,color=BLACK)
        one = MathTex(
            r"|1\rangle",
        ).set_opacity(0.5)
        one.bg=BackgroundRectangle(one,fill_opacity=1,color=BLACK)
        zero_group=VGroup(zero.bg,zero) #Order matters
        one_group=VGroup(one.bg,one) #Order matters
        zero_group.to_edge(UP)
        zero_group.shift(LEFT*3.7)
        one_group.to_edge(RIGHT)
        one_group.shift(DOWN*2.2)
        one_group.shift(LEFT*2)

        self.add(graph, zero_group, one_group)
        #self.play(self.camera.frame.animate.scale(0.5).move_to(dot_at_start_graph))
        #
        self.wait()

        arrow_diag = Arrow(dot_at_start_graph, np.array([0.8,2.4,0])).scale(1.1)
        self.play(Create(arrow_diag))
        
        zero_point_eight = MathTex(r"0.8", tex_to_color_map={"0.8": BLUE})
        zero_point_six = MathTex(r"0.6", tex_to_color_map={"0.6": BLUE})
        one_2 = MathTex(
            r"|1\rangle",
        )
        zero_2 = MathTex(
            r"|0\rangle",
        )
        plus = Tex("+")
        eq_1 = VGroup(zero_point_six, zero_2, plus, zero_point_eight, one_2).arrange(RIGHT)
        # self.add(zero_point_eight.copy(), zero_point_six.copy())
        ket = MathTex(
            r"0.6|0\rangle+0.8|1\rangle",
        )

        one_matrix = MathTex(r"\begin{bmatrix}0\\1\end{bmatrix}")
        zero_matrix = MathTex(r"\begin{bmatrix}1\\0\end{bmatrix}")

        equation_line_2 = MathTex(
            r"= 0.6\begin{bmatrix}0\\1\end{bmatrix} + 0.8\begin{bmatrix}1\\0\end{bmatrix}",
        )
        equation_line_3 = MathTex(
            r"= \begin{bmatrix}0.6\\0.8\end{bmatrix}",
        )
        equals = MathTex(r"=").shift(LEFT*2.25)

        
        eq_2 = VGroup(zero_point_six, zero_matrix, plus, zero_point_eight, one_matrix).arrange(RIGHT)
        zero_point_six_matrix = MathTex(r"\begin{bmatrix}0.6\\0\end{bmatrix}") # , tex_to_color_map={"0.6": BLUE}
        zero_point_eight_matrix = MathTex(r"\begin{bmatrix}0\\0.8\end{bmatrix}") # , tex_to_color_map={"0.8": BLUE} :(
        final_vector = MathTex(r"\begin{bmatrix}0.6\\0.8\end{bmatrix}") # eq 4

        eq_3 = VGroup(zero_point_six_matrix, plus, zero_point_eight_matrix).arrange(RIGHT)
        
        group = VGroup(eq_1, eq_2, eq_3, final_vector, equals)
        # group.arrange(DOWN, buff=1.0)
        group.shift(RIGHT*3.5)
        group.shift(UP*2.5)

        
        self.play(Write(eq_1))
                
        self.play(self.camera.frame.animate.scale(0.5).move_to(np.array([3,2,0])))
        self.wait()

        # self.play(Write(equation_line_2))
        # self.play(Write(equation_line_3))

        # Eq 2
        self.play(Transform(one_2, one_matrix), Transform(zero_2, zero_matrix), Write(equals))
        self.wait()

        # Eq 3
        self.play(FadeOutToPoint(zero_point_six, point=(3.2,2.9,0)), Transform(zero_2, zero_point_six_matrix))
        self.play(FadeOutToPoint(zero_point_eight, point=(4.5,2.2,0)), Transform(one_2, zero_point_eight_matrix))
        self.wait()

        # Eq 4
        self.play(Transform(one_2, final_vector), Transform(zero_2, final_vector), Transform(plus, final_vector), equals.animate.shift(RIGHT))
        self.wait()

        # BAKCK
        self.play(Restore(self.camera.frame), Unwrite(equals), 
            # move matrix left
            one_2.animate.shift(LEFT*1.5), 
            zero_2.animate.shift(LEFT*1.5), 
            plus.animate.shift(LEFT*1.5), 

        )
        # dashed lines
        line1 = Line(np.array([-4,-2.5,0]), np.array([0.8,-2.5,0])).set_color(YELLOW) # x
        line2 = Line(np.array([0.8,-2.5,0]), np.array([0.8,2.4,0])).set_color(YELLOW) # y
        dash1 = DashedVMobject(line1)
        dash2 = DashedVMobject(line2)
        b1 = Brace(line1, direction=line1.copy().rotate(PI / 2).get_unit_vector()).set_color(YELLOW).shift(DOWN*0.65).rotate(PI)

        b1text = b1.get_text("x coordinate: 0.6").set_color(YELLOW)

        b2 = Brace(line2, direction=line2.copy().rotate(PI / 2).get_unit_vector()).set_color(YELLOW).shift(RIGHT*0.65).rotate(PI)

        b2text = b2.get_text("y coordinate: 0.8").set_color(YELLOW)
        self.play(Create(dash1), Create(dash2))
        self.play(Create(b1), Write(b1text), Create(b2), Write(b2text))

class Graph2(GraphScene):
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
        "y_label_decimal":3
    }
    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        self.setup_axes(animate=False)
        graph = self.get_graph(
            lambda x: 0.8,
                               color=BLACK,
                               x_min=0.6,
                               x_max=0.6,
                               )
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])
        zero = MathTex(
            r"|0\rangle",
        ).set_opacity(0.5)
        zero.bg=BackgroundRectangle(zero,fill_opacity=1,color=BLACK)
        one = MathTex(
            r"|1\rangle",
        ).set_opacity(0.5)
        one.bg=BackgroundRectangle(one,fill_opacity=1,color=BLACK)
        zero_group=VGroup(zero.bg,zero) #Order matters
        one_group=VGroup(one.bg,one) #Order matters
        zero_group.to_edge(UP)
        zero_group.shift(LEFT*3.7)
        one_group.to_edge(RIGHT)
        one_group.shift(DOWN*2.2)
        one_group.shift(LEFT*2)
        arrow_diag = Arrow(dot_at_start_graph, np.array([0.8,2.4,0])).set_opacity(0.5)
        ket_small = MathTex(
            r"0.6|0\rangle+0.8|1\rangle", tex_to_color_map={"0.6": BLUE, "0.8": BLUE}
        ).set_opacity(0.5)
        ket_small.shift(RIGHT*3)
        ket_small.shift(UP*2.2)

        ket_small_2 = ket_small.copy()
        
        self.add(graph, zero_group, one_group, arrow_diag, ket_small, ket_small_2)
        # Initial graph setup over

        self.wait()

        zero_point_six = MathTex(r"0.6", tex_to_color_map={"0.6": BLUE})
        zero_point_eight = MathTex(r"0.8", tex_to_color_map={"0.8": BLUE})
        one_2 = MathTex(
            r"|1\rangle",
        )
        zero_2 = MathTex(
            r"|0\rangle +",
        )
        ket_group = VGroup(zero_point_six, zero_2, zero_point_eight, one_2).arrange(RIGHT)
        ket_group.scale(1.5)
        self.play(Transform(ket_small, ket_group))
        self.add(zero_point_eight, zero_point_six)

        self.wait()

        zero_point_six_eq_2 = MathTex(r"0.6^{2}", tex_to_color_map={"0.6": BLUE})
        zero_point_eight_eq_2 = MathTex(r"0.8^{2}", tex_to_color_map={"0.8": BLUE})
        plus = MathTex(r"+")
        eq_2_group = VGroup(zero_point_six_eq_2, plus, zero_point_eight_eq_2).arrange(RIGHT).scale(1.5).shift(DOWN)

        self.play(Transform(zero_point_six, zero_point_six_eq_2), ket_small.animate.shift(UP), zero_point_eight.animate.shift(UP))
        
        self.play(Transform(zero_point_eight, zero_point_eight_eq_2))
        self.play(Write(plus))

        self.wait()
        
        equals = MathTex(r"=").shift(LEFT*2.5, DOWN)
        eq_3_2 = MathTex(r"+")
        zero_point36 = MathTex(r"0.36").set_color(BLUE)
        zero_point64 = MathTex(r"0.64").set_color(BLUE)
        eq_3_group = VGroup(zero_point36, eq_3_2, zero_point64).arrange(RIGHT).scale(1.5).shift(DOWN)

        self.play(Transform(zero_point_six, zero_point36), Transform(zero_point_eight, zero_point64), Write(equals))
        # self.play(Transform(eq_2_group, eq_3_group))

        self.wait()

        equation_line_four = MathTex(r"1").scale(1.5).shift(DOWN).set_color(YELLOW).shift(LEFT*1.5)
        self.play(Transform(zero_point_eight, equation_line_four), Transform(zero_point_six, equation_line_four), Transform(plus, equation_line_four))

        self.wait()


class Graph3(GraphScene, MovingCameraScene):
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
        "y_label_decimal":3
    }
    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        self.camera.frame.save_state()

        self.setup_axes(animate=False)
        graph = self.get_graph(
            lambda x: 0.08,
                               color=BLACK,
                               x_min=0.06,
                               x_max=0.06,
                               )
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])
        zero = MathTex(
            r"|0\rangle",
        ).set_opacity(0.5)
        zero.bg=BackgroundRectangle(zero,fill_opacity=1,color=BLACK)
        one = MathTex(
            r"|1\rangle",
        ).set_opacity(0.5)
        one.bg=BackgroundRectangle(one,fill_opacity=1,color=BLACK)
        zero_group=VGroup(zero.bg,zero) #Order matters
        one_group=VGroup(one.bg,one) #Order matters
        zero_group.to_edge(UP)
        zero_group.shift(LEFT*3.7)
        one_group.to_edge(RIGHT)
        one_group.shift(DOWN*2.2)
        one_group.shift(LEFT*2)
        arrow_diag = Arrow(dot_at_start_graph, np.array([0.8,2.4,0]))
        line = Line(dot_at_start_graph, np.array([0.8,2.4,0])).set_opacity(0.5)
        ket_small = MathTex(
            r"0.6|0\rangle+0.8|1\rangle", tex_to_color_map={"0.6": BLUE, "0.8": BLUE}
        )
        ket_small.shift(RIGHT*3)
        ket_small.shift(UP*2.2)
        
        self.add(graph, zero_group, one_group, arrow_diag, ket_small)
        b1 = Brace(arrow_diag, direction=line.copy().rotate(PI / 2).get_unit_vector()).set_color(YELLOW)

        b1text = b1.get_text("length 1").set_color(YELLOW).rotate(PI/4).shift(RIGHT*0.5)
        self.play(Create(b1), Write(b1text))

        self.wait()


        # Rotate arrow around origin and draw the unit circle
        # camera zoom out

        # unit_circle = Circle(center_of_mass=graph.get_center)
        # unit_circle = Circle(radius=arrow_diag.get_length)
        # self.play(arrow_diag.rotate, 360*DEGREES, {"about_point":graph.get_center})
        # self.play(arrow_diag.animate.rotate(PI * 2, about_point=graph.get_center))
        # self.play(arrow_diag.animate.rotate(PI * 2), Create(unit_circle))
        # self.play(arrow_diag.animate.rotate_in_place(PI / 2))

    
class Circle2(Scene):
    def construct(self):
        circle = Circle(radius=3).set_color(BLUE)
        self.play(Create(circle), run_time=3)
        self.wait()

class ArcExample(Scene):
    def construct(self):
        self.play(Create(DashedVMobject(Arc(angle=PI))))
