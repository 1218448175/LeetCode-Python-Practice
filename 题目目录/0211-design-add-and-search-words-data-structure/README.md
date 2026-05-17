## [211. 添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/)

### 中等

请你设计一个数据结构，支持 **添加新单词** 和 **查找字符串是否与任何先前添加的字符串匹配** 。

实现 `WordDictionary` 类：

- `WordDictionary()` 初始化字典树对象。
- `void addWord(word)` 将 `word` 添加到数据结构中，之后可以对它进行匹配。
- `bool search(word)` 如果数据结构中存在与 `word` **匹配** 的字符串，返回 `true` ；否则，返回 `false` 。`word` 中可能包含一些 **`.`** ，每个 `.` 都可以表示任何一个字母。

**示例：**

```
输入
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出
[null,null,null,null,false,true,true,true]
```

---

## 题解：字典树插入 + DFS 处理通配符 `.`

### 1. 核心思路：在 208 的 Trie 上扩展「模糊查询」

- `addWord` 与 [208. 实现 Trie](../0208-implement-trie-prefix-tree) 的 `insert` 相同：沿字符建 `Node`，词尾 `end = True`。
- `search` 在普通 Trie 逐字符匹配的基础上，遇到 **`.`** 时需尝试 **当前节点的所有子分支**，用 DFS 回溯枚举可能路径；无 `.` 时与普通 Trie 查找一致。

---

### 2. `addWord`：标准字典树插入

对每个字符 `c`，若不存在则 `cur.dict[c] = Node()`，最后 `cur.end = True`。

---

### 3. `dfs(cur, word, i)` 的三种分支

- **`i >= len(word)`**：已消费完查询串，仅当 `cur.end` 为真才表示匹配到某个 **完整已插入单词**。
- **`word[i] == '.'`**：通配一位字母，对 `cur.dict` 中 **每个子节点** 递归 `dfs(node, word, i + 1)`，任一成功即 `True`（代码用 `ans = ans or ...` 聚合）。
- **普通字母 `c`**：若 `c not in cur.dict` 返回 `False`；否则沿 `cur.dict[c]` 继续 `dfs(..., i + 1)`。

`search` 入口：`return self.dfs(self.root, word, 0)`。

---

### 4. 复杂度分析

设单词长度为 $L$，字典中已存单词总字符数为 $N$，查询串长度为 $M$。

- **`addWord`**：单次 $O(L)$。
- **`search`**：最坏情况下每个 `.` 都可能展开为 $O(\Sigma)$ 个子节点（$\Sigma$ 为字符集大小，小写字母为 26），最坏约 $O(26^M)$；平均取决于词库结构与通配符个数。
- **空间复杂度**：建树 $O(N)$；DFS 递归栈 $O(M)$。

---

### 5. 代码回顾

```python
class Node:
    def __init__(self):
        self.dict = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.end = True

    def dfs(self, cur: str, word: str, i: int) -> bool:
        ans = False
        if i >= len(word):
            return cur.end
        c = word[i]
        if c == ".":
            for node in cur.dict.values():
                ans = ans or self.dfs(node, word, i + 1)
            return ans
        if c not in cur.dict:
            return False
        return self.dfs(cur.dict[c], word, i + 1)

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
```

（`dfs` 第一个参数类型标注写为 `Node` 更准确；力扣提交以运行逻辑为准。）
