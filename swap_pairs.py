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

def print_list(list):
    cur = list
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)

def swapPairs(head: ListNode) -> ListNode:
    if not head: return
    if not head.next: return head
    prev = None
    cur = head
    nx = cur.next
    head = nx
    while cur and nx:
        cur.next = nx.next
        nx.next = cur
        if prev == None: prev = cur
        prev = cur
        cur = cur.next
        nx = None if not cur else cur.next
    return head

swapPairs(init_list([1,2,3,4]))
