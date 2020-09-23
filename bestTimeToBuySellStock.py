def buysell(prices):

    maxprofit = 0
    minprice = float('inf')

    for p in prices:
        minprice = min(minprice,p)
        maxprofit = max(maxprofit, p-minprice)

    return maxprofit



prices = [7,6,4,3,1,5]
print(buysell(prices))