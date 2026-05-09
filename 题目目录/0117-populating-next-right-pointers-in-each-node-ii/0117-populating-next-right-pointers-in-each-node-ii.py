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
    def handle(self, p):
        if self.last:
            self.last.next = p
        if not self.next_start:
            self.next_start = p
        self.last = p

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        start = root
        while start:
            self.last = None
            self.next_start = None
            p = start
            while p:
                if p.left:
                    self.handle(p.left)
                if p.right:
                    self.handle(p.right)
                p = p.next
            start = self.next_start

        return root
        