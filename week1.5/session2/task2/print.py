# Week 1.5, Session 2: Task 2
import geometry


# Write code here to create and print a Point object,
# then create and print a Circle object
x = float(input('Input an x coordinate: '))
y = float(input('Input a y coordinate: '))
radius = float(input('Input a radius: '))
p = geometry.Point(x, y)
print(f'The point is at {p}. The distance from the origin is {p.distance()}')
circle = geometry.Circle(radius, p)
print(f'The circle of radius {radius} centred at point {p} has area {round(circle.area(), 3)} and perimeter {round((circle.perimeter()), 3)}')