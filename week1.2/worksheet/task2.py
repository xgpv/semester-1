# Worksheet 1.2: Task 2 Solution

import sys

from util import read_numbers

try:
    numbers = read_numbers()
except ValueError:
    sys.exit('Error: no numbers provided')
if len(numbers) == 0:
    sys.exit('Error: no numbers provided')

numbers = sorted(numbers)

#Calculating Median
median = len(numbers) // 2
if (len(numbers)) % 2 == 0:
    median = (numbers[median] + numbers[median - 1]) / 2
elif len(numbers) == 1:
    median = numbers[0]
median = numbers[len(numbers) // 2]


print(f'Minimum = {min(numbers)} \nMaximum = {max(numbers)} \nMean = {sum(numbers)/len(numbers)} \nMedian = {median}')