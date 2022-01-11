# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def calc(node, temp):
            if not node:
                return 0
            
            temp = temp*2 + node.val
            if (node.left is None) and (node.right is None):
                return temp
            
            return (calc(node.left, temp) + calc(node.right, temp))
        
        return calc(root, 0)
