# Jakob West
# CSCI 101 - Section G (remote)
# Python Lab 11
# References: U-Climb Mentor Patrick
# Time: 2 hours

'''
Data Comparison:
Using data from census.gov, there is 60.7% white people in Aurora Colorado, and
using this lab data, 65.8% of white people are stopped. 65.8% is close to 60.7%.
16.0% of people in Aurora Colorado are black and the data shows that 23.9% of
people stopped were black. This percentage is slightly higher than the percent of
black people living in Aurora which seems to point to some racism. However this
percentage is lower than what I would have expected, but to be fair, Colorado does not
have as much diversity as states out East, so I bet that east coast states have a
more disproportionate number of stops of black people based on the news and the
Black Lives Matter Movement. Overall, Colorado is better than I would
have imagined.
'''

import csv #3 functions need to be defined 
def read_csv(file_path):
    new_list = []
    with open(file_path, 'r' ,encoding='utf8') as csv_file: #include encoding=''
        reader = csv.reader(csv_file)
        for row in reader:
            new_list.append(row)
    return new_list #creates a giant list of everything


def stops_by_race(content,race): #content is new list
    count = 0
    if race == 'ALL':
        return len(rows) - 1 #return total length of list
    for row in content:
        if row[8] == race: #column nine is race
            count += 1
    return count


def stops_by_sex(content,sex):
    count = 0
    if sex == 'ALL':
        return len(rows) - 1
    for row in content:
        if row[9] == sex: #column 10 is sex
            count += 1
    return count

    
