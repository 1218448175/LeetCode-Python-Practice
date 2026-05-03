class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # 只要快指针不走到尽头，就一直跑
        while fast and fast.next:
            slow = slow.next          # 走1步
            fast = fast.next.next     # 走2步
            
            if slow == fast:          # 在环内相遇
                return True
        return False