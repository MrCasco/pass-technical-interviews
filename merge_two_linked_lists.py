# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __repr__(self):
    #     cur = self
    #     res = []
    #     while cur != None:
    #         res.append(cur.val)
    #         cur = cur.next
    #     print(res)
    #     return str(self.val)

def init_list(arr):
    root = ListNode(arr[0])
    cur = root
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    cur.next = None
    return root

def print_list(list):
    cur = list
    res = []
    while cur != None:
        res.append(cur.val)
        cur = cur.next
    print(res)


def mergeTwoLinkedLists(l1, l2):
    cur = res = ListNode(0)
    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    cur.next = l1 or l2
    return res.next

l1 = init_list([1, 1, 2, 4])
l2 = init_list([0, 3, 5])
print_list(mergeTwoLinkedLists(l1, l2))

l1 = init_list([5, 10, 15, 40])
l2 = init_list([2, 3, 20])
print_list(mergeTwoLinkedLists(l1, l2))

l1 = init_list([-1, -1, 0, 1])
l2 = init_list([-1, 0, 0, 1, 1])
print_list(mergeTwoLinkedLists(l1, l2))

l1 = init_list([1, 1])
l2 = init_list([0])
print_list(mergeTwoLinkedLists(l1, l2))

l1 = init_list([1, 1, 1])
l2 = init_list([1, 2, 3, 4])
print_list(mergeTwoLinkedLists(l1, l2))

l1 = init_list([1])
l2 = init_list([1, 4, 6])
print_list(mergeTwoLinkedLists(l1, l2))
