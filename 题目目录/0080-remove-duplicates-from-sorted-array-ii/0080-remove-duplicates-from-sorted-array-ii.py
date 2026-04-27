class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 2, 2
        n = len(nums)
        if n <= 2:
            return n

        while right < n:
            if nums[right] != nums[left-2]:
                nums[left] = nums[right]
                left += 1
            right += 1
    
        return left


