# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=101, next=head)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur.next = cur.next.next
                if cur:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next
        