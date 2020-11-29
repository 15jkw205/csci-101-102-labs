# Jakob West
# CSCI 102 - Section E - Group A
# Week 3 - Lab A - Twitter Decoding
# References: no one
# Time: 30 minutes

print('Enter the Tweet or Message abbreviation to decode.')
tweet = input("TWEET>") #inputs are initially strings 
if tweet == 'LOL':
    print('The decoded abbreviation is:') #There probably is a simpler way to condense all of this 
    print("OUTPUT LOL = laughing out loud")
elif tweet == 'BFN':
    print('The decoded abbreviation is:') #elif = else if 
    print("OUTPUT BFN = bye for now")
elif tweet == 'FTW': #Don't ever forget the ":" (colon)
    print('The decoded abbreviation is:')
    print("OUTPUT FTW = for the win")
elif tweet == 'IRL':
    print('The decoded abbreviation is:')
    print("OUTPUT IRL = in real life")
elif tweet == 'BTW': #== is used for equality not assingment like = is 
    print('The decoded abbreviation is:')
    print("OUTPUT BTW = by the way")
elif tweet == 'CU':
    print('The decoded abbreviation is:')
    print("OUTPUT CU = see you")
elif tweet == 'AFAIK':
    print('The decoded abbreviation is:')
    print("OUTPUT AFAIK = as far as I know")
elif tweet == 'IDK':
    print('The decoded abbreviation is:')
    print("OUTPUT IDK = I don't know")   
else:
    print("OUTPUT Sorry, don't know that one") #must use "" for phrases with contractions like don't and can't
