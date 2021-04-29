class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def initialize_tree(arr):
    root = TreeNode(arr.pop(0))
    sons = [root]
    while sons:
        node = sons.pop(0)
        if node:
            if arr:
                if not arr[0]:
                    arr.pop(0)
                else:
                    node.left = TreeNode(arr.pop(0))
            if arr:
                if not arr[0]:
                    arr.pop(0)
                else:
                    node.right = TreeNode(arr.pop(0))
            sons += [node.left, node.right]
    return root
