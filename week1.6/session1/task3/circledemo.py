# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
import math
from shapes import Shape, Circle
from point import Point

p = Point(0,0)  # Initialises the variables needed for the Circle class
radius = 2.5
colour = 'red'

c = Circle(radius, p, colour)

print(f'{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')  # Lists all current properties of Circle

p = Point(1.6, 3.2) # Changes the point to test the code works
c.set_position(p)

print(f'Moving the circle...\n{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')

c.set_colour('green')  # Changes the colour to test the code works

print(f'Moving the circle...\n{c}\nArea = {c.area(radius)}\nPerimeter = {c.perimeter(radius)}')