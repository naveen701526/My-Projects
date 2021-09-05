# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if p is None:
            if q is None:
                return True
            else:
                return False
        if q is None:
            if p is None:
                return True
            else:
                return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
opt = Solution()
root = TreeNode(1)
root1 = TreeNode(1)
root.left = TreeNode(2)
root1.left = TreeNode(2)
root.right = TreeNode(3)
root1.right = TreeNode(3)
print(opt.isSameTree(root,root1))
        
