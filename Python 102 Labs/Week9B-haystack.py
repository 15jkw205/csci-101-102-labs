# Jakob West
# CSCI 102 - Section E - Group A
# Week 9 - Lab B - Combing Through a Haystack
# References: U-Climb Mentor Tori Messimore
# Time: 30 minutes 

print('Enter a DNA string s:')
s = input("s>")
print('Enter a substring t:')
t = input("t>")
location = []
count = 0
for index in range(len(s)):
    if s[index:index + len(t)] == t: #indexes to length of sub-string
        count += 1
        location.append(index + 1) #add 1 for this list
    index += 1
    
print(f"The total number of substrings found is {count}")
print("OUPUT" , count)
print('The locations of these substrings in s are: ' , end='')
print(*location) #the asterix removes brackets 
print("OUPUT" , *location)
