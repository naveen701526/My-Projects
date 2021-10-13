# Python3 program to count number of nodes in
# a circular linked list.

# structure for a node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to insert a node at the beginning
# of a Circular linked list */
def push(head_ref,data):

	ptr1 = Node(0)
	temp = head_ref
	ptr1.data = data
	ptr1.next = head_ref

	# If the linked list is not None then set
	# the next of last node
	if (head_ref != None) :
		while (temp.next != head_ref):
			temp = temp.next
		temp.next = ptr1
	else:
		ptr1.next = ptr1 #For the first node */

	head_ref = ptr1
	return head_ref

# Function to print nodes
# in a given Circular linked list
def countNodes(head):

	temp = head
	result = 0
	if (head != None) :
		while True :
			temp = temp.next
			result = result + 1
			if (temp == head):
				break
	
	return result

# Driver Code
if __name__=='__main__':

	# Initialize lists as empty */
	head = None
	head = push(head, 12)
	head = push(head, 56)
	head = push(head, 2)
	head = push(head, 11)

	print( countNodes(head))
	
