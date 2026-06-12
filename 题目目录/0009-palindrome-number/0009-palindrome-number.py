class Solution:
    def isPalindrome(self, x: int) -> bool:
        for a, b in zip(str(x), str(x)[::-1]):
            if a != b:
                return False
        return True
        