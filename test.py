from manim import *

class TestScene(MovingCameraScene):
    def construct(self):
        t1 = Tex("{{x}}")
        t2 = Tex("{{x}} - {{x}}")
        # VGroup(t1, t2)\
        #     .scale(3)\
        #     .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(t1, t2),
            run_time=4
        )
        self.wait()
