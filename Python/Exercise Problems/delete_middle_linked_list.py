# Python3 program to delete middle
# of a linked list

# Link list Node
class Node:
	
	def __init__(self):
		
		self.data = 0
		self.next = None
	
# Count of nodes
def countOfNodes(head):

	count = 0
	
	while (head != None):
		head = head.next
		count += 1
	
	return count

# Deletes middle node and returns
# head of the modified list
def deleteMid(head):

	# Base cases
	if (head == None):
		return None
	if (head.next == None):
		del head
		return None

	copyHead = head

	# Find the count of nodes
	count = countOfNodes(head)

	# Find the middle node
	mid = count // 2

	# Delete the middle node
	while (mid > 1):
		mid -= 1
		head = head.next

	# Delete the middle node
	head.next = head.next.next

	return copyHead

# A utility function to print
# a given linked list
def printList(ptr):

	while (ptr != None):
		print(ptr.data, end = '->')
		ptr = ptr.next
	
	print('NULL')
	
# Utility function to create a new node.
def newNode(data):

	temp = Node()
	temp.data = data
	temp.next = None
	return temp

# Driver Code
if __name__=='__main__':
	
	# Start with the empty list
	head = newNode(1)
	head.next = newNode(2)
	head.next.next = newNode(3)
	head.next.next.next = newNode(4)

	print("Gven Linked List")
	printList(head)

	head = deleteMid(head)

	print("Linked List after deletion of middle")
	printList(head)
