# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    zero_count = 0
    for num in intList:
        if num == 0 and zero_count < 2:
            zero_count += 1
        elif num == 7 and zero_count == 2:
            return True
    return False

# Check if the following lines of code produce the correct output
n = '\n'
print(f'{isBond([1, 2, 4, 0, 0, 7, 5])}{n}')   # True
print(f'{isBond([1, 0, 2, 4, 0, 5, 7])}{n}')   # True
print(f'{isBond([1, 7, 2, 0, 4, 5, 0])}{n}')   # False
