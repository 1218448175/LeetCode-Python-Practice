class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_len = 0
        for i in range(0, n):
            if max_len < i:
                break
            else:
                max_len = max(max_len, i + nums[i])
        return max_len >= n-1
        