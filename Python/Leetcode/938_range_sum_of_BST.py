# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def helper(n: TreeNode = root):
            if not n:
                return
            if n.val > high:
                yield from helper(n.left)
            elif n.val < low:
                yield from helper(n.right)
            else:
                yield n.val
                yield from helper(n.left)
                yield from helper(n.right)
                
        return sum(helper())
