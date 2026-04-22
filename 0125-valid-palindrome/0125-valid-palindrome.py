class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(new_s)
        l, r = 0, n - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l, r = l + 1, r - 1
        return True