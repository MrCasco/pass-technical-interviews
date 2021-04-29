class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def kthSmallest(root, k):
    # To traverse in order a binary tree, we must follow the next
    # path traversing: root.left, root, root.right
    def in_order_traversal(root):
        if not root: return
        # Traverse and append each node into res
        in_order_traversal(root.left)
        res.append(root.val)
        in_order_traversal(root.right)
    res = []
    in_order_traversal(root)
    # Once res is filled, return k-1 element
    return res[k-1]

right = TreeNode(5)
left = TreeNode(2, None, TreeNode(3))
root = TreeNode(4, left, right)
print(kthSmallest(root, 1))
