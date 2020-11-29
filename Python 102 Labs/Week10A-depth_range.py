# Jakob West
# CSCI 102 - Section E - Group A
# Week 10 Lab
# Reference: https://docs.python.org/3/library/csv.html, TA Emma
# Time: 1 hour 30 minutes 

import csv #imports csv library
split_list = []
with open('formations.csv' , 'r' , newline='') as csvfile: #have to do newline
    with open('formations_parsed.csv' , 'w' , newline='') as write_file:
        reader = csv.reader(csvfile) #defines reader
        writer = csv.writer(write_file)
        writer.writerow(['Depth','Start Depth','End Depth',
                         'Average Depth','Formation'])
        next(reader)  #skips first line
        for row in reader:
            split_list = row[0].split('-')
            average = (float(split_list[0]) + float(split_list[1])) / 2 
            writer.writerow([row[0],float(split_list[0]),float(split_list[1]),
                             round(average,1),row[1]]) #use brackets for writerow()
            
            
            
            
            
            
            
            
            

            

            
