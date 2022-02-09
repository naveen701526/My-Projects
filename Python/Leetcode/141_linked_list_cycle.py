# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow=fast=head
        while (fast.next is not None) and (fast.next.next is not None):
                slow=slow.next
                fast=fast.next.next
                if slow==fast: return True
        return False
