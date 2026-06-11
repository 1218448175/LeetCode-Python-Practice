class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b
        