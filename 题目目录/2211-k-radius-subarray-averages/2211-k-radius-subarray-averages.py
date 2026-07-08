class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        total = sum(nums[0:2 * k])
        for i in range(k, n - k):
            total += nums[i + k]
            ans[i] = total // (2 * k + 1)
            total -= nums[i - k]
        return ans
        