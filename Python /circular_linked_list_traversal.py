# Function to print nodes in a given Circular linked list
def printList(self):

	temp = self.head
	
	# If linked list is not empty
	if self.head is not None:
		while(True):
			
		# Print nodes till we reach first node again
		print(temp.data, end = " ")
				temp = temp.next
				if (temp == self.head):
					break
	
