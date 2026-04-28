class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        return not ((s_cnt - t_cnt) or (t_cnt - s_cnt))
        