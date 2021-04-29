"""
Given a binary tree, find the depth of the shallowest leaf node. Return min depth

Example:
         1
       /   \
      2     3
     / \     \
    4   5     6**
     \   \
      7   8

Output:
2

Test Cases:
1 2 4 x 7 x x 5 x x 3 x 6 x x
0 x x
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root):
    queue = [(root, 0)]
    while queue:
        node, cur_level = queue.pop(0)
        if node.right == node.left == None:
            return cur_level
        if node:
            if node.right != None:
                queue.append((node.right, cur_level+1))
            if node.left != None:
                queue.append((node.left, cur_level+1))
    return cur_level

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
    print('Min depth is:', binary_tree_min_depth(root))
