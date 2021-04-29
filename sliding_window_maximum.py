"""
This algorithm finds the maximum element among all k-length windows
"""

## NAIVE SOLUTION ##
# This code will get the minimum among all windows and then get the maximum from them
def sliding_window_maximum(nums, k):
    from bisect import insort
    # Initialize left and right pointer to 0 and k
    left, right = 0, k
    # This array will store all the minimum numbers
    minimums = []
    # While right is inside our array
    while right <= len(nums):
        # Insert to minimums array, the minimum from left to right
        insort(minimums, min(nums[left:right]))
        # Increment both pointers
        left += 1
        right += 1
    # Return the maximum from the minimums array
    return minimums[-1]

## BEST SOLUTION ##
def sliding_window_maximum(nums, k):
    from collections import deque
    q = deque() # stores *indices*
    res = [] # Here will lay all the maximum elements we can see in all k-sized windows
    for i, cur in enumerate(nums):
        # While there are elements in q and the last number is shorter than our current value
        # eliminate this element because it's shorter
        while q and nums[q[-1]] <= cur:
            q.pop()
        # This element is not shorter, so append it
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
