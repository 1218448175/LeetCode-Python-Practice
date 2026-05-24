## [79. 单词搜索](https://leetcode.cn/problems/word-search/)

### 中等

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word`，如果 `word` 存在于网格中，返回 `true`；否则，返回 `false` 。

单词必须按照字母顺序，通过 **相邻** 的单元格内的字母构成，其中「相邻」单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

**示例 1：**

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
```

**示例 3：**

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

---

## 题解：网格 DFS 回溯 + 原地标记

### 1. 核心思路：枚举起点，四向扩展匹配

- 目标：判断 `word` 能否在 `board` 上按相邻规则拼出（每格最多用一次）。
- 双重循环枚举每个 `(i, j)`：若 `board[i][j] == word[0]`，以该格为起点尝试匹配。
- `backtrack(r, c, index)` 表示当前已站在 `word[index]` 对应格子；在 **四邻域** 中寻找 `word[index + 1]` 继续递归。

---

### 2. 回溯与访问标记

- 进入格子前将 `board[r][c] = '#'` 表示已占用；递归返回后 **`board[r][c] = char`** 恢复，供其他起点或分支复用。
- 起点处同样先标记再调用 `backtrack(i, j, 0)`，返回后恢复首字符。
- 四向数组 `[(1,0), (-1,0), (0,1), (0,-1)]`；邻居需满足：在界内、非 `'#'`、且 **`board[x][y] == word[index + 1]`**。

---

### 3. 终止条件

- **`index == len(word) - 1`**：当前格已是单词最后一个字母（起点或上一步已匹配到末位），置 `ans = True` 并返回。
- 本题只需判断存在性，找到一条路径即可；亦可在外层循环中若 `ans` 已为真则提前结束（当前实现依赖 `nonlocal ans` 在深层返回）。

---

### 4. 与相关题目的关系

- 本题为 [212. 单词搜索 II](../0212-word-search-ii) 的单词版：212 在相同 DFS 框架上叠加 **Trie** 与剪枝，批量匹配词库。
- 回溯 + `'#'` 标记与 [130. 被围绕的区域](../0130-surrounded-regions)、[200. 岛屿数量](../0200-number-of-islands) 等网格 DFS 写法一脉相承。

---

### 5. 复杂度分析

设棋盘 $M \times N$，单词长度 $L$。

- **时间复杂度**：最坏 $O(M \cdot N \cdot 4^L)$（每个格作起点，每步最多四岔）；实际因字符不匹配与 `'#'` 剪枝会小很多。
- **空间复杂度**：$O(L)$ 递归栈；原地改 `'#'` 不计额外矩阵。

---

### 6. 代码回顾

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        m = len(board)
        n = len(board[0])
        def backtrack(r: int, c: int, index: int) -> None:
            nonlocal ans
            if index == len(word) - 1:
                ans = True
                return
            for x_d, y_d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = r + x_d, c + y_d
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    char = board[x][y]
                    if char == word[index + 1]:
                        board[x][y] = '#'
                        backtrack(x, y, index + 1)
                        board[x][y] = char
            return
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    char = board[i][j]
                    board[i][j] = '#'
                    backtrack(i, j, 0)
                    board[i][j] = char
        return ans
```

亦可使用 `visited` 布尔矩阵代替 `'#'` 原地修改；找到答案后可在各层 `if ans: return` 提前剪枝。
