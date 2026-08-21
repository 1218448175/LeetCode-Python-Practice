class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for n in nums:
            ans += cnt[n]
            cnt[n] += 1
        return ans
        