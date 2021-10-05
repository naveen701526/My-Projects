# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        
        
        
        node = head
        while node and node.val == val:
            node = node.next
        
        if not node:
            return None
        elif not node.next:
            return node
        
        
        # now we have at least 2 nodes, and 'node'.val != val 
        res = node
        
        while node and node.next:
            if node.next.val != val:
                node = node.next
            else: # node.next.val == val
                node.next = node.next.next
            
        return res 
        
opt = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

ans = opt.removeElements(head,6)
while ans:
    print(ans.val)
    ans = ans.next
