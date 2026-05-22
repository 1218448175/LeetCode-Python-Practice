class Solution:
    def totalNQueens(self, n: int) -> int:
        # 低n位二进制全为1，用于表示当前行位置已满
        done = (1 << n) - 1

        # cols: 列，ld: 往左的斜线，rd: 往右的斜线
        def backtrack(cols, ld, rd) -> int:
            if cols == done:    # 位置填满，结果加一
                return 1
            count = 0

            # 获取当前可选位置，取反会带来无限位1，使用done截断
            pos = done & (~(cols | ld | rd))

            while pos:
                # 取最低为的1
                p = pos & -pos
                # 减去该位
                pos -= p
                # 递归
                count += backtrack(cols | p, (ld | p) << 1, (rd | p) >> 1)
            return count
            
        return backtrack(0, 0, 0)
