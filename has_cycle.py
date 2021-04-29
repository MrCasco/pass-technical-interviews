"""
Code to detect whether a linked list has a cycle or not
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    cur = head
    seen = set()
    while cur != None:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next
    return False
