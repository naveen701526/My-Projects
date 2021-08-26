# Python3 program to Get Level of a
# node in a Binary Tree

# Helper function that allocates a
# new node with the given data and
# None left and right pairs.


class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Helper function for getLevel(). It
# returns level of the data if data is
# present in tree, otherwise returns 0


def getLevelUtil(node, data, level):
	if (node == None):
		return 0

	if (node.data == data):
		return level

	downlevel = getLevelUtil(node.left,
							data, level + 1)
	if (downlevel != 0):
		return downlevel

	downlevel = getLevelUtil(node.right,
							data, level + 1)
	return downlevel

# Returns level of given data value


def getLevel(node, data):

	return getLevelUtil(node, data, 1)


# Driver Code
if __name__ == '__main__':

	# Let us construct the Tree shown
	# in the above figure
	root = newNode(3)
	root.left = newNode(2)
	root.right = newNode(5)
	root.left.left = newNode(1)
	root.left.right = newNode(4)
	for x in range(1, 6):
		level = getLevel(root, x)
		if (level):
			print("Level of", x,
				"is", getLevel(root, x))
		else:
			print(x, "is not present in tree")
