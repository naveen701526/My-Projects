""" program to Delete a Tree """

# Helper function that allocates a new
# node with the given data and None
# left and right poers.								
class newNode:

	# Construct to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

""" This function traverses tree in post order to
	to delete each and every node of the tree """
def deleteTree( node) :

	if (node == None):
		return

	""" first delete both subtrees """
	deleteTree(node.left)
	deleteTree(node.right)
	
	""" then delete the node """
	print(" Deleting node:", node.data)


# Driver Code
if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	deleteTree(root)
	root = None

	print("Tree deleted ")
