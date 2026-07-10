class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        cur = blocks[: k - 1].count('W')
        ans = n
        for i in range(k - 1, n):
            cur += 1 if blocks[i] == 'W' else 0
            ans = min(cur, ans)
            if ans == 0:
                return ans
            l = i - k + 1
            cur -= 1 if blocks[l] == 'W' else 0
        return ans
        