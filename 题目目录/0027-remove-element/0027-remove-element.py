class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        r = n - 1
        l = 0
        while r >= l:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l
