# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root) -> [int]:
        output=[]
        self.inorder(root,output)
        return output
    def inorder(self,root,output):
        if root==None:
            return
        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right,output)
        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
opt = Solution()
print(opt.inorderTraversal(root))
