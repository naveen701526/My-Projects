# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        cur = head
        heap = []
        mapping_dict = {} # priority queue will do object comparision in case of duplicate values.
        
        for i in range(len(lists)):
            if not lists[i]:
                continue
            mapping_dict.setdefault(lists[i].val, 0)
            mapping_dict[lists[i].val] += 1
            heappush(heap, (lists[i].val, mapping_dict[lists[i].val], lists[i]))

        while heap:
            top = heappop(heap)
            if head is None:
                head = top[2]
                cur = head
            else:
                cur.next = top[2]
                cur = cur.next
            
            if cur.next is not None:
                mapping_dict.setdefault(cur.next.val, 0)
                mapping_dict[cur.next.val] += 1
                heappush(heap, (cur.next.val, mapping_dict[cur.next.val], cur.next))

            cur.next = None
            
        return head
