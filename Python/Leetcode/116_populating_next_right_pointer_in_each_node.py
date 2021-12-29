"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        c1, c2 = root.left, root.right
        
        while c1 and c2:
            c1.next = c2
            c1, c2 = c1.right, c2.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root
