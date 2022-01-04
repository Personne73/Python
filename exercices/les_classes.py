import math


class Point2D(object):
    """
    Point dans un plan
    >>> p1 = Point2D(3, 4)
    >>> print(p1.x, p1.y)
    3 4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> print(p2.x, p2.y)
    0 0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> print(p1.x, p1.y)
    4 5
    >>> print(p1)
    Point2D(4,5)
    >>> print(p1.distance(p2))
    6.4031242374328485
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        return None

    def distance(self, point):
        return math.hypot((self.x - point.x), (self.y - point.y))

    def __str__(self):
        return f"Point2D({self.x},{self.y})"


class Vector2D(object):
    """
    Vecteur dans un plan
    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O,A)
    >>> v2 = Vector2D(O,B)
    >>> v3 = Vector2D(O,C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1+v2)
    Vector2D(2,1)
    >>> print(v1+v3)
    Vector2D(1,1)
    >>> print(v1-v3)
    Vector2D(1,-1)
    >>> print(v1+v3 == v2)
    True
    """
    def __int__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point2.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __str__(self):
        return "Vector2D({0},{1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector2D(Point2D(0, 0), Point2D(-self.x, -self.y))

    def __add__(self, other):
        return Vector2D(Point2D(0, 0), Point2D(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vector2D(Point2D(0, 0), Point2D(self.x - other.x, self.y - other.y))


def main():
    # votre code de test ici...
    pass


if __name__ == "__main__":
    main()
