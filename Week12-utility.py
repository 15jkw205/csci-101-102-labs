# Jakob West
# CSCI 102 - Section E - Group A
# Week 12 - Utility using Git and Incremental Development
# References: none
# Time:

#1
'''def load_file(filename): #need to run through each line of file 

lines = load_file("text.txt")
print("OUTPUT" , lines)
'''
#2
def update_string(first_string,second_string,index):
    updated_string = first_string[:index] + second_string + first_string[(index + 1):]
    print("OUTPUT" , updated_string)
    
#3 
'''def find_word_count(word_list,string):
    count = 0
    #call in load file (1st function)
    if string in word_list:
        count += 1
    return count
        
#4
def score_finder(list1,list2,name):
    for index in range (list1):
        if name not in list1:
            return print('player not found')
        if name in list1:
            player_score = list2[index]
            return print(f"OUTPUT {name} got a score of {player_score}")

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

        



    
