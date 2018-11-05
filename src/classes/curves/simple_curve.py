from src.classes.curves.curve import Curve
from src.classes.point import Point


def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n
    return 0;


class SimpleCurve(Curve):
    def __init__(self, n, tasks, a, b, p):
        Curve.__init__(self, n, tasks, a, b)
        self.p = p

    def add(self, point1, point2):
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y
        p = self.p
        if x1 != x2:
            k = (y2 - y1) * mulinv(x2 - x1, p)
            d = y1 - k * x1
            x3 = k * k - x1 - x2
            return Point(x3 % p, -(k * x3 + d) % p)
        else:
            k = (3 * x1 * x1 + self.a) * mulinv(2 * y1, p)
            d = y1 - k * x1
            x3 = k * k - x1 - x2
            return Point(x3 % p, -(k * x3 + d) % p)

    def mull(self, point1, number):
        new_point = point1
        for c in bin(number)[3:]:
            new_point = self.add(new_point, new_point)
            if c == '1':
                new_point = self.add(new_point, point1)
        return new_point

