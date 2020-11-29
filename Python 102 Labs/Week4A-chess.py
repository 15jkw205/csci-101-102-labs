# Jakob West
# CSCI 102 - Section E - Group A
# Week 4 - LabA - Missing Chess Pieces  
# References: none
# Time: 30 minutes 

print('Please enter the number of white chess pieces that you have of each type:')
kings = int(input("KINGS>"))
queens = int(input("QUEENS>"))
rooks = int(input("ROOKS>")) #ask to input variable
bishops = int(input("BISHOPS>"))
knights = int(input("KNIGHTS>"))
pawns = int(input("PAWNS>"))

kings = 1 - kings
queens = 1 - queens
rooks = 2 - rooks
bishops = 2 - bishops #simple math
knights = 2 - knights
pawns = 8 - pawns 
print('The output below provides the number of each type you have (over or under):')
print("OUTPUT" , kings , queens , rooks , bishops , knights , pawns)

#I'm still confused on what end='' does
#I tried messing around with it, and it doesn't do what I thought it did
