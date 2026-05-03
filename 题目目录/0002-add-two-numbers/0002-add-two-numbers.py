class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:  # 将 carry 也放入循环条件，可以省去最后的 if carry
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # 计算总和及进位
            total = v1 + v2 + carry
            carry = total // 10
            
            # 创建新节点
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # 推进原链表
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next