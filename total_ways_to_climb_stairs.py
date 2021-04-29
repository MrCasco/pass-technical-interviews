"""
You need to climb a staircase that has n steps, and you decide to get some extra
exercise by jumping up the steps. You can cover at most k steps in a single jump.
Return all the possible sequences of jumps that you could take to climb the staircase, sorted.


For n = 4 and k = 2, the output should be
climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
"""

def climbingStaircase(n, k):
    def get_path(parents, n):
        node = n
        way = []
        prev = node
        while node != None:
            prev = node
            node = parents[node]
            if node != None:
                way.append(prev-node)
        return way

    if n == 0:
        return [[]]
    stack = [0]
    parents = {0: None}
    ways = []
    while stack:
        cur = stack.pop()
        for step in range(1, k+1):
            if cur+step < n:
                parents[cur+step] = cur
                stack.append(cur+step)
            elif cur+step == n:
                parents[n] = cur
                ways.append(get_path(parents, n))
    return sorted(ways)

answer = climbingStaircase(20, 8)
print(answer, 'total unique ways', len(answer))
