# report.py
#
# Exercise 2.4
# import csv
# import os


# def read_portfolio(filename):
#     os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio


# print(read_portfolio('Data/portfolio.csv'))

# Exercise 2.5
import csv
import os


def read_portfolio(filename):
    os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        name = headers[0]
        for row in rows:
            dictPortfolio = {}
            dictPortfolio['name'] = row[0]
            dictPortfolio['price'] = float(row[2])
            dictPortfolio['shares'] = int(row[1])
            portfolio.append(dictPortfolio)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)

# exercise 2.6


def read_prices(filename):
    os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
    stocks = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = row[1]
                stocks[name] = price
            except:
                print("empty row")
    return stocks


prices = read_prices('Data/prices.csv')
print(prices)


# exercise 2.7
# calculate cost
cost = 0.0
for p in portfolio:
    cost += p['price'] * p['shares']
print("Total cost is", cost)

# calculate value
value = 0.0
for p in portfolio:
    value += p['shares'] * float(prices[p['name']])
print("Total value is", value)

print("Gain or loss is", round(value - cost, ndigits=2))
