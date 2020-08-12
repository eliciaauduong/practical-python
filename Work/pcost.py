# pcost.py
#
# Exercise 1.27

# redirect python path to current directory
import os
os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')

file = open('Data/portfolio.csv', 'rt')
headers = next(file).split(',')
cost = 0
for line in file:
    row = line.split(',')
    cost = cost + (float(row[1]) * float(row[2]))

print(f'Total cost {round(cost, ndigits=2)}')
