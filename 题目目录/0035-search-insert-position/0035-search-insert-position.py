class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left: int, right: int):
            if left > right:
                return -1
            mid = (left + right) // 2
            loc = -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                loc = binarySearch(left, mid - 1)
                return loc if loc != -1 else left
            else:
                loc = binarySearch(mid + 1, right)
                return loc if loc != -1 else right + 1
        
        return binarySearch(0, len(nums) - 1)
        