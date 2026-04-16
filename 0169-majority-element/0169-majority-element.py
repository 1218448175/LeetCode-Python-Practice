class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = -1, 0
        n = len(nums)
        for i in range(n):
            if count == 0:
                num = nums[i]
                count = 1
            else:
                if num == nums[i]:
                    count += 1
                else:
                    count -= 1
        return num