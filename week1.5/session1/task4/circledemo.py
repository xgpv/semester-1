# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
import math
import geometry 
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

x = float(input('Add a x coordinate: '))
y = float(input('Add the corresponding y coordinate: '))
p = geometry.Point(x,y)
radius = float(input("Add the circle's radius: "))
print(round(geometry.Circle.area(p, radius),4))
print(round(geometry.Circle.perimeter(p, radius),4))