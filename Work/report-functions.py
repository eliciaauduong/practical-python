# exercise 3.1 and 3.2
import csv
import os


def read_portfolio(filename):
    os.chdir('C:\\Users\\Elicia Au Duong\\Documents\\GitHub\\practical-python\\Work')
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # exercise 2.16
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'price': float(record['prices']),
                'shares': int(record['shares'])
            }
            portfolio.append(stock)
    return portfolio


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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
