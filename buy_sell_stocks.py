def maxProfit(prices):
    buyPrice = float('inf')
    profit = 0
    for price in prices:
        if buyPrice > price:
            buyPrice = price
        else:
            profit = max(profit, price-buyPrice)
    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,1,1,1,2,1]))
