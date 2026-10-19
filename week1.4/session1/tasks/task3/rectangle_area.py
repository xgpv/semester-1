import sys
# function implementation

def rectangle_area (base, height):  # define suitable input data
    area = base * height               # implement the function
    return area             # return an appropriate value

# testing the function
try:
    base = int(input('Enter rectangle base, rounded to a whole number: '))
    height = int(input('Enter rectangle height, rounded to a whole number: '))
except ValueError:
    sys.exit('Invalid input entered')

print(f"Area is {rectangle_area(base, height)}")   # provide suitable data matching your inputs


def integerlist(startint):
    list = []
    list.append(startint)
    while True:
        startint-=1
        list.append(startint)
        if startint == 0:
            return (list[::-1])

try:
    startint = int(input('Input the starting integer of the list: '))
except ValueError:
    sys.exit('Incorrect value type')

print(f'The list to zero from the starting integer is {integerlist(startint)}')

def meanaverage(list):
    total = 0
    for i in range(len(list)):
        total = total+list[i]
    mean = total / len(list)
    return mean

list = []
while True:
    try:
        numA = input('Enter a number to add to the first set, or type "next" to continue: ')
        if str(numA.lower()) == 'next':
            break
        list.append(int(numA))
        print(f'The list now contains {list}')
    except ValueError:
        sys.exit('Incorrect input type entered')
        
print(f'The mean of the {list} is {meanaverage(list)}')