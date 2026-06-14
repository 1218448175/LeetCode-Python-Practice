class Solution:
    def myPow(self, x: float, n: int) -> float:
        d = 1
        if n < 0:
            n *= -1
            d = -1
        ans = 1
        x_contribute = x
        while n > 0:
            if n % 2 == 1:
                ans *= x_contribute
            x_contribute *= x_contribute
            n //= 2
        return ans if d == 1 else 1 / ans
        