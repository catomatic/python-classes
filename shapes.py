#!/usr/bin/python
"""Shape class and inherited shapes"""

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

# Assignment:
# Shape Area and Perimeter Classes - Create an abstract class called Shape and
# then inherit from it other shapes like diamond, rectangle, circle, triangle
# etc. Then have each class override the area and perimeter functionality to
# handle each shape type.
# https://github.com/karan/Projects

from __future__ import print_function
import math


def squared(num):
    """Returns input squared"""
    result = num * num
    return result


def herons(perimeter, side1, side2, side3):
    """Returns triangle area using Heron's Formula"""
    spr = perimeter / 2.0
    area = round(math.sqrt(spr * ((spr-side1) * (spr-side2) * (spr-side3))), 2)
    return area


class Shape(object):
    """Creates a Shape"""
    def __init__(self, name, color, **kwargs):
        self.name = name
        self.color = color
        super(Shape, self).__init__(**kwargs)

    def shape_name(self):
        """Returns shape name"""
        return 'Name: {0}'.format(self.name)

    def shape_area(self):
        """Returns shape area"""
        return 'Area: {0}'.format(self.area)

    def shape_perimeter(self):
        """Returns shape perimeter"""
        return 'Perimeter: {0}'.format(self.perimeter)

    def shape_color(self):
        """Returns shape color"""
        return 'Color: {0}'.format(self.color)


class Rectangle(Shape):
    """Creates a Rectangle Shape"""
    def __init__(self, width, height, **kwargs):
        self.area = width * height
        self.perimeter = (width * 2) + (height * 2)
        super(Rectangle, self).__init__(**kwargs)


class Square(Shape):
    """Creates a Square Shape"""
    def __init__(self, sides, **kwargs):
        self.area = squared(sides)
        self.perimeter = sides * 4
        super(Square, self).__init__(**kwargs)


class Circle(Shape):
    """Creates a Circle Shape"""
    def __init__(self, radius, **kwargs):
        self.area = round(math.pi * squared(radius), 2)
        self.perimeter = round((2 * math.pi) * radius, 2)
        super(Circle, self).__init__(**kwargs)


class Diamond(Shape):
    """Creates a Diamond Shape"""
    def __init__(self, sides, angle, **kwargs):
        self.area = round(squared(sides) * math.sin(angle), 2)
        self.perimeter = sides * 4
        super(Diamond, self).__init__(**kwargs)


class Triangle(Shape):
    """Creates a Triangle Shape"""
    def __init__(self, side1, side2, side3, **kwargs):
        self.perimeter = side1 + side2 + side3
        self.area = herons(self.perimeter, side1, side2, side3)
        super(Triangle, self).__init__(**kwargs)


# pylint: disable=C0103
rect1 = Rectangle(width=10, height=6, name='Rectangle', color='red')
print(rect1.shape_name())
print(rect1.shape_area())
print(rect1.shape_perimeter())
print(rect1.shape_color())

print('-------------')

square1 = Square(sides=10, name='Square', color='yellow')
print(square1.shape_name())
print(square1.shape_area())
print(square1.shape_perimeter())
print(square1.shape_color())

print('-------------')

circle1 = Circle(radius=8, name='Circle', color='green')
print(circle1.shape_name())
print(circle1.shape_area())
print(circle1.shape_perimeter())
print(circle1.shape_color())

print('-------------')

dia1 = Diamond(sides=13, angle=45, name='Diamond', color='blue')
print(dia1.shape_name())
print(dia1.shape_area())
print(dia1.shape_perimeter())
print(dia1.shape_color())

print('-------------')

tri1 = Triangle(side1=5, side2=7, side3=3, name='Triangle',
    color='purple')
print(tri1.shape_name())
print(tri1.shape_area())
print(tri1.shape_perimeter())
print(tri1.shape_color())
