# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# # What features of Python does it rely on?

# The list fruit is not an empty list, so it is true by truthy-falsey logic. 
# Therefore, while True, print the output of the .pop() command. 
# The default argument is -1, so .pop() removes the final element of the list. 
# Since we are printing the output, the list has all its elements printed in reverse order.
# When list is empty, it is considered false, so the loop breaks and nothing more is printed.