# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Checks name and birth inputted are correct format.
        """
        if not isinstance(name, str):
            raise TypeError('Name given is not a string.')
        if not name:
            raise ValueError('Name cannot be empty.')
        if not isinstance(birth, date):
            raise TypeError('Birth given is not a date.')

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initals(self):
        """
        Capitalises all words and puts the capital ones into a returned string
        """
        self.name = self.name.title
        returnname = ''
        for i in self.name:
            if i.isupper():
                returnname += i
        return returnname
    def is_birthday(self):
        """
        Checks if birthday is today.
        """
        now = date.today()
        return (now.month, now.day) == (self.birth.month, self.birth.day)