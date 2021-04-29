## BEST SOLUTION ##
def sumInRange(nums, queries):
    sums = [nums[0]] + [0 for _ in range(len(nums))]
    final_sum = 0
    for i in range(len(nums)):
        sums[i+1] = sums[i] + nums[i]
    for i, j in queries:
        final_sum += sums[j+1] - sums[i]
    return final_sum%((10**9)+7)

## NAIVE SOLUTION ##
def sumInRange(nums, queries):
    sums = 0
    for i, j in queries:
        sums += sum(nums[i:j+1])
    return sums%((10**9)+7)
