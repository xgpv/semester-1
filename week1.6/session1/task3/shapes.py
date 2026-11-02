# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid colour: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    """
    A subset of shapes, focusing on the Circle shap
    """
    def __init__(self, radius = 2.5, position = (0.0, 0.0), colour = 'red'):
        """
        Relates it to the superclass
        """
        self.set_radius(radius)
        super().__init__(Point(0.0, 0.0), 'red')
        self.radius = radius
        self.position = position
        self.colout = colour
    
    def set_radius(self, radius):
        """
        Checks the radius is the correct type
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a positive integer or float.')
        if radius < 0:
            raise ValueError('Radius must be greater than zero.')
        
    def __str__(self):
        """
        Returns a string of the properties 
        """
        return f'{self.colour} circle, radius {self.radius}, at {self.position}'
    def area(self, radius):
        return round((math.pi * radius **2), 3)
    def perimeter(self, radius):
        return round((2 * math.pi * radius), 3) 
