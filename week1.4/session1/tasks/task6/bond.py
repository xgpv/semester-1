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

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    #pass # delete pass to write your code
    count = 0
    for i in intList:
        count += 1
        print(i)
        if i == 0:
            intList = intList[count:]
            print('First 0')
            count = 0
            for i in intList:
                count += 1
                print(i)
                if i == 0:
                    i = intList[i]
                    print('Second 0')
                    intList = intList[count:]
                    count = 0
                    for i in intList:
                        count += 1
                        print(i)
                        if i == 7: 
                            print('Final 7, therefore:')
                            return True
    print('No 007 in this order detected in list, therefore:')
    return False

# Check if the following lines of code produce the correct output
n = '\n'
print(f'{isBond([1, 2, 4, 0, 0, 7, 5])}{n}')   # True
print(f'{isBond([1, 0, 2, 4, 0, 5, 7])}{n}')   # True
print(f'{isBond([1, 7, 2, 0, 4, 5, 0])}{n}')   # False
