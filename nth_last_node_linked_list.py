class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

def init_list(arr):
    root = ListNode(arr[0])
    cur = root
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    cur.next = None
    return root

def nth_last_node(head, n):
    right = left = head
    count = 0
    while count < n:
        right = right.next
        count += 1
        if not right and count < n:
            return
    while right:
        right = right.next
        left = left.next
    return left

lst = init_list([5, 4, 3, 2, 1])
print(nth_last_node(lst, 3))

lst = init_list([1, 2, 3, 4, 5, 6, 7, 8])
print(nth_last_node(lst, 8))

lst = init_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(nth_last_node(lst, 10))

lst = init_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(nth_last_node(lst, 11))
