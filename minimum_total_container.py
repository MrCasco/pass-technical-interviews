## NAIVE SOLUTION ##
def min_container_size(box_sizes, days):
    def dfs(day, box):
        if day == 0:
            return 0 if box == 0 else float('inf')
        # min total truck size
        res = float('inf')
        # number of boxes moved during the last day
        for last in range(1, box + 1):
            # max size of boxes moved during the last day
            mx = max(box_sizes[box - last:box])
            # inf + mx = inf, so no need to check
            res = min(res, dfs(day - 1, box - last) + mx)
        return res
    return dfs(days, len(box_sizes))

print(min_container_size([5, 4, 2, 4, 3, 4, 5, 4], 4))

## BEST SOLUTION ##
def min_container_size(box_sizes, days):
    end = len(box_sizes) + 1
    # boundary -> min total size
    dp = [inf for _ in range(end)]
    dp[0] = 0
    for day in range(1, days + 1):
        dp_ = [inf for _ in range(end)]
        # total number of boxes moved
        for box in range(1, end):
            # max size of boxes moved during the last day
            mx = -inf
            # number of boxes moved during the last day
            for last in range(1, box + 1):
                mx = max(mx, box_sizes[box - last])
                # inf + mx = inf, so no need to check
                dp_[box] = min(dp_[box], dp[box - last] + mx)
        dp = dp_
    return dp[-1]
