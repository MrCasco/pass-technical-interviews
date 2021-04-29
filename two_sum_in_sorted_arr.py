"""
Given an array of integers sorted in ascending order, find two numbers that add
up to a given target. Return the indices of the two numbers in ascending order.
You can assume elements in the array are unique and there is only one solution.
Do this in O(n) time and with constant auxiliary space.

Input: [2 3 5 8 11 15], 5
Output: 0 1
"""

from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr)-1
    while right > left:
        if arr[left]+arr[right] == target:
            return [left, right]
        elif arr[left]+arr[right] > target:
            right -= 1
        elif arr[left]+arr[right] < target:
            left += 1
    return []

print(two_sum_sorted([2, 5, 10, 12, 30, 100], 22))
print(two_sum_sorted([1, 2, 3, 10, 20, 30, 50, 100], 101))
print(two_sum_sorted([100, 1000, 2001, 3000, 4000, 5000], 5001))
