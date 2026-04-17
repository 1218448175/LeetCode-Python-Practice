class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        step = 0
        end = 0
        for i in range(n -1):
            if max_len >= i:
                max_len = max(max_len, i + nums[i])
                if i == end:
                    end = max_len
                    step += 1

        return step
        
        