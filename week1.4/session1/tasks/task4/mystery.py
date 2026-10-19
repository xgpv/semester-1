# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    """
    Takes a string and creates a count of how many characters are uppercase and lowercase.
    It returns the count of uppercase and lowercase characters.
    
    Argument: A string

    Outputs: Both counts in the form of a tuple     
    """
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X"))
print(mystery_func("[2, 3]"))

#The first is going to return (1,0)
#The second will return (0,0)
