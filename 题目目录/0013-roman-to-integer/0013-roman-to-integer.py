class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        ans = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(n - 1):
            num_i = dic[s[i]]
            if num_i >= dic[s[i + 1]]:
                ans += num_i
            else:
                ans -= num_i
        ans += dic[s[-1]]
        return ans
        