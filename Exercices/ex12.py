# vos import ici

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
    # attributs et méthodes ici...
    pass
        
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
    # attributs et méthodes ici...
    pass
        
def main():
    # votre code de test ici...
    pass

if __name__ == "__main__":
        main()