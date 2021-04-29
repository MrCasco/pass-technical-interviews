"""
Given a binary tree, return the rightmost node of each level.

Example:
         1**
      /     \
     2       3**
    / \       \
   4   5       6**
    \
     7**

Output:
[1, 3, 6, 7]

Explanation:
We check whether the current node its the rightmost from the level and append to the final result

VALID TEST CASES
1 2 4 x 7 x x 5 x x 3 x 6 x x   =>  [1, 3, 6, 7]
0 x x  =>  [0]
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root):
    queue = [(root, 0)]
    rightmost_nodes = []
    cur_level = 0
    prev_node = (root, 0)
    while queue:
        node, cur_level = queue.pop(0)
        # If this level is +1 deeper
        if cur_level != prev_node[1]:
            # Then append the last node from the previous level
            rightmost_nodes.append(prev_node[0])
        # If this node has left child, append it
        if node.left != None:
            queue.append((node.left, cur_level+1))
        # If this node has right child, append it
        if node.right != None:
            queue.append((node.right, cur_level+1))
        # Save an instance of the last node that was checked
        prev_node = (node, cur_level)
    # Append the very last node from the tree because the while loop has finished
    rightmost_nodes.append(prev_node[0])
    return rightmost_nodes

if __name__ == "__main__":
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    root = build_tree(iter(input().split()))
    print(' '.join(str(x.val) for x in binary_tree_right_side_view(root)))
