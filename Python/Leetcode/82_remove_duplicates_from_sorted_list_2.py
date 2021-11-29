# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        start = ListNode(9999, head)
        end = start
        fast = head
        slow = start
        if not head or head.next == None:
            return head
        while fast:
            if fast.next:
                if fast.val != slow.val and fast.val != fast.next.val:
                    start.next = fast
                    start = start.next
            else:
                if fast.val != slow.val:
                    start.next = fast
                    start = start.next
            slow = fast
            fast = fast.next
        if end != start:
            start.next = fast
            return end.next
        return fast
