class Solution:
    def reverse(self, x: int) -> int:
        note = 1 if x > 0 else -1
        x = abs(x)
        ans = 0
        while x > 0:
            ans += x % 10
            ans *= 10
            x //= 10
        ans //= 10
        if ans <= pow(2, 31):
            return note * ans
        else:
            return 0
        