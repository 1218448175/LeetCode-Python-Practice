class Solution:
    def binarySearch(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if l == r:
            return nums[l]
        mid = (l + r) // 2
        if nums[mid] >= nums[l]:
            return min(nums[l], self.binarySearch(nums[mid + 1:]))
        elif nums[mid] < nums[r]:
            return self.binarySearch(nums[l: mid + 1])

    def findMin(self, nums: List[int]) -> int:
        return self.binarySearch(nums)
        