# Python program to detect and remove loop in linked list

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some poin
			# then there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)

				# Return 1 to indicate that loop if found
				return 1

		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop node-> Pointer to one of the loop nodes
	# head --> Pointer to the start node of the
	# linked list
	def removeLoop(self, loop_node):

		# Set a pointer to the beginning of the linked
		# list and move it one by one to find the first
		# node which is part of the linked list
		ptr1 = self.head
		while(1):
			# Now start a pointer from loop_node and check
			# if it ever reaches ptr2
			ptr2 = loop_node
			while(ptr2.next != loop_node and ptr2.next != ptr1):
				ptr2 = ptr2.next

			# If ptr2 reached ptr1 then there is a loop.
			# So break the loop
			if ptr2.next == ptr1:
				break

			ptr1 = ptr1.next

		# After the end of loop ptr2 is the lsat node of
		# the loop. So make next of ptr2 as NULL
		ptr2.next = None
	# Function to insert a new node at the beginning

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to prit the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next


# Driver code
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print("Linked List after removing loop")
llist.printList()
