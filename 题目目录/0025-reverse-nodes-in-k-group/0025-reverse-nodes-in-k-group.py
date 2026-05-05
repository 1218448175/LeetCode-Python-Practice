# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next
        cur = head
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nxt
            pre = tail
            head = tail.next

        return dummy.next
        