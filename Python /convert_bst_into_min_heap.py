# Python3 prgroam to contrcut all unique
# BSTs for keys from 1 to n

# Binary Tree Node
""" A utility function to create a
new BST node """
class newNode:

	# Construct to create a newNode
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Utility function to print Min-heap
# level by level
def printLevelOrder(root):
	
	# Base Case
	if (root == None):
		return

	# Create an empty queue for level
	# order traversal
	q = []
	q.append(root)

	while (len(q)):
		nodeCount = len(q)
		while (nodeCount > 0) :
		
			node = q[0]
			print(node.data, end = " " )
			q.pop(0)
			if (node.left) :
				q.append(node.left)
			if (node.right) :
				q.append(node.right)
			nodeCount -= 1
		print()

# A simple recursive function to convert a
# given Binary Search tree to Sorted Linked
# List root	 -. Root of Binary Search Tree
def BSTToSortedLL(root, head_ref):

	# Base cases
	if(root == None) :
		return

	# Recursively convert right subtree
	BSTToSortedLL(root.right, head_ref)

	# insert root into linked list
	root.right = head_ref[0]

	# Change left pointer of previous
	# head to point to None
	if (head_ref[0] != None):
		(head_ref[0]).left = None

	# Change head of linked list
	head_ref[0] = root

	# Recursively convert left subtree
	BSTToSortedLL(root.left, head_ref)

# Function to convert a sorted Linked
# List to Min-Heap.
# root -. root[0] of Min-Heap
# head -. Pointer to head node of
#		 sorted linked list
def SortedLLToMinHeap( root, head) :

	# Base Case
	if (head == None) :
		return

	# queue to store the parent nodes
	q = []

	# The first node is always the
	# root node
	root[0] = head[0]

	# advance the pointer to the next node
	head[0] = head[0].right

	# set right child to None
	root[0].right = None

	# add first node to the queue
	q.append(root[0])

	# run until the end of linked list
	# is reached
	while (head[0] != None) :
	
		# Take the parent node from the q
		# and remove it from q
		parent = q[0]
		q.pop(0)

		# Take next two nodes from the linked
		# list and Add them as children of the
		# current parent node. Also in push them
		# into the queue so that they will be
		# parents to the future nodes
		leftChild = head[0]
		head[0] = head[0].right	 # advance linked list to next node
		leftChild.right = None # set its right child to None
		q.append(leftChild)

		# Assign the left child of parent
		parent.left = leftChild

		if (head) :
			rightChild = head[0]
			head[0] = head[0].right # advance linked list to next node
			rightChild.right = None # set its right child to None
			q.append(rightChild)

			# Assign the right child of parent
			parent.right = rightChild

# Function to convert BST into a Min-Heap
# without using any extra space
def BSTToMinHeap(root):

	# head of Linked List
	head = [None]

	# Convert a given BST to Sorted Linked List
	BSTToSortedLL(root, head)
	
	# set root as None
	root = [None]

	# Convert Sorted Linked List to Min-Heap
	SortedLLToMinHeap(root, head)
	return root

# Driver Code
if __name__ == '__main__':
	root = newNode(8)
	root.left = newNode(4)
	root.right = newNode(12)
	root.right.left = newNode(10)
	root.right.right = newNode(14)
	root.left.left = newNode(2)
	root.left.right = newNode(6)

	root = BSTToMinHeap(root)
	printLevelOrder(*root)
