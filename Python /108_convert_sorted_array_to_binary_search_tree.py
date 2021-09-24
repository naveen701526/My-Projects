# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        idx = len(nums) // 2
        
        return TreeNode(nums[idx],
                        self.sortedArrayToBST(nums[:idx]),
                        self.sortedArrayToBST(nums[idx + 1:]))
