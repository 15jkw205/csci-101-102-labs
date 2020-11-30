# Jakob West
# CSCI 102 - Section E - Group A
# Week 12 - Utility using Git and Incremental Development
# References: none
# Time: TA Colin

#1
def load_file(filename):
    with open(filename, 'r') as file:
       return file.readlines()
'''lines = load_file("test.txt")
print("OUTPUT" , lines) #why is this outputting an empty line???
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
    for i in range(len(list1)):
        new_list.append(list1[i].lower())
        
    for index in range(len(new_list)):
        if new_name != new_list[index]:
            print('player not found')
        if new_name == new_list[index]:
            player_score = list2[index]
            print(f"OUTPUT {new_name} got a score of {player_score}")
'''
#5
def union(list1,list2):
    mega_list = list1 + list2
    return mega_list


#6
def intersect(listA,listB):
    #use double for loops run through listA's first element then go
    #through all of list B's elements

#7
def not_in(list1,list2):
    #similar to intersect function

#8
def is_prime(integer):
    index = 1
    count = 0
    while index <= integer:
        if integer / index == type(int()):
            count += 1
        index += 1
    if count == 2:
        return True
    else:
        return False
    
      '''

        



    
