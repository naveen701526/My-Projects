# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            return None
        
        left = min(p.val, q.val)
        right = max(p.val, q.val)
        
        def dfs(node, left, right):
            if node is None:
                return
            if node.val > left and node.val > right:
                return dfs(node.left, left, right)
            if node.val < left and node.val < right:
                return dfs(node.right, left, right)
            return node
        
        return dfs(root, left, right)
