# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        from collections import deque
        q = deque()
        cur = head
        while cur.next:
            tmp, cur.next = cur.next, None
            q += tmp,
            cur = tmp
        cur, cnt = head, 0
        while q:
            cur.next = q.popleft() if cnt & 1 else q.pop()
            cur = cur.next
            cnt += 1
