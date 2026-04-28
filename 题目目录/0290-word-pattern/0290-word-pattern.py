class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        s_dict = {}
        word_set = set()
        ans = True
        if len(s_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            a = pattern[i]
            word = s_dict.get(a)
            if (word is not None and word == s_list[i]) or (word is None and s_list[i] not in word_set):
                if not word:
                    word_set.add(s_list[i])
                    s_dict[a] = s_list[i]
                    continue
            else:
                ans = False
        print(s_dict, word_set)
        return ans