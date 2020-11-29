# Jakob West
# CSCI 101 - Section G
# Python Lab 1B
#References: no one 
# Time: 10 minutes

time = 0.0
acceleration = 0.0

print('Input the amount of time required for the car to reach 60mph, in seconds.')
time = int(input("TIME>")) #Don't forget quotations in the future
time = time / 3600 #Don't forget to convert time from seconds to hours 
print('The acceleration of the car is (in miles/hour^2:')
acceleration = 60 / time #change in velocity / time = acceleration
print("OUTPUT" , round(acceleration)) #this rounds a variable to integer value






