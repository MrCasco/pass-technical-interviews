class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def isSymmetric(root):
    if not root or root.left == root.right == None:
        return True
    # Recursive call to check two symmetric nodes at a time
    return compare(root.left, root.right)

def compare(left, right):
    # If they're not equal, tree is not symmetric
    if left and right and left.val != right.val:
        return False
    # If both are null, we are still symmetric
    if left == right == None:
        return True
    # If left or right is None, return false because one it's None and the other one not
    if not left or not right:
        return False
    # If both are equal, then we check on they're child nodes, symmetricly
    for _l, _r in [(left.left, right.right), (left.right, right.left)]:
        # If we find a couple that's not equal, return False
        if not compare(_l, _r):
            return False
    # If everything was good up to this point, return True 
    return True

left = TreeNode(-42, right=TreeNode(76, left=None, right=TreeNode(13)))
right = TreeNode(-42, left=TreeNode(76, left=None, right=TreeNode(13)))
root = TreeNode(9, left, right)

print(isSymmetric(root))

left = TreeNode(2, TreeNode(3), TreeNode(4))
right = TreeNode(2, TreeNode(4), TreeNode(3))
root = TreeNode(9, left, right)

print(isSymmetric(root))

left = TreeNode(2, None, TreeNode(4))
right = TreeNode(2, None, TreeNode(3))
root = TreeNode(1, left, right)

print(isSymmetric(root))
