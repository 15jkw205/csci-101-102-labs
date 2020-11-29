# Jakob West
# CSCI 102 - Section E - Group A
# Week 1 - Part B
# References: no one
# Time: 10 minutes

m = 0
h = 0
BMI = 0

print('Input your weight, in pounds.')
m = int(input('WEIGHT>')) # Always remember int()
print('Input your height, in inches.')
h = int(input('HEIGHT>'))
m = m * 0.454 # pounds to kilograms
h = h * 0.0254 # inches to meters
BMI = m / (h ** 2)
print('Your Body-Mass Index is:')
print ("OUTPUT" , round(BMI , 1)) # This is how you round to 1 decimal.
