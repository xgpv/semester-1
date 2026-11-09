"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""
import sys
try:
    travel_cost_input = float(input("Travel cost in pounds: "))
    food_cost_input = float(input("Food cost in pounds: "))
    accommodation_cost_input = float(input("Accommodation cost in pounds: "))
except ValueError:
    sys.exit('Invalid input')

print(f'Travel cost: £{travel_cost_input:.2f}\nFood cost: £{food_cost_input:.2f}\nAccomodation cost: £{accommodation_cost_input:.2f}\nAverage cost: £{(round(travel_cost_input+food_cost_input+accommodation_cost_input)/3):.2f}\nTotal cost: £{(accommodation_cost_input+travel_cost_input+food_cost_input):.2f}')

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
