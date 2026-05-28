# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2List(l: Optional[List], r: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            cur = dummy
            while r and l:
                if r.val <= l.val:
                    cur.next = r
                    r = r.next
                else:
                    cur.next = l
                    l = l.next
                cur = cur.next
            if r:
                cur.next = r
            if l:
                cur.next = l
            return dummy.next
        
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        nxt_lists = []
        for i in range(0, n, 2):
            if i + 1 == n:
                break
            l, r = lists[i], lists[i + 1]
            nxt_lists.append(merge2List(l, r))
        if n % 2 != 0:
            nxt_lists.append(lists[-1])
        return self.mergeKLists(nxt_lists)
        