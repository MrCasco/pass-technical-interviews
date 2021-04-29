def four_sum(nums, target):
    if len(nums) < 4:
        return []
    nums = sorted(nums)
    start, end = 0, 1
    left, right = 2, len(nums)-1
    res = []
    seen = set()
    while start < len(nums)-3:
        while end < len(nums)-2:
            second_target = target-(nums[start]+nums[end])
            while left < right:
                if nums[left]+nums[right] > second_target:
                    right -= 1
                elif nums[left]+nums[right] < second_target:
                    left += 1
                else:
                    ans = ''.join([str(x) for x in sorted([nums[start], nums[end], nums[left], nums[right]])])
                    if ans not in seen:
                        res.append([nums[start], nums[end], nums[left], nums[right]])
                        seen.add(ans)
                    right -= 1
                    left += 1

            end += 1
            left, right = end+1, len(nums)-1
        start += 1
        end = start+1
        left, right = end+1, len(nums)-1
    return res

print(four_sum([-3,-2,-1,0,0,1,2,3], 0))
print(four_sum([1,0,-1,0,-2,2], 0))
print(four_sum([1,0,-1,0,-2,2], 1))
