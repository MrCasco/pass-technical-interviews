## MY SOLUTION ##
def subarray_sum_divisible(arr, k):
    left, right = 0, len(arr)
    dp = [0, arr[0]]+[0]*(right-1)
    ways = 0
    for i in range(2, len(arr)+1):
        dp[i] = dp[i-1]+arr[i-1]

    while left < len(arr):
        if (dp[right]-dp[left])%k == 0:
            ways += 1
        if right-1 == left:
            left += 1
            right = len(arr)
            continue
        right -= 1
    return ways

## BEST SOLUTION ##
def subarray_sum_divisible(nums: List[int], K: int) -> int:
    remainders = Counter({0: 1})
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        cur_sum += num
        remainder = cur_sum % K
        compliment = (K - remainder) % K
        if compliment in remainders:
            count += remainders[compliment]
        remainders[compliment] += 1

    return count

print(subarray_sum_divisible([3,1,2,5,1], 3))
