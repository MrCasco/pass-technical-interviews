class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## MY SOLUTION ##
def tree_max_depth(root: Node) -> int:
    if not root:
        return 0
    return max(explore(root.left, 1), explore(root.right, 1))
def explore(node, depth):
    if not node:
        return depth
        return max(explore(node.left, depth+1), explore(node.right, depth+1))

## ALGO MONSTER ##
def tree_max_depth(root: Node) -> int:
    def dfs(root): # we don't actually need an inner function doing it here just keep consistent with other solutions
        # null node adds no depth
        if not root:
            return 0
        # depth of current node's subtree = max depth of the two subtrees + 1 provided by current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root)



def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input('Place each node followed by its children, just as if it was traversed like DFS, marked as x. E.g: 5 4 3 x x 8 x x 6 x x  ').split()), int)
    res = tree_max_depth(root)
    print('Max depth is:', res)
