# Week 1.2, Session 2: Task 6
#inputs
import sys
try:  
  machine_temp = int(input('What is the temperature of the machine to the nearest degree Celcius?: '))
  machine_pressure = int(input('What is the pressure of the machine to the nearest PSI?: '))
  machine_status = int(input('What is the operational status of the machine, 1/0?: '))
except ValueError():
  print('Invalid input')
  sys.exit()
#Status Determination
if machine_status == 1:
  machine_bool_status = True
else:
  machine_bool_status = False

#evaluating operating conditions
if machine_temp > 80:
  print('Machine temperature too high.')
  safety = False
elif machine_temp >= 50:
  print('Machine temperature is within safe limits.')
else:
  print('Machine temperature is low, no action needed.')

if machine_pressure > 100:
  print('Machine pressure too high.')
  safety = False
elif machine_pressure >= 70:
  print('Machine pressure is stable.')
else:
  print('Machine pressure is low, operation is normal.')

#Status check

if machine_bool_status:
  if not safety:
    print('The machine is running in unsafe conditions, shut down recommended.')
  else:
    print('The machine is running normally.')
else:
    print('Machine has stopped, no action needed.')
  
