def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    return [get_nth_index(nums, target, True), get_nth_index(nums, target, False)]

def get_nth_index(nums, target, is_first):
    left, right = 0, len(nums)-1
    middle = (left+right)//2
    while left <= right:
        cur = nums[middle]
        if cur == target:
            if is_first:
                if middle == 0 or nums[middle-1] != target:
                    return middle
                right = middle-1
            else:
                if middle == len(nums)-1 or nums[middle+1] != target:
                    return middle
                left = middle+1
        elif cur < target:
            left = middle+1
        else:
            right = middle-1
        middle = (left+right)//2
    return -1

print(searchRange([3, 3, 3], 3)) # [0,2]
print(searchRange([3, 3, 3], 1)) # [-1,-1]
print(searchRange([0, 1, 2, 3, 4, 4, 5], 4)) # [4,5]
print(searchRange([5, 7, 7, 8, 8, 10], 8)) # [3,4]
