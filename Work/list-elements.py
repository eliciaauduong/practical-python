# exercise 1.19

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist = symbols.split(',')

symlist[0]
# 'HPQ'
symlist[1]
# 'AAPL'
symlist[-1]
# 'GOOG'
symlist[-2]
# 'DOA'

symlist[2] = 'AIG'
# ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']

symlist[0:3]
# ['HPQ', 'AAPL', 'AIG']
symlist[-2:]
# ['DOA', 'GOOG']

mysyms = []
mysyms.append('GOOG')
mysyms
# ['GOOG']

symlist[-2:] = mysyms
symlist
# ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
