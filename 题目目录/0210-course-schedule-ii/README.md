## [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)

### 中等

现在你总共有 `numCourses` 门课需要选，记为 `0` 到 `numCourses - 1` 。

给你一个数组 `prerequisites` ，其中 `prerequisites[i] = [ai, bi]` ，表示在选修课程 `ai` 前 **必须先** 选修课程 `bi` ：

- 例如，想要学习课程 `0` ，你需要先完成课程 `1` ，并以 `[0,1]` 表示。

返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 **任意一种** 就可以了。如果不可能完成所有课程，返回 **空数组** 。

**示例 1：**

```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课。要学课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
```

**示例 2：**

```
输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课。先学课程 0 后，还有三门课，且课程 1 和 2 都要求先学课程 0 。随后学课程 1 和 2 ，才能学课程 3 。因此一个正确的顺序是 [0,1,2,3] 。
```

**示例 3：**

```
输入：numCourses = 1, prerequisites = []
输出：[0]
```

---

## 题解：三色 DFS 判环 + 后序收集再反转（拓扑序）

### 1. 核心思路：与 207 相同的判环，多一步「输出一种拓扑序」

- 先修关系 `[a, b]` 仍建模为 **有向边 `b → a`**（学完 `b` 才能学 `a`）。
- **无环** 时，图是 DAG，存在拓扑排序；**有环** 时无解，返回空列表 `[]`。
- 判环方式与 [207. 课程表](../0207-course-schedule) 一致：**三色 DFS**。灰点表示「当前递归栈上」，若 DFS 走到灰点则存在环。
- 在确认无环的前提下，需要在 DFS **回溯前**（节点即将标为「已完成」、颜色改为 `2` 时）把节点加入列表；这样得到的是 **DFS 完成序（后序）**。对 DAG 而言，**将该后序反转** 即得到一种合法的 **拓扑序**（所有边都从序号小的指向序号大的）。

---

### 2. 执行逻辑的拆解

#### A. 邻接表

对每条 `[a, b]`，执行 `g[b].append(a)`，表示 `b` 的后继课程包含 `a`。

#### B. 三色与判环

- `0`：未访问；`1`：在栈上（灰）；`2`：已处理完（黑）。
- `dfs` 若发现环返回 `True`，主函数中遇到则直接 `return []`。

#### C. 后序与 `ans[::-1]`

- 在无环路径上，会先一路递归到「没有未处理后继」的节点，再逐层回溯。
- 在 `colors[x] = 2` 之前执行 `ans.append(x)`，等价于 **后序** 记录完成时刻。
- 拓扑序要求：对每条边 `u → v`，`u` 在序列中出现在 `v` **之前**。后序里 `v` 往往先于 `u` 入表，故最后 **`return ans[::-1]`** 得到一种可行课表。

---

### 3. 复杂度分析

- **时间复杂度**：$O(V + E)$。$V = \texttt{numCourses}$，$E$ 为先修条数。
- **空间复杂度**：$O(V + E)$。邻接表、颜色数组、答案列表及递归栈。

---

### 4. 代码回顾

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        colors = [0] * numCourses
        ans = []
        def dfs(x: int) -> bool:
            colors[x] = 1
            nonlocal ans
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            ans.append(x)
            return False

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return []
        return ans[::-1]
```

同类做法还有 **Kahn 算法（入度 + 队列）**，边弹出边减入度，队列出队顺序本身即一种拓扑序；本题用 DFS 后序反转，与 207 代码结构高度一致，便于对照理解。
