# Worksheet 1.2: Task 1 Solution
import sys
try:  
  grade = int(input('Input the grade achieved, from 0-100: '))
except ValueError: 
  sys.exit('Error!')

if grade > 100 or grade < 0:
    sys.exit('Error!')
  45648
if grade >= 70:
  print(f'{grade} is a Distinction')
elif grade >=40:
  print(f'{grade} is a Pass')
else:
  print(f'{grade} is a Fail')
