# Control Flows
# Using If statements
# Controlling where code runs and does not, depending on our code making evaluations that return true or false

# If statements
age = int(input('How old are you?'))
driver_test = input('Have you passed your driving test?')
if age >= 18 and driver_test == 'yes':
    print('You can drive')
elif age < 18:
    print('Sorry you cannot drive')
else:
    print('Sorry you cannot drive')
