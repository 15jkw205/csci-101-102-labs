# Jakob West
# CSCI 101 - Section G (remote)
# Python Lab 6
# References: geekforgeeks.org, U-Climb Mentor John Henke
# Time: 45 minutes 
DNA = ('A','C','G','T') #A good way to start off code is with tuples listing variables#

print('Enter a DNA String (of length < 1000):')
string = input("STRING>")
a_count = 0 #initialize each variable
c_count = 0
g_count = 0
t_count = 0

for n in range(len(string)): #n does not need to be defined since the foor loop defines it
    if string[n] not in DNA:
        print('OUTPUT DNA string not valid')
        break #this breaks from all things asscoiated with for loop when condition is met 
    if string[n] in DNA:
        if string[n] == 'A': #checks to see if indicy is one of the letters in tuple
            a_count += 1 
        if string[n] == 'C':
            c_count += 1
        if string[n] == 'G':
            g_count += 1 
        if string[n] == 'T':
            t_count += 1
            
else: #this is the most important thing! Works similar to an else with an if statement
    print(f"OUTPUT {a_count} {c_count} {g_count} {t_count}") #f-strings as always 
    rna = string.replace('T','U') #.replace() function is a lifesaver 
    print("OUTPUT" , rna)
'''
The key takeway from this lab is that else statements can be used with for loops
and in conjunction with break, lines of code can be skipped. I wish I learned this earlier
for the binary lab, but now I know exactly how to finish my incomplete lab 5.
.replace() is also important. Tuples are a good way to organize code, and I should
practice writing pseudocode since this is the main thing I am having trouble with.
'''

               
