# Jakob West
# CSCI 102 - Section E - Group A
# Week 5 - Lab B - Prime Factors
# References: TA Collette and TA Becca 
# Time: 2 hours 

response = 'yes' #set response equal to 'yes'
while response == 'yes': #first while loop
    print('Enter a positive integer to generate its Prime Factors:')
    number = int(input("INPUT>"))
    print('')
    print('The Prime Factors for the integer' , number , 'are:')
    var = 2 #initialize var to 2 and prime_list to []
    prime_list = []
    while var <= number:
        if number % var == 0:
            prime_list.append(var)
            number = number / var  #this while loop does prime facorization!
        elif number % var != 0:
            var += 1
    print("OUTPUT" , '' , end='') #'' = space and end='' writes next print statement on this line 
    print(*prime_list , sep='*') #*prime_list gets rid of brackets and commas of list
    print('') #sep='*' inserts asterixes between items in list 
    print('Do you want to get Prime Factors for another input? (y/n)')
    response = str(input())
    response = response.lower() #.lower() converts string to all lowercase letters
    if response == 'y' or response == 'yes':
        response == 'yes'
        print('-------------------------------------------------------------')
    else:
        print('-------------------------------------------------------------')
        print('GoodBye!')

#refer back to this lab for prime factorization in the future!

