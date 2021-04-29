class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left and self.right:
            return 'Root: '+str(self.val)+' Childs: '+str(self.left.val)+' '+str(self.right.val)
        if self.left:
            return 'Root: '+str(self.val)+' Childs: '+str(self.left.val)+' None'
        if self.right:
            return 'Root: '+str(self.val)+' Childs: '+'None '+str(self.right.val)
        else:
            return 'Root: '+str(self.val)+' Childs: '+'None None'

def initialize_tree(arr):
    root = TreeNode(arr.pop(0))
    sons = [root]
    while sons:
        node = sons.pop(0)
        if node:
            if arr:
                node.left = TreeNode(arr.pop(0))
            if len(arr) >= 2:
                node.right = TreeNode(arr.pop(0))
            sons += [node.left, node.right]
    return root

def inorderSuccessor(root, target):
    if not root: return None
    def handler(n, cur_min, successor):
        if not n: return successor
        if cur_min > n.val > target:
            cur_min = n.val
            successor = n
        if is_leaf(n):
            return successor
        if n.val > target:
            return handler(n.left, cur_min, successor)
        return handler(n.right, cur_min, successor)
    is_leaf = lambda node: node and node.left == node.right == None
    return handler(root, float('inf'), None)

root = initialize_tree([8,6,19,4,5,9,20])
print(inorderSuccessor(root, 8))
