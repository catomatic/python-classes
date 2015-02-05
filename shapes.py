#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Shape Area and Perimeter Classes - Create an abstract class called Shape and
# then inherit from it other shapes like diamond, rectangle, circle, triangle
# etc. Then have each class override the area and perimeter functionality to
# handle each shape type.

import traceback
import sys
import math
from abc import ABCMeta, abstractmethod


def squared(a):
    b = a * a
    return b


def herons(p, s1, s2, s3):
    # Use Heron's Formula to calculate triangle
    # area so only the 3 sides are required
    s = p / 2.0
    a = round(math.sqrt(s * ((s - s1) * (s - s2) * (s - s3))), 2)
    return a


class shape(object):
    __metaclass__ = ABCMeta

    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    @abstractmethod
    def size(self):
        return 'Area: {0} Perimeter: {1}'.format(self.area, self.perimeter)


class rectangle(shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def size(self):
        self.area = self.width * self.height
        self.perimeter = (self.width * 2) + (self.height * 2)
        x = super(rectangle, self).size()
        return '{0}'.format(x)


class square(shape):

    def __init__(self, sides):
        self.sides = sides

    def size(self):
        self.area = squared(self.sides)
        self.perimeter = self.sides * 4
        x = super(square, self).size()
        return '{0}'.format(x)


class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def size(self):
        self.area = round(math.pi * squared(self.radius), 2)
        self.perimeter = round((2 * math.pi) * self.radius, 2)
        x = super(circle, self).size()
        return '{0}'.format(x)


class diamond(shape):

    def __init__(self, sides, angle):
        self.sides = sides
        self.angle = angle

    def size(self):
        self.area = round(squared(self.sides) * math.sin(self.angle), 2)
        self.perimeter = self.sides * 4
        x = super(diamond, self).size()
        return '{0}'.format(x)


class triangle(shape):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def size(self):
        self.perimeter = self.side1 + self.side2 + self.side3
        self.area = herons(self.perimeter, self.side1, self.side2, self.side3)
        x = super(triangle, self).size()
        return '{0}'.format(x)


def main():
    try:
        r1 = rectangle(6, 10)
        r1.name = 'Rectangle'
        print r1.name
        print r1.size()

        print '-------------'

        s1 = square(10)
        s1.name = 'Square'
        print s1.name
        print s1.size()

        print '-------------'

        c1 = circle(8)
        c1.name = 'Circle'
        print c1.name
        print c1.size()

        print '-------------'

        d1 = diamond(13, 45)
        d1.name = 'Diamond'
        print d1.name
        print d1.size()

        print '-------------'

        t1 = triangle(5, 7, 3)
        t1.name = 'Triangle'
        print t1.name
        print t1.size()
    except Exception:
        print traceback.print_exc()
        sys.exit(2)
    finally:
        sys.exit()


if __name__ == '__main__':
    main()
