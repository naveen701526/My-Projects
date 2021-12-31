# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans=0
        def DFS(node,big,small):
            if not node:
                return
            self.ans=max(self.ans,abs(node.val-big),abs(node.val-small))
            DFS(node.left,max(node.val,big),min(node.val,small))
            DFS(node.right,max(node.val,big),min(node.val,small))
        DFS(root,root.val,root.val)
        return self.ans
