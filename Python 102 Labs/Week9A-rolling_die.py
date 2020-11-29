# Jakob West
# CSCI 102 - Section E - Group A
# Week 9 - Lab A - Rolling a Die
# References: U-Climb Mentor Tori Messimore
# Time: 30 minutes

import random #imports random number generator
print('Input the number of rolls to make:')
number = int(input("NUMBER>"))
print('Input the seed for the random number generator:')
seed = int(input("SEED>"))
count_list = []
counter = 0

random.seed(seed) #sets seed equal to user input
while counter < number:
    random_number = random.randint(1 , 6)
    count_list.append(random_number)
    counter += 1
print()    
print(f"Your {number} rolls follow:")
count_one = count_list.count(1) #counts number of times '1' appears in list
count_two = count_list.count(2)
count_three = count_list.count(3)
count_four = count_list.count(4)
count_five = count_list.count(5)
count_six = count_list.count(6)

print(f"OUPUT 1 occurred {count_one} times")
print(f"OUPUT 2 occurred {count_two} times")
print(f"OUPUT 3 occurred {count_three} times")
print(f"OUPUT 4 occurred {count_four} times")
print(f"OUPUT 5 occurred {count_five} times")
print(f"OUPUT 6 occurred {count_six} times")

    

