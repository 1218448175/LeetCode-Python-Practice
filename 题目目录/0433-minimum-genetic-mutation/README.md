## [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/)

### 中等

基因序列由 `"A"`、`"C"`、`"G"`、`"T"` 组成，长度为 `8`。给定起始串 `startGene`、目标串 `endGene` 以及合法基因库 `bank`（仅其中的串可作为中间状态）。每次变化可将 **某一个位置** 替换为四种字符之一，且得到的新串 **必须出现在 `bank` 中**（目标串也必须在库中才算可达）。求从 `startGene` 变到 `endGene` 的 **最少变化次数**；无法达到返回 `-1`。若起点与终点相同，返回 `0`。

**示例 1：**

```
输入：startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
```

**示例 2：**

```
输入：startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
```

---

## 题解：基因库为节点、单点突变为边的 BFS

### 1. 核心思路：隐式图上的最短路

- 把 `bank` 中的每个串（以及起点）看作 **节点**；若两个串仅 **一个位置** 字符不同，则存在一条 **无权边**，代价为 1 次突变。
- 最少突变次数 = **无权图最短路**，从 `startGene` 做 **BFS** 即可；队列中保存 `(当前串, 已用步数)`。

---

### 2. 特判与合法性

- `startGene == endGene`：无需变化，返回 `0`。
- `endGene` 必须出现在 `bank` 中：题目规定只有库里的串才能作为中间/终点状态，否则 **不可达**，直接返回 `-1`。
- 将 `bank` 转为 `set`，便于 $O(1)$ 判断某个突变串是否合法。

---

### 3. 扩展邻居与去重

- 对当前串的每一位 `i`，枚举替换字符 `y ∈ {A,C,G,T}` 且 `y != cur[i]`，拼接得到 `nxt`。
- 若 `nxt in bank`：若已是 `endGene`，返回答案 `step + 1`；否则将 `nxt` 从 `bank` 中 **删除** 并入队。删除同时起到 **访问标记** 作用，避免重复入队（等价于 `visited` 集合）。

---

### 4. 复杂度分析

- 设基因长为常数 $L=8$，库大小为 $n$。每个串最多尝试 $L \times 3$ 种单点突变，每次 `set` 查询均摊 $O(1)$。
- **时间复杂度**：$O(n \cdot L)$，在 $L$ 固定时为 $O(n)$。
- **空间复杂度**：$O(n)$，存 `bank` 集合与队列。

---

### 5. 代码回顾

```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        bank = set(bank)
        if endGene not in bank:
            return -1
        q = deque([(startGene, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == endGene:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
```

（力扣环境中已提供 `from collections import deque`；本地运行需在文件头部自行补充该导入。）
