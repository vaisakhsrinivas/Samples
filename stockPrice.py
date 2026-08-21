prices = [55.39, 109.23, 48.29, 81.59, 105.53, 94.45, 12.24]
prices = iter(prices)

result = 0
minSofar = next(prices)
for price in prices:
    minSofar = min(minSofar, price)
    result = max (result, price - minSofar)

print (result)