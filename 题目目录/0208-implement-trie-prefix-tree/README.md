## [208. 实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/)

### 中等

`Trie`（发音类似 "try"）即 **字典树**，是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如拼写检查和自动补全。

请你实现 `Trie` 类：

- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word` 。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**示例：**

```
输入
["Trie", "insert", "search", "search", "startsWith", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["appl"], ["app"], ["app"]]
输出
[null, null, true, false, true, true, null, true]
```

---

## 题解：字典树节点 + 统一查找 `find`

### 1. 核心思路：按字符逐层下探

- 每个节点 `Node` 用 `dict` 存 **子节点**（键为下一字符），用 `end` 标记从根到该节点路径是否构成某个 **已插入完整单词**。
- 根节点不对应任何字符；插入/查询都从 `root` 出发，沿 `word` 或 `prefix` 的每个字符 `c` 在 `cur.dict` 中找下一层。
- 将「是否存在路径」「是否为完整词」合并进一次遍历，避免 `search` 与 `startsWith` 各写一套逻辑。

---

### 2. `insert`：沿路径建边，末节点打标

- 对每个字符 `c`：若 `c not in cur.dict`，新建 `Node()` 并挂到 `cur.dict[c]`。
- 指针 `cur` 下移；整词插入结束后 `cur.end = True`，表示该节点是某个单词的结尾。

---

### 3. `find` 的三种返回值

沿 `word` 向下走，若中途某字符不存在子节点，返回 **`0`**（连前缀都不存在）。

走完全部字符后：

- **`2`**：路径存在且 `cur.end == True` → 曾插入过 **完整单词** `word`；
- **`1`**：路径存在但 `cur.end == False` → 只是某更长词的前缀，或从未以该串为完整词插入。

对外接口：

- `search(word)`：`find(word) == 2`（必须完整匹配）；
- `startsWith(prefix)`：`find(prefix) != 0`（只要前缀路径存在即可，不要求 `end`）。

---

### 4. 复杂度分析

设单词长度为 $L$，已插入单词总字符数为 $N$（建树规模）。

- **`insert`**：单次 $O(L)$。
- **`search` / `startsWith`**：单次 $O(L)$。
- **空间复杂度**：$O(N)$，与所有插入字符总数同阶（共享前缀的节点会复用）。

---

### 5. 代码回顾

```python
class Node:
    def __init__(self):
        self.dict = dict()
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.end = True

    def find(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                return 0    # 没有匹配的字符串
            cur = cur.dict[c]
        if cur.end:
            return 2    # 完全匹配
        return 1    # 匹配前缀

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0
```

也可用 **固定大小数组**（如 26 个字母槽）代替 `dict`，在仅含小写字母时略省常数；本题用哈希字典更通用，写法也更短。
