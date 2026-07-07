class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        target = k * threshold
        ans = 0
        for i in range(n):
            left = i - k + 1
            target -= arr[i]
            if left < 0:
                continue
            if target <= 0:
                ans += 1
            target += arr[left]
        return ans
        