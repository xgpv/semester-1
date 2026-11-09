"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
import sys 

destination = input("Where are you going to? ")

try:
    distance_miles_input = float(input("How many miles will you travel? "))
    time_hours_input = float(input("How many hours will the journey take? "))
except ValueError:
    sys.exit("Distance and travel time must be numbers.")

if distance_miles_input <= 0 or time_hours_input <= 0:
    sys.exit("Distance and travel time must both be greater than zero.")


print(f'Your journey to {destination} will require an average speed of {(distance_miles_input / time_hours_input):.2f} miles per hour.')
