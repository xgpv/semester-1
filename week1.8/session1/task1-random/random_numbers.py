import random

# Get user to input how many random numbers they want
numamount = int(input('How many numbers do you want? '))
# Generate this many random numbers
list = []
for num in random.sample(range(100000), numamount):
    list.append(num)
    print(num)
# Write the random numbers to a file named random.txt, one number per line
with open('random.txt', 'w') as out:
    for num in list:
        out.write(f'{num}\n')