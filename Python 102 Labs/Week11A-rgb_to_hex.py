# Jakob West
# CSCI 102 - Section B
# Week 11 Lab
# References: U-Climb Mentor Patrick
# Time: 30 minutes

def to_hex(decimal_num):
    hex_nums = ('0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ,
                'A' , 'B' , 'C' , 'D' , 'E' , 'F') #0-15 values
    string = "" #empty string, don't use str()
    remainder = 0
    if decimal_num == 0:
        return '00'
    while decimal_num > 0:
        remainder = decimal_num % 16
        decimal_num //= 16
        string = str(hex_nums[remainder]) + string
    if len(string) == 1:
        string = '0' + string
        
    return string

def rgb_to_hex(rgb):
    hex_num1 = to_hex(rgb[0])
    hex_num2 = to_hex(rgb[1])
    hex_num3 = to_hex(rgb[2])
    final_hex_num = hex_num1 + hex_num2 + hex_num3
    return final_hex_num
