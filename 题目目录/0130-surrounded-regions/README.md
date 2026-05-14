## [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

### 中等

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` 组成，**捕获** 所有 **被围绕的区域**：

- **连接：**一个单元格与水平或垂直方向上相邻的单元格连接。
- **区域：连接所有** `'O'` 的单元格来形成一个区域。
- **围绕：**如果一个区域中的所有 `'O'` 单元格都不在棋盘的边缘，则该区域被包围。这样的区域 **完全** 被 `'X'` 单元格包围。

通过 **原地** 将输入矩阵中的所有 `'O'` 替换为 `'X'` 来 **捕获被围绕的区域**。你不需要返回任何值。

**示例 1：**

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]</span></p>

<p><b>输出：</b><span class="example-io">[['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]</span></p>

<p><strong>解释：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1718167191-XNjUTG-image.png" style="width: 367px; height: 158px;">
<p>在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。</p>
</div>

---

## 题解：从边界切入的逆向 DFS 沉岛算法

### 1. 核心思路：逆向思维，寻找“逃逸”的 'O'

本题要求捕获所有被 'X' 包围的 'O'。直接判断一个内部的 'O' 是否被包围比较困难，但我们可以**反向思考**：

- **谁不会被捕获？**：任何与**边界**上的 'O' 直接或间接相连的 'O'，都不会被包围，因此不能被替换为 'X'。

- **策略**：
  
  1. 从棋盘的**四条边**开始扫描，发现 'O' 就启动 DFS。
  
  2. 将所有从边界“逃逸”出来的连通 'O' 全部暂时标记为一个特殊符号（如你的代码中的 `'I'`）。
  
  3. 遍历整个棋盘：
     
     - 剩下的 `'O'` 一定是深陷内部、被完全包围的，将其替换为 `'X'`。
     
     - 标记为 `'I'` 的是安全的，将其还原为 `'O'`。

---

### 2. 执行逻辑的详细拆解

#### A. 边界 DFS 扫描

Python

```
for r in range(nr):
    for c in range(nc):
        # 仅从四条边界上的 'O' 发起搜索
        if (r == 0 or c == 0 or r == nr - 1 or c == nc - 1) and board[r][c] == "O":
            self.dfs(board, r, c)
```

- 这步操作像是在给所有“有救”的节点打标签。只有能走到边缘的 'O' 才是安全的。

#### B. 递归标记逻辑

Python

```
def dfs(self, board, r, c):
    board[r][c] = "I" # 标记为特殊字符，表示“不可捕获”
    # ... 四向扩散 ...
    if ... and board[x][y] == "O":
        self.dfs(board, x, y)
```

- 通过 DFS，我们将边界 'O' 所在的整个连通分量都染成 `'I'`。

#### C. 二次遍历还原与捕获

Python

```
if board[r][c] == "O": 
    board[r][c] = "X" # 没被染色的 'O'，说明无法到达边界，捕获！
elif board[r][c] == "I": 
    board[r][c] = "O" # 染色的节点，还原回 'O'
```

- 这体现了清晰的三状态转换：`O`（原始） $\rightarrow$ `I`（标记） $\rightarrow$ `O`（还原）。

---

### 3. 算法可视化

输入示例：

Plaintext

```
X X X X      第一步：从边界扫描      X X X X      第二步：全局遍历      X X X X
X O O X    ----------------->    X O O X    ----------------->    X X X X
X X O X      标记边界连通节点       X X O X      捕获内部 O，还原 I    X X X X
X O X X                          X I X X                          X O X X
```

---

### 4. 复杂度分析

- **时间复杂度**：$O(M \times N)$。其中 $M$ 和 $N$ 是矩阵的行数和列数。每个格子最多被访问两次。

- **空间复杂度**：$O(M \times N)$。主要消耗在 DFS 的递归调用栈上。在最坏情况下（如整个棋盘都是 'O' 且从边界起始），栈深度可达 $M \times N$。

---

### 5. 代码回顾

```python
class Solution:
    def dfs(self, board, r, c):
        # 临时染色
        board[r][c] = "I"
        nr, nc = len(board), len(board[0])
        for x, y in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
            if 0 <= x < nr and 0 <= y < nc and board[x][y] == "O":
                self.dfs(board, x, y)

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        nr, nc = len(board), len(board[0])

        # 1. 寻找所有边界入口并染色
        for r in range(nr):
            for c in range(nc):
                # 只有边缘的 'O' 才能作为 DFS 起点
                is_edge = (r == 0 or c == 0 or r == nr - 1 or c == nc - 1)
                if is_edge and board[r][c] == "O":
                    self.dfs(board, r, c)

        # 2. 遍历全盘，根据颜色决定命运
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "O":
                    board[r][c] = "X" # 彻底被围，捕获
                elif board[r][c] == "I":
                    board[r][c] = "O" # 边界幸存者，还原
```