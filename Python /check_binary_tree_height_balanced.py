"""
Python3 program to check if a tree is height-balanced
"""
# A binary tree Node



class Node:
	# Constructor to create a new Node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# function to find height of binary tree
def height(root):
	
	# base condition when binary tree is empty
	if root is None:
		return 0
	return max(height(root.left), height(root.right)) + 1

# function to check if tree is height-balanced or not
def isBalanced(root):
	
	# Base condition
	if root is None:
		return True

	# for left and right subtree height
	lh = height(root.left)
	rh = height(root.right)

	# allowed values for (lh - rh) are 1, -1, 0
	if (abs(lh - rh) <= 1) and isBalanced(
	root.left) is True and isBalanced( root.right) is True:
		return True

	# if we reach here means tree is not
	# height-balanced tree
	return False

# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
	print("Tree is balanced")
else:
	print("Tree is not balanced")
