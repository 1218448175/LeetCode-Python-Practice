class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tail = nums[0]
        middle = nums[0]
        for num in nums[1:]:
            middle = max(tail, middle)
            tail = max(num, tail + num)
        return max(middle, tail)
        