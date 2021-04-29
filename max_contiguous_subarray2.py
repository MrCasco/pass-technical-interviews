"""
Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays.
The subarray from which this sum comes must contain at least 1 element.
"""

def arrayMaxConsecutiveSum2(inputArray):
    mx,curr=0,0
    if all_negatives(inputArray):
        prev = inputArray[0]
        mx = inputArray[0]
        for num in inputArray[1:]:
            prev = max(num, prev+num)
            mx = max(mx, prev)
        return mx

    for x in inputArray:
        curr+=x
        if curr<0: curr=0
        if curr>mx:mx=curr
    return mx

def all_negatives(arr):
    for x in arr:
        if x > 0:
            return False
    return True
