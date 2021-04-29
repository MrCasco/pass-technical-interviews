## NAIVE SOLUTION ##
def mergeKLists(lists):
    merged_list = ListNode(0)
    cur = merged_list
    # we are done until all lists are null
    while any(lists):
        # run a loop through the number of lists to check their current head
        cur_min = float('inf')
        list_to_chop = 0
        for i in range(len(lists)):
            if lists[i] != None:
                # see which is the minimum and add it to the new sorted list
                if cur_min > lists[i].val:
                    cur_min = lists[i].val
                    list_to_chop = i
        cur.next = lists[list_to_chop]
        cur = cur.next
        # make that list one node shorter
        if lists[list_to_chop] != None:
            lists[list_to_chop] = lists[list_to_chop].next
        else:
            lists.pop(list_to_chop)
    return merged_list.next

## BEST SOLUTION? ##
def mergeKLists(lists: List[ListNode]) -> ListNode:
    # create an array that will hold all lists in array mode
    merged_lists = []
    # read each list and append it to this array
    for lst in lists:
        merged_lists += list_to_array(lst)
    # sort the array
    merged_lists.sort()
    # create a merged linked list based on the array
    return array_to_list(merged_lists)

def list_to_array(lst):
    cur = lst
    res = []
    while cur != None:
        res.append(cur.val)
        cur = cur.next
    return res

def array_to_list(arr):
    head = ListNode(0)
    cur = head
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next
