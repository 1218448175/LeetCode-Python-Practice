def check_sum(n):
    cnt = 0
    num = n
    while n > 0:
        cnt += (n % 10) ** 2
        n = n // 10
    return cnt

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = check_sum(slow)
            fast = check_sum(check_sum(fast))
            if slow == fast:
                break
        
        return True if slow == 1 else False
        