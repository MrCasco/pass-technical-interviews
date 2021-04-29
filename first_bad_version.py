def firstBadVersion(n):
    left, right = 1, n
    mid = (left+right)//2
    while left < right:
        version = isBadVersion(mid)
        if version:
            right = mid
        else:
            left = mid+1
        mid = (left+right)//2
    return left
