# Week 1.5, Session 2: Task 2
import geometry


# Write code here to create and print a Point object,
# then create and print a Circle object
x = float(input('Input an x coordinate: '))
y = float(input('Input a y coordinate: '))
radius = float(input('Input a radius: '))
p = geometry.Point(x, y)
circle = geometry.Circle(radius, p)
print(circle.area())
print(circle.perimeter())