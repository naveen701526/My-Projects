# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
		#Iterate over list
        while(temp):
			#store next value of current node
            n=temp.next
			
            # To avoid circular loop
            if(temp==head):
                prev=temp
                temp=n
                continue
			
			#Find correct position for current node
            temprep=head
            while(temprep and temprep.val<temp.val):
                prevrep=temprep
                temprep=temprep.next
                
			#Find previous of current node(node to be replaced)
            while(prev.next!=temp):
                prev=prev.next
                
			#Two cases:
			#1 - If current node to be replaced is start of list
            if(temprep==head):
                prev.next=temp.next
                temp.next=temprep
                head=temp
                
			#2 - If node is to be replaced in between
            else:
                prevrep.next=temp
                temp.next=temprep
                if(temprep.next==temp):
                    temprep.next=n
                else:
                    prev.next=n
			
			#Iterate over list
            temp=n

        return head
