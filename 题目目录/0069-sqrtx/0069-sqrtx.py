class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1 if l * l > x else r + 1
        