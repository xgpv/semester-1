# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
import money
pounds1 = int(input('How many pounds is the first sum of money?: '))
pence1 = int(input('How many pence is the first sum of money?: '))
money1 = money.Money(pounds1,pence1)

pounds2 = int(input('How many pounds is the second sum of money?: '))
pence2 = int(input('How many pence is the second sum of money?: '))
money2 = money.Money(pounds2,pence2)

print(f'The sum of {money1} and {money2} is {(money1+money2)}')
