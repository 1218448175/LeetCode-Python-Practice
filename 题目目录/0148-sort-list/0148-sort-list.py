class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 1. 寻找中间节点 (快慢指针)
        # slow 停在前半段末尾，fast 负责探路
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 切断链表
        mid = slow.next
        slow.next = None
        
        # 2. 递归排序
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 3. 合并
        return self.mergeList(left, right)
    
    def mergeList(self, l, r):
        dummy = ListNode()
        cur = dummy
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l if l else r
        return dummy.next