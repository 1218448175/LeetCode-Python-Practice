class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        v_i_dict = {}
        n = len(nums)
        ans = False
        for i in range(n):
            if v_i_dict.get(nums[i]) is None or (i - v_i_dict.get(nums[i]) > k):
                v_i_dict[nums[i]] = i
            else:
                ans = True
                break
        return ans
        