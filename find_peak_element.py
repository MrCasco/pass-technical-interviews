# First approach: O(n) solution
def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1 or nums[0] > nums[1]: return 0
    if nums[-1] > nums[-2]: return len(nums)-1
    for i in range(1, len(nums[1:])):
        if nums[i-1] < nums[i] > nums[i+1]:
            return i
    return -1

# Best solution: O(logn)
def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1 or nums[0] > nums[1]: return 0
    l, r = 0, len(nums)-1
    while r > l:
        mid = (l+r)//2
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid-1]:
            r = mid
        else:
            l = mid+1
    return -1
