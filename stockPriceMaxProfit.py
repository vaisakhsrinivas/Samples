'''
Given an array of daily stock prices and a budget (in dollars),
calculate the maximum profit you could make by buying and selling the stock over the given period.

You may only sell after you buy.
You can only buy whole shares.
Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.
'''

def maxProfit(prices, budget):

    maxProfit = 0
    minPrice = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            shares = int(budget // minPrice)
            profit = shares * (prices[i] - minPrice)
            maxProfit = max(maxProfit, profit)
    return f"{maxProfit:.2f}"


print(maxProfit([5, 6], 50)) #should return "10.00".
print(maxProfit([8, 2, 5, 10], 20)) #should return "80.00".
print(maxProfit([4, 5, 3, 6], 20)) #should return "18.00".
print(maxProfit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200)) #should return "8.31".
print(maxProfit([15.38, 15.01, 14.99, 14.62, 14.28], 80)) #should return "0.00".
print(maxProfit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25)) #should return "73.80"