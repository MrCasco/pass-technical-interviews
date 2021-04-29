def threeSum(nums):
    nums.sort()
    if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
        return []
    seen = set()
    length=len(nums)
    for i in range(length):
        l=i+1
        r=length-1
        target=nums[i]
        while l<r:
            if nums[l]+nums[r] == -target:
                seen.add((target,nums[l],nums[r]))
                while l < r and nums[l + 1] == nums[l]:
                    l += 1
                while l < r and nums[r - 1] == nums[r]:
                    r -= 1
                l+=1
                r-=1
            elif nums[l]+nums[r]>-target:
                r-=1
            else:
                l+=1
    return [[num for num in solution] for solution in seen]

print(threeSum([-1, 1, 1, 1, 1, 1, -2, 2, 3, 0]))
