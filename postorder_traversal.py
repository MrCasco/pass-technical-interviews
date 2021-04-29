# Postorder in binary tree
def postorderTraversal(root):
    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    res = []
    dfs(root)
    return res

#Postorder in n-ary tree
def postorderTraversal(root):
    def dfs(node):
        if not node: return
        for child in node.children:
            dfs(child)
        res.append(node.val)
    res = []
    dfs(root)
    return res
