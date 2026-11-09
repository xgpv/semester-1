# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math
import pytest

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5

    # complete the implementation for
    # testing distance_to()
def test_init():
    p = Point(12,13)
    c = Circle(45, p)
    assert c.radius == 45
    assert c.centre == p

def test_area():
    p = Point(45, 12)
    c1 = Circle(9, p)
    c2 = Circle(1)
    assert c1.area() == pytest.approx(math.pi * 81)
    assert c2.area() == pytest.approx(math.pi)

def test_perimeter():
    p = Point(1, 0)
    c1 = Circle(4, p)
    c2 = Circle(2)
    assert c1.perimeter() == pytest.approx(math.pi * 8)
    assert c2.perimeter() == pytest.approx(math.pi * 4)

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
