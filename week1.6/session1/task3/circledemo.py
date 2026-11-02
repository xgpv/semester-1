# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
import math
from shapes import Shape, Circle
from point import Point
p = Point(0,0)
radius = 2.5
colour = 'red'
c = Circle(radius, p, colour)
print(f'{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')
p = Point(1.6, 3.2)
c.set_position(p)
print(f'Moving the circle...\n{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')
c.set_colour('green')
print(f'Moving the circle...\n{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')