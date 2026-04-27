from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # 统计目标字符串 t 中各字符需要的数量
        target_cnt = Counter(t)
        target_kinds = len(target_cnt)
        
        # 窗口内当前各字符的数量
        window_cnt = Counter()
        kinds = 0 # 当前窗口内已经“完全达标”的字符种类数
        
        min_len = float('inf')
        ans_left = 0
        l = 0
        
        for r in range(len(s)):
            in_char = s[r]
            # 1. 扩张窗口
            if in_char in target_cnt:
                window_cnt[in_char] += 1
                # 只有当数量正好相等时，才算增加了一个达标种类
                if window_cnt[in_char] == target_cnt[in_char]:
                    kinds += 1
            
            # 2. 当所有种类都达标时，进入收缩阶段
            while kinds == target_kinds:
                # 更新最短长度
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_left = l
                
                out_char = s[l]
                # 3. 尝试收缩左边界
                if out_char in target_cnt:
                    # 关键逻辑：如果当前数量正好等于目标数量，
                    # 那么移出这个字符后，该种类就不再达标了
                    if window_cnt[out_char] == target_cnt[out_char]:
                        kinds -= 1
                    window_cnt[out_char] -= 1
                l += 1
                
        return s[ans_left : ans_left + min_len] if min_len != float('inf') else ""