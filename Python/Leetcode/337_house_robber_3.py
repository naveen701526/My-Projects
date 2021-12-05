# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            leftOneLayer, leftTwoLayer, rightOneLayer, rightTwoLayer = [0] * 4
            if node.left:
                leftOneLayer, leftTwoLayer = dfs(node.left)
            if node.right:
                rightOneLayer, rightTwoLayer = dfs(node.right)
            if not node.left and not node.right:
                return node.val, 0
            
            return node.val + leftTwoLayer + rightTwoLayer, max(leftOneLayer, leftTwoLayer) + max(rightOneLayer, rightTwoLayer)
        return max(dfs(root))
