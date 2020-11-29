# Jakob West
# CSCI 101 - Section G
# Python Lab 2B
# References: none
# Time: 30 minutes

dollars = 0.0
convert_rate = 0.0
item_cost = 0.0

print('Input the currency to convert from')
currency = str(input("CURRENCY>")) #str for this part
print("Input today's convert rate for" , currency)
convert_rate = float(input("RATE>"))
print("Input the cost of the item you want to purchase")
item_cost = float(input("COST>")) #use floats

dollars = (convert_rate * item_cost) 
message1 = f"The item thats costs {item_cost:.1f} in {currency} currency costs ${dollars:.2f} in US dollars"
print(message1) #f-strings are needed for the $ sign 
message2 = f"OUTPUT ${dollars:.2f}" #print 2 decimal places using {var_1:.2f} w/ f-strings
print(message2)
