from heapq import heapify, heappop, heappush

def findMedianSortedArrays(nums1, nums2):
    if not nums1:
        heap = nums2
    elif not nums2:
        heap = nums1
    elif nums1 and nums2:
        heap = merge_k_sorted_lists([nums1, nums2])
    else:
        return []
    median_index = 0
    count = 0
    len_heap = len(heap)
    if len_heap%2 == 0:
        median_index = (((len_heap)//2)-1, (len_heap)//2)
        while count <= median_index[0]:
            median = heappop(heap)
            count += 1
        return (median+heappop(heap))/2
    else:
        median_index = (len_heap)//2
        while count <= median_index:
            median = heappop(heap)
            count += 1
        return median

def merge_k_sorted_lists(lists):
    res = []
    heap = []
    for current_list in lists:
        # push lowest number of each list into the heap
        heappush(heap, (current_list[0], current_list, 0)) # 1

    while heap:
        val, current_list, head_index = heappop(heap)
        res.append(val)
        head_index += 1
        # if there are more numbers in the list, push into the heap
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))
    return res

print(findMedianSortedArrays([], [4]))
