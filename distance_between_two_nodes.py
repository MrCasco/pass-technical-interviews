from init_tree import initialize_tree

def distance(root, a, b):
    is_leaf = lambda n: n.left == n.right == None
    new_root = lca(root, a, b)
    return new_root


def lca(node, a, b):
    if not node:
        return
    if node.val == a or node.val == b:
        return node
    left = lca(node.left, a, b)
    right = lca(node.right, a, b)
    if left and right:
        return node
    return left or right

tree = [5,3,6,2,4,None,7,1,None,None,None,None,8]
print(distance(initialize_tree(tree), 1, 8))

"""
         5
        / \
       3   6
      / \   \
     2   4   7
    /         \
   1           8
"""
