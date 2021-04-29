def serialize(root):
    if not root: return []
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            for child in [node.left, node.right]:
                queue.append(child)
        else:
            res.append(None)
    while res[-1] == None:
        res.pop()
    return res

def deserialize(data):
    return data
