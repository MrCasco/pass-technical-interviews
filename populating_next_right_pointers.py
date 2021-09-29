"""
Original Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def connect(root: 'Node') -> 'Node':
    if not root: return
    queue = [(root, 0)]
    prev_node = root
    prev_lvl = -1
    while queue:
        cur, lvl = queue.pop(0)
        if prev_lvl != lvl:
            prev_node.next = None
            prev_lvl = lvl
        else:
            prev_node.next = cur
        prev_node = cur
        for child in [cur.left, cur.right]:
            if child:
                queue.append((child, lvl+1))
    return root
