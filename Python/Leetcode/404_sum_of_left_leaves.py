# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root, ans=0, flag=False) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None and flag:
            return root.val

        return ans + self.sumOfLeftLeaves(root.left, ans, True) + self.sumOfLeftLeaves(root.right, ans, False)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
obj = Solution()
print(obj.sumOfLeftLeaves(root))
