# Jakob West
# CSCI 101 - Section G (Remote) 
# Python Lab 4
# References: none
# Time: 150 minutes 

print('Please enter the filing status:')
status = str(input("STATUS>")) #must be a string
print('Please enter the income earned:')
original_income = int(input("INCOME>"))

if status == 'single': #checks to see if status is single 
    if original_income <= 9325:
        tax_owed = int(original_income * 0.1) #take integer 
    elif 9326 <= original_income <= 37950:
        income = original_income - 9325
        tax_owed = int((9325 * 0.1) + (income * 0.15))
    elif 37951 <= original_income <= 91900:
        income = original_income - 37950 
        tax_owed = int((9325 * 0.1) + (28625 * 0.15) + (income * 0.25)) #divide up into increments
    elif 91501 <= original_income <= 191650:
        income = original_income - 91500
        tax_owed = int((9325 * 0.1) + (28625 * 0.15) + (53550 * 0.25) + (income * 0.28))
    elif 191651 <= original_income <= 416900:
        income = original_income - 191650
        tax_owed = int((9325 * 0.1) + (28625 * 0.15) + (53550 * 0.25) + (100150 * 0.28) + (income * 0.33))
    elif 416901 <= original_income <= 418400:
        income = original_income - 416900
        tax_owed = int((9325 * 0.1) + (28625 * 0.15) + (53550 * 0.25) + (100150 * 0.28) + (225250 * 0.33) + (income * 0.35))
    elif original_income >= 418401:
        income = original_income - 418400
        tax_owed = int((9325 * 0.1) + (28625 * 0.15) + (53550 * 0.25) + (100150 * 0.28) + (225250 * 0.33) + (1500 * 0.35) + (income * 0.396))
        
if status == 'joint': #checks to see if status is joint
    if original_income <= 18650:
        tax_owed = int(original_income * 0.1)
    elif 18651 <= original_income <= 75900:
        income = original_income - 18650
        tax_owed = int((18650 * 0.1) + (income * 0.15)) #same process as above
    elif 75901 <= original_income <= 153100:
        income = original_income - 75900
        tax_owed = int((18650 * 0.1) + (57250 * 0.15) + (income * 0.25))
    elif 153101 <= original_income <= 233350:
        income = original_income - 153100
        tax_owed = int((18650 * 0.1) + (57250 * 0.15) + (77200 * 0.25) + (income *0.28))
    elif 233351 <= original_income <= 416900:
        income = original_income - 233350
        tax_owed = int((18650 * 0.1) + (57250 * 0.15) + (77200 * 0.25) + (80250 * 0.28) + (income * 0.33))
    elif 416901 <= original_income <= 470700:
        income = original_income - 416900
        tax_owed = int((18650 * 0.1) + (57250 * 0.15) + (77200 * 0.25) + (80250 * 0.28) + (183550 * 0.33) + (income * 0.35))
    elif original_income >= 470701:
        income = original_income - 470700
        tax_owed = int((18650 * 0.1) + (57250 * 0.15) + (77200 * 0.25) + (80250 * 0.28) + (183550 * 0.33) + (53800 * 0.35) + (income * 0.396))

print(f"The tax owed by this person ({status} filing status) with {original_income} income is {tax_owed}") #f strings are the way to go
print("OUTPUT" , tax_owed)
percent_taxed = (tax_owed / original_income) * 100 #calculate percent
print(f"The percent of income paid in taxes is {percent_taxed:.2f}")
print(f"OUTPUT {percent_taxed:.2f}") #f strings yet again


