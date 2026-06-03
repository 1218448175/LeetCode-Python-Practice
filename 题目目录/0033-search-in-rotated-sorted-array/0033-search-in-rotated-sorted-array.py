class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l: int, r: int) -> int:
            if l > r: 
                return -1

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[l]:
                if target < nums[mid] or target > nums[r]:
                    return binarySearch(l, mid - 1)
                else:
                    return binarySearch(mid + 1, r)
            elif nums[mid] > nums[r]:
                if target > nums[mid] or target < nums[l]:
                    return binarySearch(mid + 1, r)
                else:
                    return binarySearch(l, mid -1)
            else:
                if target > nums[mid]:
                    return binarySearch(mid + 1, r)
                else:
                    return binarySearch(l, mid - 1)

            return -1
        
        return binarySearch(0, len(nums) - 1)
        