"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

""" Time Complexity:  O(N), Space Complexity: O(1) """

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        
        # step:1- creating deep copies of node and inserting between self and next node.
        # eg. A -> B will become A -> A'(New Node) -> B
        cur_node = head
        while cur_node:
            nxt_node = cur_node.next
            new_node = ListNode(cur_node.val)
            cur_node.next = new_node
            new_node.next = nxt_node
            cur_node = nxt_node

        # step:2- setting up the random pointers for our deep copy.
        # eg. A -> K (Random Pointer) and now A' will also point to the same random pointer A' -> K
        cur_node = head
        while cur_node :
            if not cur_node.random:
                cur_node.next.random = None
            else:
                cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next

        # step:3 - separating original and our deep copied list
        original = head
        copy = head.next
        new_head = copy
        while original:
            original.next = original.next.next
            if not copy.next:
                copy.next = copy.next
            else:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        return new_head
