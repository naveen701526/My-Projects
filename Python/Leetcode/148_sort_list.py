# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getTail(self, head):
        while head.next:
            head = head.next
        return head

    def getMid(self, head, tail):
        s = head
        f = head
        while f != tail and f.next != tail:
            f = f.next.next
            s = s.next
        return s
    
    def mergeTwoSortedList(self, fsh, ssh):
        if fsh is None:
            return ssh
        if ssh is None:
            return fsh

        head = ListNode(None)
        cur = head

        while fsh and ssh:
            if fsh.val < ssh.val:
                cur.next = fsh
                fsh = fsh.next
                cur = cur.next
            else:
                cur.next = ssh
                ssh = ssh.next
                cur = cur.next

        if not fsh:
            cur.next = ssh
        else:
            cur.next = fsh
        return head.next

    def mergeSort(self, head, tail):
        if head == tail:
            return ListNode(head.val)
        mid = self.getMid(head, tail)
        fsh = self.mergeSort(head, mid)
        ssh = self.mergeSort(mid.next, tail)
        return self.mergeTwoSortedList(fsh, ssh)
        
    
    def sortList(self, head):
        if not head: return head
        temp_head = head
        # get tail of linked list
        tail = self.getTail(temp_head)
        # use merge sort to sort a linked list.
        return self.mergeSort(head, tail)
        