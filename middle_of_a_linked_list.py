class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


## MY SOLUTION ##
def middle_of_linked_list(head: ListNode) -> ListNode:
    if not head:
        return None
    if head.next == None:
        return head
    left, right = 0, -1
    cur = head
    while cur != None:
        right += 1
        cur = cur.next
    cur = head
    if right%2 != 0:
        right += 1
    while left != right//2:
        cur = cur.next
        left += 1
    return cur

## BEST SOLUTION ##
def middle_of_linked_list(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

if __name__ == '__main__':
    dummy = ListNode(-1)
    cur = dummy
    for val in input().split():
        node = ListNode(int(val))
        cur.next = node
        cur = node
    res = middle_of_linked_list(dummy.next)
    print(res.val)
