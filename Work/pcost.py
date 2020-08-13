# pcost.py
#
# Exercise 1.27

# redirect python path to current directory
# import os
# os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
# file = open('Data/portfolio.csv', 'rt')
# headers = next(file).split(',')
# cost = 0
# for line in file:
#     row = line.split(',')
#     cost = cost + (float(row[1]) * float(row[2]))

# print(f'Total cost {round(cost, ndigits=2)}')


# exercise 1.30

# import os

# def portfolio_cost(filename):
#     os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
#     file = open(filename, 'rt')
#     headers = next(file).split(',')
#     cost = 0
#     for line in file:
#         row = line.split(',')
#         # exercise 1.31
#         try:
#             cost = cost + (float(row[1]) * float(row[2]))
#         except ValueError:
#             print("missing values")
#     return round(cost, ndigits=2)

# cost = portfolio_cost('Data/missing.csv')
# print('Total cost:', cost)


# exercise 1.32

# import csv
# import os

# def portfolio_cost(filename):
#     os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
#     file = open(filename, 'rt')
#     rows = csv.reader(file)
#     headers = next(rows)
#     cost = 0
#     for row in rows:
#         try:
#             cost = cost + (float(row[1]) * float(row[2]))
#         except ValueError:
#             print("missing values")
#     return round(cost, ndigits=2)

# cost = portfolio_cost('Data/missing.csv')
# print('Total cost:', cost)

# exercise 1.33
import csv
import os
import sys


def portfolio_cost(filename):
    os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')

    file = open(filename, 'rt')
    rows = csv.reader(file)
    headers = next(rows)
    cost = 0
    for row in rows:
        try:
            cost = cost + (float(row[1]) * float(row[2]))
        except ValueError:
            print("missing values")
    return round(cost, ndigits=2)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
