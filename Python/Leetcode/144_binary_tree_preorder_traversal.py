# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

		# This is an approach using stack

		stack = [root] # Taking the root not in the stack so that the loop will be initialized
		output = [] # Making a list for storing the output

		if root is None:
			return [] # If the root is None then directly return empty list

		while stack: # Will run till the stack is empty
			root = stack.pop() # First we will get the root element from the stack by popping the last element from the stack
