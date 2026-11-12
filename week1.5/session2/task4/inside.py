# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry
x = int(input('Enter an x coordinate: '))    # Initialises the two variables needed for the Point class, which is needed for the Circle
y = int(input('Enter an y coordinate: '))
p = geometry.Point(x,y) 
radius = int(input('Enter the radius of a circle: '))    # Initialises the final variable needed for the Circle class
circ = geometry.Circle(radius, p)
x1 = int(input('Enter another x coordinate: '))  # Initialises the two variables needed for the final Point class
y2 = int(input('Enter another y coordinate: '))
q = geometry.Point(x1,y2)

if q in circ:
    print(f'The second point, coordinates {q}, is contained in the circle, centre {p} and radius {radius}.')
else:
    print(f'The second point, coordinates {q}, is NOT contained in the circle, centre {p} and radius {radius}.')