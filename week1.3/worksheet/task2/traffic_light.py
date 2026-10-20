"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Amrit Saggu
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
#state = "red"
liststate = iter(states)
state = next(liststate)

time = 0



for systime in range(maxtime+1):
    print(f"Time {systime:03} State {state}")
    time += 1
    if time >= states[state]:
        time = 0
        try:
            state = next(liststate)
        except:
            liststate = iter(states)
            state = next(liststate)


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14