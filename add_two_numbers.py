"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(l):
    cur = l
    while cur != None:
        print(cur.val, end='')
        cur = cur.next
    print('')

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1 = list_to_array(l1)[::-1]
    l2 = list_to_array(l2)[::-1]
    suma = int(''.join(l1)) + int(''.join(l2))
    return string_to_reversed_list(str(suma))

def string_to_reversed_list(string):
    cur = ListNode(int(string[-1]))
    head = cur
    for num in string[:-1][::-1]:
        cur.next = ListNode(int(num))
        cur = cur.next
    return head


def list_to_array(l):
    cur = l
    res = []
    while cur != None:
        res.append(str(cur.val))
        cur = cur.next
    return res

def string_to_list(string):
    cur = ListNode(int(string[0]))
    head = cur
    for num in string[1:]:
        cur.next = ListNode(int(num))
        cur = cur.next
    return head

print_list(addTwoNumbers(string_to_list('243'), string_to_list('564')))
print_list(addTwoNumbers(string_to_list('500'), string_to_list('500')))
