# def split_primes(number):
#     def prime(num):
#         num = int(num)
#         return len([i for i in range(1, (num//2)+1) if num%i == 0]) == 1
#
#     def dfs(cur_num, path):
#         import ipdb; ipdb.set_trace()
#         if cur_num == '':
#             return 1
#         if prime(cur_num) and int(cur_num) >= 2:
#             # return dfs(number.replace(''.join(path+[cur_num]), '', 1), path+[cur_num])
#             return 1
#         temp = 0
#         for move in [cur_num[:i] for i in range(1, len(cur_num)+1)]:
#             if prime(move) and int(move) >= 2:
#                 temp += dfs(cur_num.replace(move, '', 1), path+[move])
#         return temp
#     res = []
#     primes = 0
#     for cur_num in [number[:i] for i in range(1, len(number)+1)]:
#         import ipdb; ipdb.set_trace()
#         if prime(cur_num) and int(cur_num) >= 2:
#             primes += dfs(number.replace(cur_num, '', 1), [cur_num])
#     return primes

def split_primes(s):
    n = len(s)
    def prime(num):
        num = int(num)
        if num < 2:
            return False
        return len([i for i in range(1, (num//2)+1) if num%i == 0]) == 1

    def dfs(start):
        # import ipdb; ipdb.set_trace()
        if start == n:
            return 1
        temp = 0
        for i in range(start + 1, n + 1):
            prefix = s[start: i]
            if prime(prefix):
                temp += dfs(i)
        return temp
    return dfs(0)


## BEST SOLUTION ##
primes = set()
for a in range(2, 1000):
    if all(a % p != 0 for p in primes):
        primes.add(a)

def split_primes(input_str):
    # boundary -> num of ways
    dp = [-1 for _ in range(len(input_str) + 1)]
    dp[0] = 1
    for i in range(1, len(input_str) + 1):
        dp[i] = sum(
            dp[i - n]
            # length of last number
            # at most 3 digits,
            # and cannot be more than the num of characters we have scanned
            for n in range(1, min(3, i) + 1)
            # not contain leading 0, and is prime
            if input_str[i - n] != '0' and int(input_str[i - n:i]) in primes
        )
    return dp[-1]

print(split_primes('53739'))
print(split_primes('31173'))
print(split_primes('31173'))
