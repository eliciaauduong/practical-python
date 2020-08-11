# exercise 1.22

symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']

symlist.append('RHT')
# ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

symlist.insert('AA')
# ['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

symlist.remove('MSFT')
# ['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']

symlist.append('YHOO')
# ['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']

symlist.index('YHOO')
# 4
symlist[4]
# 'YHOO'

symlist.count('YHOO')
# 2

symlist.remove('YHOO')
# ['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
