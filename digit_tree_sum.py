#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
"""
We're going to store numbers in a tree. Each node in this tree will store a single digit
(from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it

t = {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}

the output should be
digitTreeSum(t) = 218.
There are 3 numbers encoded in this tree:

    Path 1->0->3 encodes 103
    Path 1->0->1 encodes 101
    Path 1->4 encodes 14
    and their sum is 103 + 101 + 14 = 218
"""
def digitTreeSum(t):
    if not t:
        return 0
    stack = [t]
    parents = {t:None}
    sm = 0
    while stack:
        node = stack.pop()
        if node.left != None:
            stack.append(node.left)
            parents[node.left] = node
        if node.right != None:
            stack.append(node.right)
            parents[node.right] = node
        if node != None:
            if node.left == None and node.right == None:
                sm += get_number(parents, node)
    return sm

def get_number(parents, node):
    num = ''
    print('Cur node', node.value)
    while node != None:
        num += str(node.value)
        node = parents[node]
    return int(num[::-1])
