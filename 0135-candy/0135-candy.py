class Solution:
    def candy(self, ratings: List[int]) -> int:
        pre = 1
        down_ls_len = 0
        inc_ls_len = 1
        total = 1
        n = len(ratings)
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                down_ls_len = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                total += pre
                inc_ls_len = pre
            else:
                down_ls_len += 1
                if down_ls_len == inc_ls_len:
                    down_ls_len += 1

                total += down_ls_len
                pre = 1

        return total


        