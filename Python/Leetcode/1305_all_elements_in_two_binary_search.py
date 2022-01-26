# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if root is None:
                return []
            
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        list1, list2 = dfs(root1), dfs(root2)
        n1, n2 = len(list1), len(list2)
        i = j = 0
        res = []
        
        while i < n1 and j < n2:
            if list1[i] <= list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        
        for k in range(i, n1):
            res.append(list1[k])
        
        for k in range(j, n2):
            res.append(list2[k])
        
        return res
