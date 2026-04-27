class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = set()
        n = len(s)
        max_l = 0
        left = 0
        for right in range(n):
            if s[right] not in dic:
                dic.add(s[right])
                max_l = max(max_l, right - left + 1)
            else:
                while s[left] != s[right]:
                    dic.remove(s[left])
                    left += 1
                left += 1
        return max_l
        