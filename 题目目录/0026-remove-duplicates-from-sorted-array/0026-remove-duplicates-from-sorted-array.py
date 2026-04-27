class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 1
        n = len(nums)
        if n == 0:
            return 0
        else:
            while right < n:
                if nums[right] != nums[left - 1]:
                    nums[left] = nums[right]
                    left += 1
                right += 1
        return left

