class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    if not root:
        return 0
    return explore(root.left, root.val) + explore(root.right, root.val) + 1

def explore(node, max_node):
    if not node:
        return 0
    if max_node < node.val:
        return explore(node.left, node.val) + explore(node.right, node.val) + 1
    return explore(node.left, max_node) + explore(node.right, max_node)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
