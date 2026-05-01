class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pos = points[0][1]
        n = len(points)
        i = 0
        ans = 1
        while i < n:
            start = points[i][0]
            if start > pos:
                pos = points[i][1]
                ans += 1
            i += 1
        return ans
        