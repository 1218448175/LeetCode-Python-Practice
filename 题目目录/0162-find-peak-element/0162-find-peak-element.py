from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(l: int, r: int) -> int:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                return binarySearch(mid, r)
            elif nums[mid] < nums[mid - 1]:
                return binarySearch(l, mid)
            else:
                return mid

        nums = [float('-inf')] + nums + [float('-inf')]
        return binarySearch(0, len(nums) - 1) - 1
