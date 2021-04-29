"""
Given a binary tree, return its level order traversal.
Input is the root node of the tree. The output should be a list of lists of integers,
with the ith list containing the values of nodes on level i, from left to right.

For example:
         1
      /     \
     2       3
    / \       \
   4   5       6
    \
     7

Output:
[
    [1],
    [2, 3],
    [4, 5, 6],
    [7]
]
"""
## VALID TEST CASES ##

# 1 2 4 x 7 x x 5 x x 3 x 6 x x
# 1 2 3 4 x x x x x

from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def level_order_traversal(root: Node) -> List[List[int]]:
    queue = [(root, 1)]
    levels = []
    cur_levels = []
    cur_level = 0
    prev_level = 1
    while queue:
        node, cur_level = queue.pop(0)
        if cur_level != prev_level:
            levels.append(cur_levels[:])
            cur_levels.clear()
        if node != None:
            cur_levels.append(node.val)
            if node.children:
                for child in node.children:
                    queue.append((child, cur_level+1))
        prev_level = cur_level
    if not levels and not cur_levels:
        return []
    levels.append(cur_levels)
    return levels

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
