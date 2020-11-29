# Jakob West
# CSCI 102 - Section E - Group A
# Week6B-visitors
# References: U-Climb Mentor John Henke
# Time: 1 hour
print('Enter the users separated by commas:')
users = input("USERS>")
print() #prints a blank line
n = 0
lower_list = []
start = 0 
while n < len(users):
    if users[n] == ',':
        name = users[start:n].lower() #goes from start to n when condition is met
        lower_list.append(name)
        start = n + 2 #ensures that space and comma will not be in start
        n += 1
    n += 1 #double count n (comma and space is now accounted for)
name = users[start:].lower() #adds on last name 
lower_list.append(name)
print('You entered the following users:')
print("OUTPUT" , lower_list)

new_list = []
for index in range(len(lower_list)): #use variable index instead of i or n for readability
    if lower_list[index] not in new_list: 
        new_list.append(lower_list[index])
        new_list.append(lower_list.count(lower_list[index])) #use the count function 
        
    
print('The Unique Users and their occurences are:')
print("OUTPUT" , new_list)

'''
Don't overthink these problems! Good practice would be to write out simple pseudocode
before starting lab. Consider the conditionals and loops that will be needed. Use
variables that are easier to understand such as index rather than n or i. Think like a
computer! Give yourself like an hour or 2 to tackle the code then if you are having
trouble, come into office hours for help. Iterated coding is a great way to go about
coding. Implement print statements to check for bugs. Practice finding bugs on your
own methodically rather than giving up like you did in Lab 5. Go back and fix lab 5
tonight. The count function is handy for counting the frequency of an element in a list.
Start working on homework earlier than later, so you don't stress yourself out. You need
more sleep! Don't give up on comp sci! Failure isn't falling down, it's falling down and
never getting back up.
'''


    

    
    
    
    
