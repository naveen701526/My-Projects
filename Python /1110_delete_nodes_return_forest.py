# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def delNodes(self, root, to_delete):
        if root.val not in to_delete:
            self.output.append(root)
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            if node.val in to_delete:
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:
                    self.delNodes(node.right, to_delete)
            
            else:
                if node.left:
                    queue.append(node.left)
                    if node.left.val in to_delete:
                        node.left = None
                if node.right:
                    queue.append(node.right)
                    if node.right.val in to_delete:
                        node.right = None
        return self.output

    def print_output(self):
        for i in range(len(self.output)):
            print(self.output[i].val)
            if self.output[i].left:
                print(self.output[i].left.val)
            
            if self.output[i].right:
                print(self.output[i].right.val)
            
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

delete_nodes = Solution()

result = delete_nodes.delNodes(root, [3,5])
delete_nodes.print_output()
