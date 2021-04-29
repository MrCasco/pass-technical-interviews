class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        cur = self
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
        return ''

def reverseList(head):
    cur = head
    res = []
    while cur != None:
        res.append(cur.val)
        cur = cur.next
    return createListFromArray(res[::-1])

def reverseList(head):
    if not head: return
    prev = None
    curr = head
    next = curr.next
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def createListFromArray(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return ListNode(arr[0])
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    return head

def init_list(arr):
    root = ListNode(arr[0])
    cur = root
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    cur.next = None
    return root

lst = init_list([1, 2, 3, 4, 5])
print(reverseList(lst))

lst = init_list([5, 4, 3, 2, 1])
print(reverseList(lst))
