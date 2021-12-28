# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        twice_head = head
        while twice_head and twice_head.next:
            head, twice_head = head.next, twice_head.next.next
        return head
