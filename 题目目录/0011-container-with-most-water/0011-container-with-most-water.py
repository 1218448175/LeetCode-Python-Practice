class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = r * min(height[l], height[r])
        while l < r:
            if height[l] <= height[r]:
                ans = max(ans, (r - l) * height[l])
                l += 1
            elif height[l] > height[r]:
                ans = max(ans, (r - l) * height[r])
                r -= 1
        return ans

