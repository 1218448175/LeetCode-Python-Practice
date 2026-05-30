class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_f = 0
        max_s = -inf
        min_f = 0
        min_s = 0

        for num in nums:
            max_f = max(max_f, 0) + num
            max_s = max(max_s, max_f)
            min_f = min(min_f, 0) + num
            min_s = min(min_s, min_f)

        if max_s < 0:
            return max_s
        return max(max_s, sum(nums) - min_s)
        