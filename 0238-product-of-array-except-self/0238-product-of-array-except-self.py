class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1 for _ in range(n)]
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        R = 1
        for j in range(n - 1, -1, -1):
            answer[j] = answer[j] * R
            R = R * nums[j]
        return answer
        