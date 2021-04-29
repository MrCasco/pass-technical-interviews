from init_tree import initialize_tree

def longest_distance(root):
    def dfs(node):
        if is_leaf(node):
            return 0
        left, right = 0, 0
        if node.left:
            left = dfs(node.left)+1
        if node.right:
            right = dfs(node.right)+1
        lowest = max(left, right)
        ans[0] = max(ans[0], left+right)
        return lowest
    is_leaf = lambda n: n.left == n.right == None
    ans = [float('-inf')]
    dfs(root)
    return ans[0]

print(longest_distance(initialize_tree([1,2,3,4,5,None,7,8,None,None,11,None,None,9,None,None,10,12,None,None,13,None,None,None,14])))
print(longest_distance(initialize_tree([5,3,6,2,4,None,7,1,None,None,None,None,8])))
print(longest_distance(initialize_tree([1,2,3,None,None,None,None])))
