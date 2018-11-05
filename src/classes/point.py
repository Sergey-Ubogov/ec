class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'({self.x},{self.y})'
