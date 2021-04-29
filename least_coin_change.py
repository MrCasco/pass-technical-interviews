def least_coin_change(amount, coins):
    coins.sort()
    options = [amount+1]*(amount+1)
    options[0] = 0
    for i in range(1, amount+1):
        for sz in coins:
            if i-sz < 0:
                continue
            if i-sz == 0:
                options[i] = 1
                break
            options[i] = min(options[i-sz]+1, options[i])
    if options[amount] == amount+1:
        return -1
    return options[amount]

print(least_coin_change(2584, [1, 2, 5, 10]))
