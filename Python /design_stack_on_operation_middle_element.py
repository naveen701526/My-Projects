''' Python3 Program to implement a stack
that supports findMiddle()
and deleteMiddle in O(1) time '''

''' A Doubly Linked List Node '''


class DLLNode:

	def __init__(self, d):
		self.prev = None
		self.data = d
		self.next = None


''' Representation of the stack
data structure that supports
findMiddle() in O(1) time. The
Stack is implemented using
Doubly Linked List. It maintains
pointer to head node, pointer
to middle node and count of
nodes '''


class myStack:

	def __init__(self):
		self.head = None
		self.mid = None
		self.count = 0


''' Function to create the stack data structure '''


def createMyStack():
	ms = myStack()
	ms.count = 0
	return ms


''' Function to push an element to the stack '''


def push(ms, new_data):
	''' allocate DLLNode and put in data '''
	new_DLLNode = DLLNode(new_data)

	''' Since we are adding at the beginning,
	prev is always NULL '''
	new_DLLNode.prev = None

	''' link the old list off the new DLLNode '''
	new_DLLNode.next = ms.head

	''' Increment count of items in stack '''
	ms.count += 1

	''' Change mid pointer in two cases
	1) Linked List is empty
	2) Number of nodes in linked list is odd '''
	if(ms.count == 1):
		ms.mid = new_DLLNode

	else:
		ms.head.prev = new_DLLNode

		# Update mid if ms->count is odd
		if((ms.count % 2) != 0):
			ms.mid = ms.mid.prev

	''' move head to point to the new DLLNode '''
	ms.head = new_DLLNode


''' Function to pop an element from stack '''


def pop(ms):
	''' Stack underflow '''
	if(ms.count == 0):

		print("Stack is empty")
		return -1

	head = ms.head
	item = head.data
	ms.head = head.next

	# If linked list doesn't become empty,
	# update prev of new head as NULL
	if(ms.head != None):
		ms.head.prev = None
	ms.count -= 1

	# update the mid pointer when
	# we have even number of elements
	# in the stack, i,e move down
	# the mid pointer.
	if(ms.count % 2 == 0):
		ms.mid = ms.mid.next
	return item

# Function for finding middle of the stack


def findMiddle(ms):
	if(ms.count == 0):
		print("Stack is empty now")
		return -1
	return ms.mid.data


# Driver code
if __name__ == '__main__':

	ms = createMyStack()
	push(ms, 11)
	push(ms, 22)
	push(ms, 33)
	push(ms, 44)
	push(ms, 55)
	push(ms, 66)
	push(ms, 77)

	print("Item popped is " +
		str(pop(ms)))
	print("Item popped is " +
		str(pop(ms)))
	print("Middle Element is " +
		str(findMiddle(ms)))
