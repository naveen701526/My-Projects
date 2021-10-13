# Python3 code to implement Priority Queue
# using Singly Linked List

# Class to create new node which includes
# Node Data, and Node Priority
class PriorityQueueNode:
	
def __init__(self, value, pr):
	
	self.data = value
	self.priority = pr
	self.next = None
		
# Implementation of Priority Queue
class PriorityQueue:
	
	def __init__(self):
		
		self.front = None
		
	# Method to check Priority Queue is Empty
	# or not if Empty then it will return True
	# Otherwise False
	def isEmpty(self):
		
		return True if self.front == None else False
	
	# Method to add items in Priority Queue
	# According to their priority value
	def push(self, value, priority):
		
		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:
			
			# Creating a new node and assinging
			# it to class variable
			self.front = PriorityQueueNode(value,
										priority)
			
			# Returning 1 for successful execution
			return 1
			
		else:
			
			# Special condition check to see that
			# first node priority value
			if self.front.priority > priority:
				
				# Creating a new node
				newNode = PriorityQueueNode(value,
											priority)
				
				# Updating the new node next value
				newNode.next = self.front
				
				# Assigning it to self.front
				self.front = newNode
				
				# Returning 1 for successful execution
				return 1
				
			else:
				
				# Traversing through Queue until it
				# finds the next smaller priority node
				temp = self.front
				
				while temp.next:
					
					# If same priority node found then current
					# node will come after previous node
					if priority <= temp.next.priority:
						break
					
					temp = temp.next
				
				newNode = PriorityQueueNode(value,
											priority)
				newNode.next = temp.next
				temp.next = newNode
				
				# Returning 1 for successful execution
				return 1
	
	# Method to remove high priority item
	# from the Priority Queue
	def pop(self):
		
		# Condition check for checking
		# Priority Queue is empty or not
		if self.isEmpty() == True:
			return
		
		else:
			
			# Removing high priority node from
			# Priority Queue, and updating front
			# with next node
			self.front = self.front.next
			return 1
			
	# Method to return high priority node
	# value Not removing it
	def peek(self):
		
		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:
			return
		else:
			return self.front.data
			
	# Method to Traverse through Priority
	# Queue
	def traverse(self):
		
		# Condition check for checking Priority
		# Queue is empty or not
		if self.isEmpty() == True:
			return "Queue is Empty!"
		else:
			temp = self.front
			while temp:
				print(temp.data, end = " ")
				temp = temp.next

# Driver code
if __name__ == "__main__":
	
	# Creating an instance of Priority
	# Queue, and adding values
	# 7 -> 4 -> 5 -> 6
	pq = PriorityQueue()
	pq.push(4, 1)
	pq.push(5, 2)
	pq.push(6, 3)
	pq.push(7, 0)
	
	# Traversing through Priority Queue
	pq.traverse()
	
	# Removing highest Priority item
	# for priority queue
	pq.pop()
