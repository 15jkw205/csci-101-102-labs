# Jakob West
# CSCI 102 - Section E - Group A
# Week 5 - Lab A - ASCII Carpet
# References: TA Becca
# Time: 45 Minutes 

print('Input the dimensions for the rug, and the character to print:')
width = int(input("WIDTH>"))
height = int(input("HEIGHT>"))
character = str(input("CHARACTER>"))
character += ' ' #adds a space to the character inputted 
iterations = 0 #initialize this variable 
print(f"A {width}x{height} rug with character {character}will look like:")

while iterations < height: #do while loop using height not width! 
    print("OUTPUT" , (character * width)) #multiplies character by width 
    iterations += 1 #adds one to keep loop going

    

    
    
    
    
    
