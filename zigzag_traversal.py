"""
Given a binary tree, return its level order traversal but alternate left to right order.

Example:
         1
      /     \
     2       3
    / \       \
   4   5       6
    \   \
     7   8

Output:
[
    [1],
    [3, 2],
    [4, 5, 6],
    [8, 7]
]

Explanation:
We flip each level only if number its not a pair, in this case we flip levels 1 and 3, assuming root is level 0

VALID TEST CASES
1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def zigzag_traversal(root):
    queue = [(root, 0)]
    levels = []
    cur_levels = []
    cur_level = 0
    prev_level = 0
    while queue:
        node, cur_level = queue.pop(0)
        if cur_level != prev_level:
            if prev_level%2 != 0:
                levels.append(cur_levels[:][::-1])
            else:
                levels.append(cur_levels[:])
            cur_levels.clear()
        if node.left != None:
            queue.append((node.left, cur_level+1))
        if node.right != None:
            queue.append((node.right, cur_level+1))
        if node != None:
            cur_levels.append(node)
        prev_level = cur_level
    levels.append(cur_levels[:][::-1])
    return levels

if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    root = build_tree(iter(input().split()))
    for level in zigzag_traversal(root):
        print(' '.join(str(x.val) for x in level))
