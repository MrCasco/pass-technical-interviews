# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the
number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all
elements from list l that have a value equal to k.
"""
def removeKFromList(l, k):
    if not l:
        return l

    while l.value == k:
        l = l.next
        if l is None:
            return None

    parent = l
    cur = l.next
    while cur != None:
        if cur.value == k:
            parent.next = cur.next
        else:
            parent = cur
        cur = cur.next
    return l
