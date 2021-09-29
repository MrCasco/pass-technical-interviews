def canGetExactChange(targetMoney, denominations):
    mn = min(denominations)
    dp = [True] + [False]*(mn-1)
    for target in range(mn, targetMoney+1):
        can_get_change = False
        for coin in denominations:
            if target-coin >= 0:
                if dp[target-coin]:
                    can_get_change = True
                    break
        dp.append(can_get_change)
    return dp[-1]

print(canGetExactChange(94, [5, 10, 25, 100, 200]))
print(canGetExactChange(75, [4, 17, 29]))
print(canGetExactChange(75, [1]))
print(canGetExactChange(75, [4]))
