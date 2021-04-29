def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            dic[num] += [i]
        else:
            dic[num] = [i]
    for i, num in enumerate(nums):
        if target-num in dic:
            if len(dic[num]) > 1:
                return [i, dic[target-num][1]]
            if i != dic[target-num][0]:
                return [i, dic[target-num][0]]

print('Indices which sum up to target:', twoSum([3, 0, 3], 6))
print('Indices which sum up to target:', twoSum([2, 7, 11, 15], 9))
print('Indices which sum up to target:', twoSum([3, 3], 6))
print('Indices which sum up to target:', twoSum([3, 2, 4], 6))
print('Indices which sum up to target:', twoSum([0, 1, 0, 0, 0, 0, 0, 0, 2], 3))
print('Indices which sum up to target:', twoSum([1, 0, 0, 0, 0, 0, 0, 2, 5], 7))
