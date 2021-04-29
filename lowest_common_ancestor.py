def lowestCommonAncestor(root, p, q):
    # If node is null, return nothing
    if not root: return
    # If this node is one of the ones i'm looking for, return this node
    # because that's the LCA
    if root.val == q.val or root.val == p.val: return root
    # Search in the tree if p or q is on the left side
    l_node = lowestCommonAncestor(root.left, p, q)
    # Search in the tree if p or q is on the right side
    r_node = lowestCommonAncestor(root.right, p, q)
    # If both are on each branch, then return current node
    if l_node and r_node:
        return root
    # If both are on the same (left, right), then return the first who appeared in there
    return l_node or r_node
