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
# print(portfolio)

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
                pass
    return stocks


prices = read_prices('Data/prices.csv')
# print(prices)


# exercise 2.7
# calculate cost
# cost = 0.0
# for p in portfolio:
#     cost += p['price'] * p['shares']
# print("Total cost is", cost)

# # calculate value
# value = 0.0
# for p in portfolio:
#     value += p['shares'] * float(prices[p['name']])
# print("Total value is", value)

# print("Gain or loss is", round(value - cost, ndigits=2))


# exercise 2.9
def make_report(portfolio, prices):
    data = []
    for p in portfolio:
        name = p['name']
        shares = p['shares']
        price = float(prices[p['name']])
        change = float(prices[p['name']]) - p['price']
        s = (name, shares, price, change)
        data.append(s)
    return data


# exercise 2.10
report = make_report(portfolio, prices)
# exercise 2.11
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
