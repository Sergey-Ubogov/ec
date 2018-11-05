from src.classes.curves.curve import Curve


class SupersingularCurve(Curve):
    def __init__(self, a, b, c):
        Curve.__init__(self, a, b)
        self.c = c

    def add(self, point):
        print(1)
