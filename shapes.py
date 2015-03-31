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


class Shape:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        return 'Area: {0} Perimeter: {1}'.format(self.area, self.perimeter)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.area = width * height
        self.perimeter = (width * 2) + (height * 2)


class Square(Shape):
    def __init__(self, sides):
        self.area = squared(sides)
        self.perimeter = sides * 4


class Circle(Shape):
    def __init__(self, radius):
        self.area = round(math.pi * squared(radius), 2)
        self.perimeter = round((2 * math.pi) * radius, 2)


class Diamond(Shape):
    def __init__(self, sides, angle):
        self.area = round(squared(sides) * math.sin(angle), 2)
        self.perimeter = sides * 4


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.perimeter = side1 + side2 + side3
        self.area = herons(self.perimeter, side1, side2, side3)


def main():
    try:
        r1 = Rectangle(6, 10)
        r1.name = 'Rectangle'
        print r1.name
        print r1

        print '-------------'

        s1 = Square(10)
        s1.name = 'Square'
        print s1.name
        print s1

        print '-------------'

        c1 = Circle(8)
        c1.name = 'Circle'
        print c1.name
        print c1

        print '-------------'

        d1 = Diamond(13, 45)
        d1.name = 'Diamond'
        print d1.name
        print d1

        print '-------------'

        t1 = Triangle(5, 7, 3)
        t1.name = 'Triangle'
        print t1.name
        print t1
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
