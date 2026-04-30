class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        n = len(intervals)
        ans = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1,n):
            new_l, new_r = intervals[i][0], intervals[i][1]
            if new_l > r:
                ans.append([l, r])
                l = new_l
            r = max(r, new_r)
        ans.append([l, r])
        return ans
        