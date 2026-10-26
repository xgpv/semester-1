# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
# Week 1.5, Session 1: Task 3
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__ (self, x, y):
    # Add distance() method here
        self.x = x
        self.y = y
    # Add distance_to() method here
    def distance_to(self, x2, y2):
        """
        Takes another point in 2D space and finds the distance
        between the original and this new point
        """
        return math.hypot((self.x-x2), (self.y-y2))
    # (This will need a parameter representing another point)


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:
    """
    Takes the point as a centre of a circle, with a
    user-inputted radius.
    """
    def __init__(self, radius, centre):
        """
        Takes a circle, with a user-inputted radius and centre.        
        """
        self.radius = radius
        self.centre = centre
    def area(self, radius):
        """
        Will take the radius of the circle and raise it to
        the power of two, while multiplying it by pi.
        """
        return radius**2 * math.pi
    def perimeter (self, radius):
        """
        Will take the radius and multiply it by 2 * pi.
        """
        return radius * math.pi * 2


# Don't add any testing code to this file!
