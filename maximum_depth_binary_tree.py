def maxDepth(root):
    level = 0
    queue = [(root, level)]
    while queue:
        node, level = queue.pop(0)
        if node:
            for child in [node.left, node.right]:
                queue.append((child, level+1))
    return level
