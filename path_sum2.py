class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

def initialize_tree(arr):
    root = TreeNode(arr.pop(0))
    sons = [root]
    while sons:
        node = sons.pop(0)
        if node:
            if arr:
                val = arr.pop(0)
                if val:
                    node.left = TreeNode(val)
                else:
                    node.left = None
            if len(arr) >= 2:
                val = arr.pop(0)
                if val:
                    node.right = TreeNode(val)
                else:
                    node.right = None
            sons += [node.left, node.right]
    return root

def pathSum(self, root: TreeNode, target: int):
    def dfs(n, sm):
        if not n: return
        sm += n.val
        if sum_lib[sm-target] > 0:
            self.count += sum_lib[sm-target]
        sum_lib[sm] += 1
        dfs(n.left, sm)
        dfs(n.right, sm)
        sum_lib[sm] -= 1
    sum_lib = defaultdict(int)
    sum_lib[0] = 1
    self.count = 0
    dfs(root, 0)
    return self.count

print(pathSum(initialize_tree([1,-2,-3,1,3,-2,None,-1]), 3))
