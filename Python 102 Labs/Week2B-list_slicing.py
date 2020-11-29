# Jakob West
# CSCI 102 - Section E - Group A
# Week 2 - Lab B - List Splicing
# References: stackoverflow.com
# Time: 30 minutes

print('Enter your string:')
the_str = list(input("STRING>")) #Make the inputed value a list
print("Enter four numbers to slice the string")
a = int(input("A>")) #int() to ensure numbers 
b = int(input("B>"))
c = int(input ("C>"))
d = int(input("D>"))
slice_1 = ''.join(the_str [a:b+1]) #go from a to b and add 1 
slice_2 = ''.join(the_str [c:d+1]) 
print("OUTPUT" , slice_1 + " " + slice_2)

#Used stackoverflow.com as a reference for learning about converting a list of characters to a string
#I find this method the most simple
# ''.join() is very handy for joining list of letters together
