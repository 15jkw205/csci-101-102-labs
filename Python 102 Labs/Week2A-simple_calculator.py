# Jakob West
# CSCI 102 - E - Group A
# Week 2 - Lab A - Simple Calculator
# References: None
# Time: 2.5 hours
operand_one = 0.0 #Initialize all variables to zero
operand_two = 0.0
Sum = 0.0
diff = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

print('Input the first operand.')
operand_one = float(input("FIRST>")) #don't use int()
print('Input the second operand.')
operand_two = float(input("SECOND>"))

Sum = operand_one + operand_two
diff = operand_one - operand_two
product = operand_one * operand_two
quotient = operand_one // operand_two
remainder = operand_one % operand_two #gets remainder from division 

message = f""" 
The sum of {operand_one} and {operand_two} is {Sum:.1f} 
The difference of {operand_one} and {operand_two} is {diff:.1f}
The product of {operand_one} and {operand_two} is {product:.1f}
The quotient of {operand_one} and {operand_two} is {int(quotient)}
The remainder of {operand_one} and {operand_two} is {remainder:.2f}
"""
#Next time make sure that your python can ACTUALLY do f-strings. Don't be an idiot!
#Update python when needed; f-strings don't work on python 3.2!!!!!!!!!
#f""" is a good way to do f-strings on multiple lines 
print(message)





