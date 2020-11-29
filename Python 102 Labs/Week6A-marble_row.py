# Jakob West
# CSCI 102 - Section E - Group A
# Week 6 - Lab A - Lost Marbles 
# References: none
# Time: 10 minutes 

print("Enter a string of X's and O's:")
marbles = list(input("MARBLES>")) #better to use a list than a string
marble_list =[]
for n in range(0,len(marbles)): #for statement w/ range function 
    if marbles[n] == 'O':
        marble_list.append(n) #append to list
    else:
        continue #continue loop if X is found
    
print(f"Oh no you lost your marbles! Don't worry they are at {marble_list}")
print('Your Marbles are at the following indices:')
print("OUTPUT" , marble_list)
