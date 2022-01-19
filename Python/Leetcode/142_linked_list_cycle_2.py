# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return
        
        slow = head.next
        fast = slow.next
        
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        
        if fast is None or fast.next is None:
            return

        while fast != head:
            head = head.next
            fast = fast.next
        return fast
