class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -inf
        window_cnt = 0
        n = len(nums)
        for i in range(n):
            left = i - k + 1
            window_cnt += nums[i]
            if left < 0:
                continue
            ans = max(ans, window_cnt / k)
            window_cnt -= nums[left]
        return ans
        