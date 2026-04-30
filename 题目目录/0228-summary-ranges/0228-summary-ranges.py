class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            low = i
            high = i
            while high < n - 1 and nums[high + 1] == nums[high] + 1:
                high += 1
            if high == low:
                ans.append(f"{nums[low]}")
            else:
                ans.append(f"{nums[low]}->{nums[high]}")
            i = high + 1
        return ans