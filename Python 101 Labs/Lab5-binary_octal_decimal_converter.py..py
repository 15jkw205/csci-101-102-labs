# Jakob West
# CSCI 101 - Section G (remote)
# Python Lab 5
# References: thispointer.com , TA Emma
# Time: 8 hours

c = ('1','2','3','4','5')
b = ('0','1') #tuples can be useful at the start of coding
o = ('0','1','2','3','4','5','6','7')
d = ('0','1','2','3','4','5','6','7','8','9') 

print('Welcome to the Binary-Octal-Decimal Converter')
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
print('Enter an option:')
print('1. Binary-Decimal Conversion')
print('2. Decimal-Binary Conversion')
print('3. Octal-Decimal Conversion')
print('4. Decimal-Octal Conversion')
print('5. Quit')

option = input("OPTION>")
continue_ = 'yes'
while continue_ == 'yes': #this is the condition to keep the main loop running
    
    if option not in c:
        print('ERROR: Please choose from [1-5]')
        print('OUTPUT Error')
        
    if option in c:    
        if option == '1':
            binary_num = input("BINARY-STR>")
            decimal_num = 0
            i = len(binary_num) - 1
            n = 0

            for bd in range(len(binary_num)):
                if binary_num[bd] in b: #need to loop through every index and check 
                    continue #to see if condition is satisfied.
                if binary_num[bd] not in b: #name indexes something that makes sense
                   print(f"ERROR: Input {binary_num} is NOT a binary number.")
                   print('OUTPUT ERROR')
                   break
                
            else: #this else statement is super powerful. Else partnered with for
                if binary_num[bd] in b:
                    while i >= 0:
                        decimal_num += int(binary_num[i]) * (2 ** n) #takes last digit 
                        i -= 1
                        n += 1
                    print(f"Binary {binary_num} is Decimal {decimal_num}")
                    print("OUTPUT" , decimal_num)

                
        elif option == '2':
            OG_decimal_num = input("DECIMAL-STR>")
            remainder = 0
            string = str()
            i = len(OG_decimal_num)
            
            for db in range(i): #don't do length minus one!
                if OG_decimal_num[db] in d:
                    continue
                if OG_decimal_num[db] not in d or OG_decimal_num[0] == '0':
                    print(f"ERROR: Input {OG_decimal_num} is NOT a decimal number.")
                    print('OUTPUT ERROR')
                    break
                
            else:
                if OG_decimal_num[db] in d:
                    decimal_num = int(OG_decimal_num)
                    while decimal_num > 0:
                        remainder = decimal_num % 2
                        decimal_num //= 2
                        string = str(remainder) + string #ensures that read backwards
                    print(f"Decimal {OG_decimal_num} is Binary {string}")
                    print("OUTPUT" , string)

            
        elif option == '3': #same thing as 1 but octal numbers
            octal_num = input("OCTAL-STR>")
            decimal_num = 0
            i = len(octal_num) - 1
            n = 0
                
            for od in range(len(octal_num)):
                if octal_num[od] in o:
                    continue
                if octal_num[od] not in o:
                    print(f"ERROR: Input {octal_num} is NOT an octal number.")
                    print('OUTPUT ERROR')
                    break
                
            else:
                if octal_num[od] in o:
                    while i >= 0:
                        decimal_num += int(octal_num[i]) * (8 ** n)
                        i -= 1
                        n += 1
                    print(f"Octal {octal_num} is Decimal {decimal_num}")
                    print("OUTPUT" , decimal_num)

             
        elif option == '4': #same thing as 2 but octal numbers 
            OG_decimal_num = input("DECIMAL-STR>")
            remainder = 0
            string = str()
            i = len(OG_decimal_num)
            n = 0
           
            for do in range(i):
                if OG_decimal_num[do] in d:
                    continue
                if OG_decimal_num[do] not in d or OG_decimal_num[0] == '0':
                    print(f"ERROR: Input {OG_decimal_num} is NOT a decimal number.")
                    print('OUTPUT ERROR')
                    break

            else:
                if OG_decimal_num[do] in d:
                    decimal_num = int(OG_decimal_num)
                    while decimal_num > 0:
                        remainder = decimal_num % 8
                        decimal_num //= 8
                        string = str(remainder) + string
                    print(f"Decimal {OG_decimal_num} is Octal {string}")
                    print("OUTPUT" , string)
        
                
        elif option == '5':
            print('OUTPUT Goodbye!')
            print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            break #exits out of all loops
        
    print('Would you like to continue (y/n)?')
    continue_ = input("CONTINUE>")
    continue_ = continue_.lower()
    
    if continue_ == 'y' or continue_ == 'yes':
        continue_ = 'yes' #don't do == !!!
        print('Welcome to the Binary-Octal-Decimal Converter')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('Enter an option:')
        print('1. Binary-Decimal Conversion')
        print('2. Decimal-Binary Conversion')
        print('3. Octal-Decimal Conversion')
        print('4. Decimal-Octal Conversion')
        print('5. Quit')
        option = input("OPTION>")
        
    else: 
        print('OUTPUT Goodbye!')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

'''
I spent 8 goddamn hours on this and even went to office hours. I thought I
knew what I was doing, but I am fucken done! If possible please let me know
how I can fix this code. I tried very hard, and could not get all outputs.
The best version of my code could execute all but 1 example outputs. I ended
up just naming my variables nonsense because not all of it would execute.
This assignment has determined that comp sci is not for me.
'''


"""
Updated notes 11/02/20:
Finally got the code to work! I am so happy. Originally got a 5.5/7 on this assignment,
but now I am finally content since my code passes all example executions. Maybe I should
stick with comp-sci as a minor. I'm not the best at coding, but I'm pretty good.
"""

