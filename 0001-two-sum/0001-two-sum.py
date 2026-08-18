class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        Hash_dict = {}
        for i in range(n):
            num = nums[i]
            gap = target - num
            if num in Hash_dict.keys():
                return (Hash_dict.get(num), i)
            Hash_dict[gap] = i
