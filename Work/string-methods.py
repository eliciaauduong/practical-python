# exercise 1.16

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'

symbols.lower()
# 'hpq,aapl,ibm,msft,yhoo,sco,goog'
symbols
# 'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'

lowersyms = symbols.lower()
symbols.find('MSFT')
# 13

symbols[13:17]
# 'MSFT'

symbols = symbols.replace('SCO', 'DOA')
symbols
# 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

name = '   IBM   \n'
name = name.strip()    # Remove surrounding whitespace
name
# 'IBM'
