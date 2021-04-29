def oddEvenList(self, head: ListNode) -> ListNode:
    if head == None: return
    odds = ListNode(head.val)
    new_head = odds
    if head.next == None: return odds
    evens = ListNode(head.next.val)
    evens_head = evens
    cur = head.next.next
    count = 1
    while cur != None:
        if count == -1:
            evens.next = ListNode(cur.val)
            evens = evens.next
        else:
            odds.next = ListNode(cur.val)
            odds = odds.next
        count *= -1
        cur = cur.next
    odds.next = evens_head
    return new_head
