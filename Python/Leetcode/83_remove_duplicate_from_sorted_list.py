# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        ptr, prev = head, ListNode(-101, head)
        while ptr:
            if ptr.val == prev.val:
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return head
