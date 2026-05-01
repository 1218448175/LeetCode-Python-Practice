class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        l, r = newInterval

        while i < n and intervals[i][1] < l:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= r:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1
        res.append([l, r])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res