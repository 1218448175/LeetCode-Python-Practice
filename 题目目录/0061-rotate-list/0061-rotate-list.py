# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        q = dummy
        list_len = 0
        while q.next:
            q = q.next
            list_len += 1
        q.next = head
        if list_len == 0:
            return head
        step = k % list_len
        for _ in range(list_len - step):
            head = head.next
            q = q.next
        q.next = None
        return head
        