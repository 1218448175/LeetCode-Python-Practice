class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        cnt = dict()
        for n in nums:
            if cnt.get(n):
                ans = max(ans, abs(n))
                
            else:
                cnt[-n] = 1

        return ans
            
        