# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        large = ListNode()
        small_q = small
        large_q = large
        cur = head
        while head:
            if head.val < x:
                small_q.next = head
                small_q = small_q.next
                head = head.next
                small_q.next = None
            else:
                large_q.next = head
                large_q = large_q.next
                head = head.next
                large_q.next = None
        small_q.next = large.next
        return small.next
        