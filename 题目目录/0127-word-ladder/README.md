## [127. 单词接龙](https://leetcode.cn/problems/word-ladder/)

### 困难

给定两个单词 `beginWord`、`endWord` 和一个字典 `wordList`（所有单词 **长度相同**）。每次变换只能改 **恰好一个字母**，且中间结果必须在字典中出现（`endWord` 也必须在字典中才算可达）。求从 `beginWord` 到 `endWord` 的 **最短转换序列的长度**（序列包含首尾两个词）；无法到达则返回 `0`。

**示例 1：**

```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog" ，返回 5。
```

**示例 2：**

```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，无法转换。
```

---

## 题解：单词与「通配模式」建二分图 + BFS

### 1. 核心思路：用虚拟节点压缩邻接

- 朴素想法是对每个词枚举改一位再查是否在字典中，邻居数多、字典大时开销高。
- 本题代码采用经典 **建图技巧**：对每个单词的每一位，将该位换成通配符 `*`，得到模式串（如 `hot` → `*ot`、`h*t`、`ho*`）。**原词与模式各为图上的节点**，在「词 `w`」与「`w` 能生成的模式 `p`」之间连 **无向边**。
- 若两个词只差一位，它们必与 **同一个模式** 相邻，从而在图中通过 **词 → 模式 → 词** 用 **2 条边** 表示一次合法变换。

---

### 2. `addWord` / `addEdge` 在做什么

- `wordId`：为每个出现过的「词或模式」分配连续编号；`edge`：邻接表。
- `addEdge(word)`：先登记 `word`，再对每个位置 `i` 把该位改成 `*` 得到 `newWord`，同样登记后，在 **原词编号** 与 **模式编号** 之间各加一条无向边（双向 `append`）。

对 `wordList` 中每个词调用 `addEdge`，再对 `beginWord` 调用一次（起点可能不在列表里）。若 `endWord` 从未被登记（不在字典），直接返回 `0`。

---

### 3. BFS 与答案 `dis[endId] // 2 + 1`

- `dis` 为从 `beginWord` 对应节点出发的最短 **边数**（无权图 BFS）。
- 从 `beginWord` 到 `endWord` 的任意一条最短路在「词—模式—词—…」结构上，**每真实跳变一个合法单词对应图上的 2 条边**。
- 因此序列长度（包含起点与终点两个词）为：**边数 ÷ 2 + 1**，即 `dis[endId] // 2 + 1`。

---

### 4. 复杂度分析

设单词个数为 $N$，长度为 $L$。节点数约为 $O(N \cdot L)$（每个词对应 $L$ 个模式，模式会去重），边数同阶。

- **时间复杂度**：建图 $O(N \cdot L^2)$（每个词 $L$ 个模式，拼接长度 $L$）；BFS $O(V + E)$，总览为关于 $N, L$ 的多项式级别。
- **空间复杂度**：$O(N \cdot L)$ 存 `wordId` 与邻接表。

---

### 5. 代码回顾

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp
        wordId = dict()
        edge = defaultdict(list)
        nodeNum = 0
        for word in wordList:
            addEdge(word)
        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        q = deque([beginId])
        while q:
            x = q.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    q.append(it)
        return 0
```

（力扣环境已提供 `from collections import defaultdict, deque`；本地运行需在文件头部自行补充。）

同类题还可双向 BFS 或单向 BFS + 按位枚举邻居；本题展示的是 **通配虚拟点** 建图写法。
