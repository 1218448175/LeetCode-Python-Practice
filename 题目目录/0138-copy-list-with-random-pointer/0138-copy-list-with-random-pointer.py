"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        q = head
        while q:
            copy_node = Node(q.val, q.next)
            q.next = copy_node
            q = copy_node.next
        q = head
        while q:
            q.next.random = q.random.next if q.random else None
            q = q.next.next
        dummy = Node(0)
        p = dummy
        q = head
        while q:
            p.next = q.next
            p = p.next
            q = q.next.next
        return dummy.next
        