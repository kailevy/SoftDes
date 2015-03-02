"""Dealing with rectangles"""

## Point and print_point from Think Python
class Point(object):
    """Represents a point in 2-D space"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

def print_point(p):
    """Print a Point object in human-readable format"""
    template = "({x}, {y})"
    # See Python string formatting docs
    # https://docs.python.org/2/library/string.html#format-examples
    return template.format(x=p.x, y=p.y)


## TODO:
# - Implement Rectangle class using two points, instead of point + width/length
# - Implement print_rectangle
# - Implement find_center function

class Rectangle(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def print_rectangle(self):
        template = "Corner 1: {p1}, Corner 2: {p2}"
        print template.format(p1 = print_point(self.p1), p2 = print_point(self.p2))

point1 = Point(2,5)
point2 = Point(6,15)
rekt = Rectangle(point1, point2)
rekt.print_rectangle()

def find_center(my_rect):
    """
    Return the Point at the center of my_rect Rectangle

    Note: Your doctest may be different depending on your 
    implementation of Rectangle
    >>> p1 = Point()
    >>> p1.x = 0
    >>> p1.y = 0
    >>> p2 = Point()
    >>> p2.x = 6
    >>> p2.y = 4
    >>> rect = Rectangle()
    >>> rect.lower_left = p1
    >>> rect.upper_right = p2
    >>> print find_center(rect)
    (3.0, 2.0)
    """
    cen_x = (my_rect.p1.get_x() + my_rect.p2.get_x()) / 2.0
    cen_y = (my_rect.p1.get_y() + my_rect.p2.get_y()) / 2.0
    center = Point(cen_x, cen_y)
    return center

print print_point(find_center(rekt))

## Challenge problem:
def bounding_box(rects):
    """
    Given a list of Rectangles, return a Rectangle
    that contains all of them
    """
    pass