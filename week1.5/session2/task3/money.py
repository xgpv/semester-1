# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds: int, pence: int):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer, done
        # - pounds is not negative, done
        # - the pence parameter is an integer, done
        # - pence is not negative and not greater than 99, done
        # Raise appropriate exceptions if any of these are violated
        if not isinstance(pounds, int):
            raise TypeError('Pounds must be a whole number')
        if pounds < 0:
            raise ValueError('Pounds must be greater than 1')
        if not isinstance(pence, int):
            raise TypeError('Pence must be a whole number')
        if pence > 99 or pence < 0:
            raise ValueError('Pence must between 0-99')
        

        self.pounds = pounds
        self.pence = pence


    def __str__(self) -> str:
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return (f'£{self.pounds}.{self.pence:02d}') 

    def __add__(self, other) -> Money:
        """
        Adds this Money to another Money, returning the total.
        """

        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other, Money):
            raise ValueError('The second sum is not a valid amount')
        total = (self.pounds + other.pounds) * 100 + (self.pence + other.pence)
        return Money(total//100,total%100)