#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Shape Area and Perimeter Classes - Create an abstract class called Shape and
# then inherit from it other shapes like diamond, rectangle, circle, triangle
# etc. Then have each class override the area and perimeter functionality to
# handle each shape type.
# https://github.com/karan/Projects

import traceback
import sys
import math


def squared(a):
    b = a * a
    return b


def herons(p, s1, s2, s3):
    # Use Heron's Formula to calculate triangle
    # area so only the 3 sides are required
    s = p / 2.0
    a = round(math.sqrt(s * ((s - s1) * (s - s2) * (s - s3))), 2)
    return a


class Shape(object):
    def __init__(self, name, color, **kwds):
        self.name = name
        self.color = color
        super(Shape, self).__init__(**kwds)

    def shape_name(self):
        return 'Name: {0}'.format(self.name)

    def shape_area(self):
        return 'Area: {0}'.format(self.area)

    def shape_perimeter(self):
        return 'Perimeter: {0}'.format(self.perimeter)

    def shape_color(self):
        return 'Color: {0}'.format(self.color)


class Rectangle(Shape):
    def __init__(self, width, height, **kwds):
        self.area = width * height
        self.perimeter = (width * 2) + (height * 2)
        super(Rectangle, self).__init__(**kwds)


class Square(Shape):
    def __init__(self, sides, **kwds):
        self.area = squared(sides)
        self.perimeter = sides * 4
        super(Square, self).__init__(**kwds)


class Circle(Shape):
    def __init__(self, radius, **kwds):
        self.area = round(math.pi * squared(radius), 2)
        self.perimeter = round((2 * math.pi) * radius, 2)
        super(Circle, self).__init__(**kwds)


class Diamond(Shape):
    def __init__(self, sides, angle, **kwds):
        self.area = round(squared(sides) * math.sin(angle), 2)
        self.perimeter = sides * 4
        super(Diamond, self).__init__(**kwds)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, **kwds):
        self.perimeter = side1 + side2 + side3
        self.area = herons(self.perimeter, side1, side2, side3)
        super(Triangle, self).__init__(**kwds)


def main():
    try:
        r1 = Rectangle(width=10, height=6, name='Rectangle', color='red')
        print(r1.shape_name())
        print(r1.shape_area())
        print(r1.shape_perimeter())
        print(r1.shape_color())

        print('-------------')

        s1 = Square(sides=10, name='Square', color='yellow')
        print(s1.shape_name())
        print(s1.shape_area())
        print(s1.shape_perimeter())
        print(s1.shape_color())

        print('-------------')

        c1 = Circle(radius=8, name='Circle', color='green')
        print(c1.shape_name())
        print(c1.shape_area())
        print(c1.shape_perimeter())
        print(c1.shape_color())

        print('-------------')

        d1 = Diamond(sides=13, angle=45, name='Diamond', color='blue')
        print(d1.shape_name())
        print(d1.shape_area())
        print(d1.shape_perimeter())
        print(d1.shape_color())

        print('-------------')

        t1 = Triangle(side1=5, side2=7, side3=3, name='Triangle', color='purple')
        print(t1.shape_name())
        print(t1.shape_area())
        print(t1.shape_perimeter())
        print(t1.shape_color())

        print('-------------')
    except Exception:
        print(traceback.print_exc())
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
