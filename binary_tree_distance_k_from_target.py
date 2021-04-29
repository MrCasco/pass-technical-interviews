class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

## MY SOLUTION ##
def binary_tree_distance_k_nodes(root, target, k):
    queue = [(root, 0)]
    levels = {}
    cur_levels = []
    cur_level = 0
    prev_level = 0
    node_level = float('-inf')
    res = []
    end = False
    while queue:
        node, cur_level = queue.pop(0)
        if cur_level == node_level+k:
            end = True
        if target == node:
            res += levels[cur_level-k]
            node_level = cur_level
        if node.left != None:
            queue.append((node.left, cur_level+1))
        if node.right != None:
            queue.append((node.right, cur_level+1))
        if cur_level != prev_level:
            if end and cur_level == node_level+k+1:
                return res+cur_levels[:]
            levels[prev_level] = cur_levels[:]
            cur_levels.clear()
        if node != None:
            cur_levels.append(node)
        prev_level = cur_level
    levels[cur_level] = cur_levels[:]
    if cur_level == node_level+k:
        res += cur_levels[:]
    return res

## BEST SOLUTION ##
def binary_tree_distance_k_nodes(root, target, K):
    from collections import deque

    def find_target(root):
        level = 0
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            level += 1
            for _ in range(n):
                node = queue.popleft()
                if node == target: # early exit if found target
                    return level
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)

    def bfs(root, res):
        level = 0
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            level += 1
            for _ in range(n):
                node = queue.popleft()
                if abs(target_level - level) == K: # found nodes K away from target
                    res.append(node)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        return res

    res = []
    if root:
        target_level = find_target(root)
        bfs(root, res)
    return res

if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def find_node(root, target):
        if not root: return
        if root.val == target: return root
        return find_node(root.left, target) or find_node(root.right, target)
    s = input().split()
    root = build_tree(iter(s))
    target = find_node(root, int(input()))
    K = int(input())
    print(' '.join(str(x.val) for x in sorted(binary_tree_distance_k_nodes(root, target, K), key=lambda node: node.val)))
