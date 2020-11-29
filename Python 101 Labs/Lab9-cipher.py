# Jakob West
# CSCI 101 - Section G (remote)
# Python Lab 9
# References: U-Climb Mentor Tori Messimore
# Time: 1 hour 15 minutes 

print('Input the string to encrypt:')
string = list(input("STRING>")) #use a list for the string since mutable
alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = alphabet.upper() #converts alphabet to uppercase
reverse_alpha = 'zyxwvutsrqponmlkjihgfedcba'
upp_reverse = reverse_alpha.upper()
cipher_list = []
for index in range(len(string)):
    if string[index].islower():
        for char in range(len(alphabet)):
            if string[index] != alphabet[char]:
                continue
            if string[index] == alphabet[char]:
               string[index] = reverse_alpha[char]
               cipher_list.append(string[index])
               break #without this break, it will keep checking an appending the index 
    elif string[index].isupper(): #must use if, elif, else
        for char in range(len(upper_alpha)):
            if string[index] != upper_alpha[char]:
                continue
            if string[index] == upper_alpha[char]:
                string[index] = upp_reverse[char]
                cipher_list.append(string[index])
                break
    else: #accounts for spaces, numbers, and special characters
        cipher_list.append(string[index])
i = 0
atbash_cipher = str()
while i < len(cipher_list):
    atbash_cipher += cipher_list[i] #converts the list into a string
    i += 1
print('Your Atbash ciper is:' , end=' ')
print(atbash_cipher)
print("OUTPUT" , atbash_cipher)
