# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # main variables
        mode = [root.val]
        freq_max = 1
        last = inf
        freq = 0
        
        # main function
        def in_order(node):
            nonlocal mode, freq_max, last, freq
            
            # call left node
            if node.left:
                in_order(node.left)
            
            # main operations
            if last == node.val:
                freq += 1
            
            else:
                if freq > freq_max:
                    freq_max, mode = freq, [last]
            
                elif freq == freq_max:
                    mode.append(last)
                    
                freq = 1
                last = node.val
            
            # call right node
            if node.right:
                in_order(node.right)
        
        # calling main function
        in_order(root)
        
        # edge cases
        if freq > freq_max:
            return [last]
        elif freq == freq_max:
                mode.append(last)
    
        if freq_max == 1:
            return mode[1:]
        
        # default
        return mode
