# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if not t:
        return False
    stack = [t]
    sm = 0
    visited = {t:0}
    while stack:
        node = stack.pop()
        if node != None:
            sm = visited[node]+node.value
            if node.left != None:
                stack.append(node.left)
                visited[node.left] = sm
            if node.right != None:
                stack.append(node.right)
                visited[node.right] = sm
            if node.left == node.right == None:
                if sm == s:
                    return True
    return False

def hasPathSum(root, targetSum):
    if not root: return False
    def dfs(n, cur_sum):
        if is_leaf(n):
            return targetSum == cur_sum
        for child in [n.left, n.right]:
            if child:
                if dfs(child, cur_sum+child.val):
                    return True
    is_leaf = lambda node: node and node.left == node.right == None
    if is_leaf(root):
        return targetSum == root.val
    return dfs(root, root.val)
