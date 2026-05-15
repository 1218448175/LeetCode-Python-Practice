## [207. 课程表](https://leetcode.cn/problems/course-schedule/)

### 中等

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **先** 要学习课程 `bi` ：

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，需要先完成课程 `1` 。

判断是否可能完成全部课程？

**示例 1：**

```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```

**示例 2：**

```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。课程 1 要求先修课程 0 ，课程 0 又要求先修课程 1 。因此不可能完成。
```

---

## 题解：三色标记 DFS（有向图环检测）

### 1. 核心思路：先修依赖 = 有向边，可否修完课 = 是否存在环

- 条件 `prerequisites[i] = [a, b]` 表示要学 `a`，必须先学完 `b`，相当于 **图中存在有向边 `b → a`**（`b` 指向 `a`）。
- 若图中存在 **有向环**，则要求互相等待，无法排课；**无环** 则存在拓扑序，可以修完所有课程。
- 本题代码采用 **DFS + 三色标记** 判断有向图中是否存在环，与拓扑排序判定等价。

三色含义：

- **`0`（白色）**：尚未访问；
- **`1`（灰色）**：在当前 DFS 路径上（递归栈中的节点）；
- **`2`（黑色）**：该节点及其后缀已处理完毕。

若在 DFS 过程中从某个节点走到了 **灰色** 节点，说明沿当前路径又回到「栈中」节点，即 **存在回路** ，应返回不可能修完。

---

### 2. 建图与 DFS 逻辑的拆解

#### A. 邻接表

对每条 `[a, b]`，向 `g[b]` 追加 `a`，表示学完 `b` 后才能去学 `b` 的出边邻居（即后续课程）。

#### B. 递归返回值的语义

函数 `dfs(x)`：**若从 `x` 出发 DFS 一旦发现环则返回 `True`**；否则回溯前将 `x` 标记为黑色并返回 `False`。

对邻居 `y`：

- 若 `y` 为灰色（`colors[y] == 1`），已在当前路径上，**即刻判定存在环**，返回 `True`；
- 若 `y` 为白色，需继续 `dfs(y)`；若递归为真则向上传递 `True`；
- 若 `y` 为黑色，说明该枝条已无非环争议，跳过即可。

⚠️ 注意条件写法（`or` 与 `and` 的优先级）：`colors[y] == 1 or colors[y] == 0 and dfs(y)` 等价于「遇到灰则真，否则在白点上继续深搜」，黑点上两式皆假，不产生误判。

---

### 3. 算法可视化（简化）

示例 `prerequisites = [[1,0],[0,1]]`，边为 `0 → 1` 与 `1 → 0`。

1. 从 `0` 开始：标记灰，沿边到 `1`；
2. `1` 标记灰，沿边又回到 `0`，此时 `0` 为灰 ⇒ **检测到环**，返回不可能修完。

若图为 `0→1→2` 无环链，DFS 会先一路标灰下探，回溯时逐个标黑，全程不会「遇到灰邻居」，故能修完。

---

### 4. 复杂度分析

- **时间复杂度**：$O(V + E)$。$V = \texttt{numCourses}$，$E$ 为先修的对数；每条边与每点至多访问常数次。
- **空间复杂度**：$O(V + E)$。邻接表存边；递归栈最坏 $O(V)$；颜色数组 $O(V)$。

---

### 5. 代码回顾

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses
        def dfs(x: int) -> bool:
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False

        return True
```

同类思路还可实现 **Kahn 算法（入度 + 队列）** 做拓扑排序；本题用三色 DFS 一次遍历即可判定是否可修完。
