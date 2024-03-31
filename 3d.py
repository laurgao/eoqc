from manim import *


class Axes(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))
        self.wait()

class ThreeDLightSourcePosition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            resolution=(5, 12),
            fill_opacity=(0),
            stroke_color=BLUE

        )
        sphere2 = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            resolution=(2, 2),
            checkerboard_colors=(BLACK, BLACK),
            fill_opacity=(0.1),
            stroke_color=BLUE
        )
        sphere3 = sphere2.copy()
        sphere4 = sphere2.copy()
        # self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        group = VGroup(sphere, sphere2, sphere3, sphere4).scale(1.5)
        self.play(Create(group))
        self.wait()

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait()

class DrawArrow(ThreeDScene):
    def construct (self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=120 * DEGREES)
        text3d = MathTex(r"\sqrt{0.7}|0\rangle+\sqrt{0.3}i|1\rangle", tex_to_color_map={"i": YELLOW})
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.shift(LEFT*5, UP*3.5)

        # arrow = Arrow3D(ORIGIN, (np.sqrt(0.7), np.sqrt(0.3), 1)) og
        arrow = Arrow3D(ORIGIN, (np.sqrt(0.7)*3, np.sqrt(0.3)*3, 3)) # scaled by 3
        line = Line(ORIGIN, (np.sqrt(0.7)*3, np.sqrt(0.3)*3, 3))
        # self.add(axes)
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector()).set_color(YELLOW)

        b2text = b2.get_text("Length 1").set_color(YELLOW)
        self.play(Create(b2), Write(b2text))

        self.play(Create(arrow), Write(text3d))
        self.wait()

class Light(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            resolution=(20, 20),
            checkerboard_colors=(BLUE, BLUE),
            fill_opacity=(0.5),
            stroke_width=0,
        ).scale(1.5)
        
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(sphere))
        self.wait()
