# Jakob West
# CSCI 101 - Section G (remote)
# Python Lab 7
# References: TA Emma, U-Climb Mentor John Henke
# Time: 2 hours

print('Input the number of rows and columns in the crop field:')
len_row = int(input("ROWS>"))
len_col = int(input("COLUMNS>"))
print('Input each row of the crop field.')
crop_list = []
for row in range(len_row):
    user_input = input(f"Row{row}>") #f-strings for input
    user_input = user_input.split() #converts string into a list
    crop_list.append(user_input)
row = 0
col = 0
is_watered = True #boolean expressions are useful
list_of_unwatered_crops = []
for row in range(len_row):
    for col in range(len_col):
        if crop_list[row][col] == 'w':
            continue
        else: #check all 8 directions
            if col != 0: #checks left 
                if crop_list[row][col - 1] == 'w':
                    continue
            if col != len_col - 1: #checks right
                if crop_list[row][col + 1] == 'w':
                    continue
            if col != len_col - 1 and row != len_row - 1: #checks bottom right
                if crop_list[row + 1][col + 1] == 'w':
                    continue
            if row != len_row - 1: #checks bottom
                if crop_list[row + 1][col] == 'w':
                    continue
            if row != 0: #checks top
                if crop_list[row - 1][col] == 'w':
                    continue
            if row != 0 and col != 0: #checks top left 
                if crop_list[row - 1][col - 1] == 'w':
                    continue
            if row != len_row - 1 and col != 0: # checks bottom left
                if crop_list[row + 1][col - 1] == 'w':
                    continue
            if col != len_col - 1 and row != 0: #checks top right
                if crop_list[row - 1][col + 1] == 'w':
                    continue
            # if it made it this far, the crop isn't watered
            is_watered = False
            list_of_unwatered_crops.append((row, col)) #this must be inside the for loop
            #this creates a tuple in a list
if is_watered == False:
    print('Not all crops are watered!')
    print("OUTPUT" , is_watered)
    print('The following crops are not watered:')
    print("OUTPUT" , list_of_unwatered_crops)
if is_watered == True:
    print('All crops are watered!')
    print("OUTPUT" , is_watered)
            

            
            
                
        
            
                    
            
        

    
    
