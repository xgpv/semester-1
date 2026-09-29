"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Amrit Saggu
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
  monthly_amount = int(input("Input the amount of money you want to save monthly: "))
except:
  print("Invalid input")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
annual_amount = monthly_amount * 12
print (f"You will save £{annual_amount:.2f} yearly.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
print(f"Including interest, you will save £{annual_amount*1.008:.2f}")
