# Jakob West
# CSCI 102 - Section E - Group A
# References: TA Adam
# Time: 35 minutes

print('Input a positive number for the siblings to consider:')
num = int(input("NUMBER>")) #input integer
print('The sibling(s) who will work with' , num , 'follow:')
if num % 2 == 1: #gets odd numbers 
    print("OUTPUT Jimmy")
if 10 <= num <= 100: #greater than and equal to 10 and less than and equal to 100
    print("OUTPUT Jared")
if (9 < num < 100): #Number must be double digit for this to work
    num_str = str(num) #convert input into string 
    index_1 = num_str[0] #indexes and retrieves first element of string 
    index_2 = num_str[1] #second element
    index_1 = int(index_1)
    index_2 = int(index_2)
    num_2 = index_1 + index_2 #adds the two digits
    if (num_2 == 6) or (num_2 == 8): #second if statement to meet these conditions
        print("OUTPUT Josephine")
