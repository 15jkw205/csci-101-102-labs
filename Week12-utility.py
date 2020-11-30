# Jakob West
# CSCI 102 - Section E - Group A
# Week 12 - Utility using Git and Incremental Development
# References: TA Colin,
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# Time: 2.5 hours 

import math
#1

def load_file(filename):
    with open(filename, 'r') as file:
        reader = file.readlines()
        new_list = []
    for line in reader:
        updated_line = line.strip()
        new_list.append(updated_line)
    return new_list       
'''            
lines = load_file("test.txt")
print("OUTPUT" , lines)
'''

#2
def update_string(first_string,second_string,index):
    updated_string = first_string[:index] + second_string + first_string[(index + 1):]
    print("OUTPUT" , updated_string)
    
#3 
def find_word_count(word_list,string):
    count = 0
    index = 0 
    while index < len(word_list):
        count += word_list[index].count(string)
        index += 1 
    return count
'''
my_list = load_file("test.txt")
find_word_count(my_list , "me")
'''

#4
def score_finder(list1,list2,name):
    new_list = []
    new_name = name.lower()
    cap_name = new_name.capitalize()
    for i in range(len(list1)):
        lower_name = (list1[i]).lower()
        new_list.append(lower_name)
        
    for index in range(len(new_list)):
        if new_name == new_list[index]:
            player_score = list2[index]
            print(f"OUTPUT {cap_name} got a score of {player_score}")
            break
            
    else:
        print('OUTPUT player not found')
        
#5
def union(listA,listB):
    mega_list = listA + listB
    ultra_list = []
    for element in mega_list:
        if element not in ultra_list:
            ultra_list.append(element)
    return ultra_list

#6
def intersect(listA,listB):
    new_list = []
    for element in listA:
        if element in listB:
            new_list.append(element)
    return new_list
                   
#7
def not_in(listA,listB):
    new_list = []
    for element in listA:
        if element not in listB:
            new_list.append(element)
    return new_list

#8
def is_prime(integer):
    index = 2
    count = 0
    if integer == 1:
        return False
    while index <= math.sqrt(integer):
        
        if (integer % index) == 0:
            count += 1
            return False
        index += 1
    if count == 0:
        return True

        



    
