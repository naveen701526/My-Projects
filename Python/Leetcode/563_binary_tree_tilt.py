# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def _dfs(self, root):
        if not root:
            return 0
        
        left = self._dfs(root.left)
        right = self._dfs(root.right)
        self.ans += abs(left - right)
        return left + right + root.val
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)
        return self.ans
