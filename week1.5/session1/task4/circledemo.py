# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

import math 
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



# Finally, add code here to demonstrate use of Point
p = Point(3.0, 4.0)
print(p.x,p.y)
print(p.distance_to(5.0, 12.0))
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
