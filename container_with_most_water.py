"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

## NAIVE SOLUTION ##
def container_with_most_water(height):
    left, right = 0, len(height)-1
    global_max = 0
    heighest_min = height[0]
    while left < len(height)-1:
        if height[left] < heighest_min:
            left += 1
            right = len(height)-1
            continue
        else:
            heighest_min = height[left]
        cur_container = (right-left)*(min(height[left], height[right]))
        global_max = max(cur_container, global_max)
        right -= 1
        if right == left:
            left += 1
            right = len(height)-1
    return global_max

## BEST SOLUTION ##
def container_with_most_water(height):
    left, right = 0, len(height)-1
    global_max = 0
    while left < right:
        cur_container = (right-left)*(min(height[left], height[right]))
        global_max = max(cur_container, global_max)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return global_max


print(container_with_most_water([4,3,2,1,4]))
print(container_with_most_water([1,1]))
print(container_with_most_water([1,2,3]))
print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
