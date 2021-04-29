## Some test cases ##
# 6 4 3 x x 5 x x 8 x x
# 6 4 3 x x 8 x x 8 x x
# 1 2 x x 3 x x
# x
# 7 7 7 x x x 7 x 7 x x

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## MY SOLUTION ##
# def valid_bst(root):
#     if not root:
#         return True
#     if left(root.left, (root.val, float('-inf'))) and right(root.right, (float('inf'), root.val)):
#         return True
#     return False
#
# def left(node, bounds):
#     if not node:
#         return True
#     if node.val >= bounds[1] and node.val <= bounds[0]:
#         return left(node.left, (node.val, float('-inf'))) and right(node.right, (bounds[0], node.val))
#     else:
#         return False
#
# def right(node, bounds):
#     if not node:
#         return True
#     if node.val >= bounds[1] and node.val <= bounds[0]:
#         return left(node.left, (node.val, bounds[1])) and right(node.right, (float('inf'), node.val))
#     else:
#         return False

## BEST SOLUTION ##
def valid_bst(root):
    def dfs(root, min_val, max_val):
        # empty nodes are always valid
        if not root:
            return True

        if not (min_val <= root.val <= max_val):
            return False

        # see notes below
        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    return dfs(root, -float('inf'), float('inf')) 

if __name__ =="__main__":
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    root = build_tree(iter(input().split()))
    if valid_bst(root): print('true')
    else: print('false')
