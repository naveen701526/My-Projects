# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            if l2 is not None:
                return l2
            return None
        if l2 is None:
            if l1 is not None:
                return l1
            return None
        
        temp1 = l1
        temp2 = l2
        output = []
        new_list = ListNode(min(l1.val, l2.val))
        temp_new_list = new_list
        while temp1:
            output.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            output.append(temp2.val)
            temp2 = temp2.next
        output.sort()
        for i in range(1,len(output)):
            temp_new_list.next = ListNode(output[i])
            temp_new_list = temp_new_list.next
            
        temp_new_list.next = None
        return new_list
            
            
            
                
opt = Solution()
l1 = [1,2,4]
l2 = [1,3,4]
ll1 = ListNode(l1[0])
temp_ll1 = ll1
ll2 = ListNode(l2[0])
temp_ll2 = ll2
for i in range(1,len(l1)):
    temp_ll1.next = ListNode(l1[i])
    temp_ll1 = temp_ll1.next
temp_ll1.next = None
for i in range(1,len(l2)):
    temp_ll2.next = ListNode(l2[i])
    temp_ll2 = temp_ll2.next
temp_ll2.next = None

ans = opt.mergeTwoLists(ll1,ll2)
temp_ans = ans
output = []
while temp_ans:
    output.append(temp_ans.val)
    temp_ans = temp_ans.next
print(output)
