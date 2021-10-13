# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal_right(self, root: Optional[TreeNode], array):
	    if root:
		    self.traversal_right(root.right, array)
		    array.append(root.val)
		    self.traversal_right(root.left, array)
	    array.append(None)

    def traversal_left(self, root: Optional[TreeNode], array):
	    if root:
		    self.traversal_left(root.left, array)
		    array.append(root.val)
		    self.traversal_left(root.right, array)
	    array.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
	    left = []
	    right = []

	    self.traversal_left(root.left, left)
	    self.traversal_right(root.right, right)

	    return True if left == right else False
        
