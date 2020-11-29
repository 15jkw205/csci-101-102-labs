# Jakob West
# CSCI 101 - Section G
# Python Lab 2A
# References: no one
# Time: 1 hour 30 minutes

print('Input the five lists of characters to be encrypted.')
str_1 = str(input("LIST1>")) #Had trouble at start since I was doing lists instead of strings
str_2 = str(input("LIST2>"))
str_3 = str(input("LIST3>")) #print as strings
str_4 = str(input("LIST4>"))
str_5 = str(input("LIST5>"))

str_1 = str_1[-2:] + str_1[:-2] #moves last 2 characters to front
str_2 = str_2[:-2] #cuts off last 2 characters 
half_3 = len(str_3) / 2 #useful method to figure out half on input
str_3 = str_3[int(half_3):] #gets back half of string
str_4 = str_4[2] + str_4[1] + str_4[0] + str_4[3:] #swaps 3rd and 1st char 
half_5 = len(str_5) / 2
str_5a = str_5[:int(half_5)] #first half 
str_5b = str_5[int(half_5):] #second half

master_string = str_5a + ' ' + str_1 + str_2 + str_3 + str_4 + ' ' + str_5b # ' ' is good for creating spaces
print('The encrypted message is:')
print('OUTPUT' , master_string)
 #Stop procrastinating on labs in future!!!
