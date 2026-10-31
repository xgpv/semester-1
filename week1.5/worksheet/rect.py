# Worksheet 1.5: Rectangle Class
import datetime

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int):
            raise TypeError('Width must be a number.')
        if not isinstance(height, int):
            raise TypeError('Height must be a number.')
        if width < 1:
            raise ValueError('Width must be greater than 0.')
        if height < 1:
            raise ValueError('Height must be greater than 0.')
        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """
        Checks whether the rectange is a square 
        """
        return self.width == self.height
    def area(self):
        """
        Returns area of rectangle
        """
        return self.width * self.height
    def perimeter(self):
        """
        Finds perimeter of rectangle
        """
        return 2*self.width + 2*self.height