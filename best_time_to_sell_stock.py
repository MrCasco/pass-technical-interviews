def maxProfit(prices):
    profit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[r]-prices[l] > profit:
            profit = prices[r]-prices[l]
        if prices[r] < prices[l]:
            l = r
        r += 1
    return profit
