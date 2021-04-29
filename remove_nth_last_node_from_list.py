# MY SOLUTION O(N) WITH O(N) SPACE
def removeNthFromEnd(head, n):
    cur = head
    lst = []
    while cur != None:
        lst.append(cur)
        cur = cur.next
    cur = head
    to_be_removed = lst[-n]
    prev = None
    while cur != None:
        if cur == to_be_removed:
            if prev == None:
                return head.next
            else:
                prev.next = cur.next
            return head
        else:
            prev = cur
            cur = cur.next
    return head

# BEST SOLUTION O(N) AND O(1) SPACE
def removeNthFromEnd(head, n):
    right = head
    count = 0
    while right != None:
        right = right.next
        count += 1
        if count == n:
            break
    left = None
    while right != None:
        right = right.next
        if left == None:
            left = head
        else:
            left = left.next
    if left != None:
        left.next = left.next.next
    else:
        return head.next
    return head
