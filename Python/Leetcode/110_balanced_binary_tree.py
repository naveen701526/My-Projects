# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traversal(node):
            if not node:
                return 0, True
            left_height, left_balance = traversal(node.left)
            right_height, right_balance = traversal(node.right)
            return max(left_height, right_height) + 1, abs(left_height - right_height) <= 1 and left_balance and right_balance
        return traversal(root)[1]
