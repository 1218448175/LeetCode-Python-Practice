# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, last = dummy, head
        for _ in range(n):
            last = last.next
        while last:
            pre = pre.next
            last = last.next
        pre.next = pre.next.next
        return dummy.next
        