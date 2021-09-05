# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        string = ''
        temp_head = head
        while temp_head:
            string += str(temp_head.val)
            temp_head = temp_head.next
        left = 0
        right = len(string) - 1
        while left<right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
     
opt = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(opt.isPalindrome(head))
