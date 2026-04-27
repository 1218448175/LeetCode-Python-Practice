class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        k_v_dict = {}
        v_set = set()
        n = len(s)
        ans = True
        for i in range(n):
            s_char, t_char = s[i], t[i]
            get_char = k_v_dict.get(s_char)
            if get_char and get_char != t_char:
                ans = False
                break
            if not get_char:
                if t_char not in v_set:
                    k_v_dict[s_char] = t_char
                    v_set.add(t_char)
                else:
                    ans = False
                    break

        return ans
        