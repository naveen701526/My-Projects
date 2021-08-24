# Python3 program to check
# foldable binary tree

# Utility function to create a new
# tree node


class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

# Returns true if the given tree can be folded


def IsFoldable(root):
	if (root == None):
		return True
	return IsFoldableUtil(root.left, root.right)


# A utility function that checks
# if trees with roots as n1 and n2
# are mirror of each other
def IsFoldableUtil(n1, n2):
	# If both left and right subtrees are NULL,
	# then return true
	if n1 == None and n2 == None:
		return True

	# If one of the trees is NULL and other is not,
	# then return false
	if n1 == None or n2 == None:
		return False

	# Otherwise check if left and
	# right subtrees are mirrors of
	# their counterparts
	
	d1 = IsFoldableUtil(n1.left, n2.right)
	d2 = IsFoldableUtil(n1.right, n2.left)
	return d1 and d2


# Driver code
if __name__ == "__main__":

	

	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.right = newNode(4)
	root.right.left = newNode(5)

	if IsFoldable(root):
		print("Tree is foldable")
	else:
		print("Tree is not foldable")
