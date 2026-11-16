import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
namenum = int(input('How many random items from the list do you need? '))

# Display the chosen names, one per line
for name in random.sample(names, namenum):
    print(name)