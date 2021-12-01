# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int, upper=None) -> List[Optional[TreeNode]]:
        return [
            TreeNode(val, l, r) \
                for val in range(n, upper+1) \
                for l in self.generateTrees(n, val - 1) \
                for r in self.generateTrees(val + 1, upper)
        ] or [None] if upper is not None else self.generateTrees(1, n)
