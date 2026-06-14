class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i, (x, y) in enumerate(points):
            cnt = defaultdict(int)
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x, y2 - y
                k = dy / dx if dx else inf
                cnt[k] += 1
                ans = max(ans, cnt[k])
        return ans + 1
        