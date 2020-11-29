# Jakob West
# CSCI 102 - Section E - Group A
# Week 7 - LabA - Checkerboard
# References: none
# Time: 30 minutes

print('What is the length of the sides of the checkerboard?')
length = int(input("LENGTH>"))
print('What are the strings with which to pattern it?')
first = input("FIRST>")
second = input("SECOND>")
first_list = []
second_list = []
n = 0
while n < length:
    if n % 2 == 0:
        first_list.append(first)
        second_list.append(second)
    if n % 2 == 1:
        first_list.append(second)
        second_list.append(first)
    n += 1

        
print(
    f"A checkerboard with side length {length}, first string is {first}, and "
    f"second string is {second} is:"
    ) #this f strings prints long statement on same line
n = 0
array = []
while n < length:
    if n % 2 == 0:
        print('OUTPUT' , first_list)
        array.append(first_list)
    if n % 2 == 1:
        print('OUTPUT' , second_list)
        array.append(second_list)
    n += 1
print('And the 2D array representation is:')
print('OUTPUT', array)

