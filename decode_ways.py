## MY SOLUTION ##
def decode_ways(num):
    ways = 0
    if num[0] == '0':
        return 0

    if len(num) == 1:
        return 1

    def dfs(i):
        ways = 0
        if i < len(num) and num[i] == '0':
            return 0
        if i > len(num) or num[i:i+2] == '':
            return 1
        if int(num[i:i+2]) < 27 and len(num[i:i+2]) == 2:
            ways += dfs(i+2)
        return ways + dfs(i+1)
    return dfs(0)

## BEST SOLUTION WITH MEMOIZATION##
def decode_ways(num):
    if num[0] == '0':
        return 0
    if len(num) == 1:
        return 1
    def dfs(i, memo):
        ways = 0
        if i in memo:
            return memo[i]
        if i < len(num) and num[i] == '0':
            return 0
        if i > len(num) or num[i:i+2] == '':
            return 1
        if int(num[i:i+2]) < 27 and len(num[i:i+2]) == 2:
            ways += dfs(i+2, memo)
        ways += dfs(i+1, memo)
        memo[i] = ways
        return ways
    return dfs(0, {})

print('Total ways to decode 2524 are:', decode_ways('2524'))
print('Total ways to decode 06 are:', decode_ways('06'))
print('Total ways to decode 224 are:', decode_ways('224'))
print('Total ways to decode 255 are:', decode_ways('255'))
print('Total ways to decode 18 are:', decode_ways('18'))
print('Total ways to decode 123 are:', decode_ways('123'))
