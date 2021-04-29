"""
Given an array of integers, move all the 0s to the back of the array while maintaining
the relative order of the non-zero elements. Do this in-place using constant auxiliary space.

Input:
[1, 0, 2, 0, 0, 7]

Output:
[1, 2, 7, 0, 0, 0]
"""

## MY SOLUTION ##
def move_zeros(nums):
    if 0 not in nums:
        return nums
    left, right = 0, 1
    while nums[left] != 0:
        left += 1
        right = left+1
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums

## ALGO.MONSTER'S SOLUTION ##
def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

print(move_zeros([1, 0, 2, 0, 0, 0, 7]))
