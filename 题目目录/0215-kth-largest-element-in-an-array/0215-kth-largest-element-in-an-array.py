class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            small, equal, big = list(), list(), list()
            for num in nums:
                if num == pivot:
                    equal.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    big.append(num)
            if k <= len(big):
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                return quick_select(small, k + len(small) - len(nums))
            return pivot

        return quick_select(nums, k)
        