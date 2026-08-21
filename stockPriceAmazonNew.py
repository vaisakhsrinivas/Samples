def maxProfit(p):

    profit = 0
    if p:
        minval = p[0]
        for i in range(1, len(prices)):
            if p[i] < minval:
                minval = p[i]
            if p[i]-minval > profit:
                profit = p[i]-minval
    return profit




prices = [7,1,5,3,6,4]
print(maxProfit(prices))