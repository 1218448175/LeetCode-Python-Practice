## [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/)

### 困难

给定一个 `m x n` 二维字符网格 `board` 和一个单词列表 `words`，返回所有 **二维网格上** 同时出现的单词。

单词必须按照字母顺序，通过 **相邻** 的单元格内的字母构成，其中「相邻」单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

**示例 1：**

```
输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
```

**示例 2：**

```
输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]
```

---

## 题解：Trie 建词库 + 网格 DFS 回溯 + 剪枝

### 1. 核心思路：用字典树替代「对每个词单独搜棋盘」

- 若对 `words` 中每个词各做一次 [79. 单词搜索](https://leetcode.cn/problems/word-search/) 式 DFS，词多时重复遍历棋盘，易超时。
- 先把所有 `words` 插入 **Trie**；再从棋盘每个格子出发，沿 Trie 同时匹配 **多条候选词** 的前缀，共享路径。
- 节点上直接存完整单词 `word`（而不仅是 `end` 标志），命中时 `ans.append(cur_node.word)`，无需在 DFS 中拼接字符串。

---

### 2. 建 Trie 与网格 DFS

- `Trie.addWord`：与 208/211 相同沿字符建 `Node`，词尾 `cur.word = word`。
- 对每个 `(r, c)`，若 `board[r][c]` 在 `root.dict` 中，调用 `dfs(r, c, root)`。
- `dfs` 中：`cur_node = parent_node.dict[char]`；若 `cur_node.word` 非空，加入答案并 **`cur_node.word = None`**，避免同一 Trie 路径重复输出。

---

### 3. 回溯与访问标记

- 进入格子前将 `board[r][c] = '#'` 表示已用；四向扩展后 **`board[r][c] = char`** 恢复，供其他路径复用。
- 仅当 `board[x][y] in cur_node.dict` 时继续递归，自然实现「只沿 Trie 中存在的边」走。

---

### 4. 剪枝：搜干的分支从父节点删除

DFS 返回前若 **`not cur_node.dict`**（当前 Trie 节点下已无子节点、且其 `word` 也已置空），说明以该字符为前缀的所有词都已找完，执行：

`parent_node.dict.pop(char)`

从父节点删掉该边，后续从网格再走到这里时不会再进入死分支，显著减少重复搜索（212 经典优化）。

---

### 5. 复杂度分析

设棋盘大小 $M \times N$，词库总字符数 $W$，最长词长 $L$。

- **建 Trie**：$O(W)$。
- **搜索**：最坏仍可能较大，但 Trie 共享前缀 + 剪枝后，实践中远优于对每个词单独 DFS；空间为 Trie 节点数 $O(W)$ 加递归栈 $O(L)$。

---

### 6. 代码回顾

```python
class Node:
    def __init__(self):
        self.dict = {}
        # 直接存储单词，既能当 end 标志，又免去了字符串拼接
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.word = word  # 存入完整单词

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 构建 Trie 树
        trie = Trie()
        for word in words:
            trie.addWord(word)

        root = trie.root
        ans = []
        m, n = len(board), len(board[0])

        # 2. 定义内置 DFS 函数，减少 self 调用开销
        def dfs(r: int, c: int, parent_node: Node):
            char = board[r][c]
            cur_node = parent_node.dict[char]

            # 如果找到了一个单词
            if cur_node.word:
                ans.append(cur_node.word)
                cur_node.word = None  # 置空防止重复添加，代替了原先的 flag 逻辑

            # 原地标记已访问
            board[r][c] = '#'

            # 探索四个方向
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] in cur_node.dict:
                    dfs(x, y, cur_node)

            # 回溯恢复现场
            board[r][c] = char

            # 【核心优化：剪枝】如果当前节点没有任何子节点了，说明这个分支已经搜干榨净，从父节点中剔除它
            if not cur_node.dict:
                parent_node.dict.pop(char)

        # 3. 遍历网格
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.dict:
                    dfs(r, c, root)

        return ans
```
