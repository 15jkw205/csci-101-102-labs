# Jakob West
# CSCI 101 - Section G
# Python Lab 3
# References: no one
# Time 30 minutes

hours = int(input("HOURS>"))
minutes = int(input("MINUTES>"))
minutes = (hours * 60) + minutes #convert everything into total minutes 
minutes = minutes - 40 
hours = minutes // 60 #returns quotient 
minutes = minutes % 60 #returns remainder 

if hours < 0:
    hours = 24 + hours 
if 0 <= minutes <= 9: #this ensures that minutes always have 2 digits 
    minutes = '0' + str(minutes) #adds zero to beginning of string if condition is met
print("OUTPUT" , hours , minutes)  
