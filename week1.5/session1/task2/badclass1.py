# A bad class implementation

# What does the runtime error mean?
# It says Point can only take two positional arguments, but three were given.

# How do we fix the code?
# Ammend the logic. The first argument for an 'init' must be self and every field constructed must have the self prefix.

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
