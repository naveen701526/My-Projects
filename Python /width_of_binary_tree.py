# Python program to find the maximum width of
# binary tree using Level Order Traversal.

# A binary tree node


class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to get the maximum width of a binary tree


def getMaxWidth(root):
	maxWidth = 0
	h = height(root)
	# Get width of each level and compare the
	# width with maximum width so far
	for i in range(1, h+1):
		width = getWidth(root, i)
		if (width > maxWidth):
			maxWidth = width
	return maxWidth

# Get width of a given level


def getWidth(root, level):
	if root is None:
		return 0
	if level == 1:
		return 1
	elif level > 1:
		return (getWidth(root.left, level-1) +
				getWidth(root.right, level-1))

# UTILITY FUNCTIONS
# Compute the "height" of a tree -- the number of
# nodes along the longest path from the root node
# down to the farthest leaf node.


def height(node):
	if node is None:
		return 0
	else:

		# compute the height of each subtree
		lHeight = height(node.left)
		rHeight = height(node.right)

		# use the larger one
		return (lHeight+1) if (lHeight > rHeight) else (rHeight+1)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

# Function call
print("Maximum width is %d" % (getMaxWidth(root)))

