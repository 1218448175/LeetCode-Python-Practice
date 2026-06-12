class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            c = digits[i] // 10
            digits[i] %= 10
            if not c:
                break
        if not digits[0]:
            digits = [1] + digits
        return digits
        