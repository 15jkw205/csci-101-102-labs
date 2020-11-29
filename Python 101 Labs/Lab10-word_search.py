# Jakob West
# CSCI 101 - Section E - Group A
# Python Lab 10
# References: U-Climb Mentor Tori Messimore, TA Emma Loisel 
# Time: 1 hour 30 minutes

import random
print('Enter the length of the word you are looking for:')
length = int(input("LENGTH>"))
print('Enter the seed for the random number generator:')
seed = int(input("SEED>"))
random.seed(seed)
wol_list = []
long_length_list = []
integer = 0
with open('dictionary.txt' , 'r') as file:
    for line in file:
        line = line.strip() #gets rid of white space 
        if len(line) == length:
            wol_list.append(line)
        if len(line) == integer:
            long_length_list.append(line)
        elif len(line) > integer:
            integer = len(line)
            long_length_list = []
            long_length_list.append(line)
    print(f"There are {len(wol_list)} words in the dictionary with length {length}")
    print(f"OUPUT {len(wol_list)}")
    
    print(f"Here is one random word in the dictionary with length {length}")
    random_index = random.choice(wol_list) #do random.choice()
    print(f"OUTPUT \"{random_index}\"")
    print('The longest word(s) is/are:' , long_length_list)
    print("OUTPUT" , long_length_list)
    print()
    print('GoodBye!')

    
"""
In the future don't have backindented statements after a for loop
when you intend for the statements to be contained inside the for loop
"""
        
                
            
            
            
        


