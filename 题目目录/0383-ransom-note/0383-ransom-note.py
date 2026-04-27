class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target_counter = Counter(ransomNote)
        cnt = Counter(magazine)
        ans = True
        for k in target_counter:
            if target_counter[k] > cnt[k]:
                ans = False
                break

        return ans
        