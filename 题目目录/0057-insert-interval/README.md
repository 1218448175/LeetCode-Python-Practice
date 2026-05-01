## [57. 插入区间](https://leetcode.cn/problems/insert-interval/)

### 中等

给你一个 **无重叠的** ，按照区间起始端点排序的区间列表 `intervals`，其中 `intervals[i] = [starti, endi]` 表示第 `i` 个区间的开始和结束，并且 `intervals` 按照 `starti` 升序排列。同样给定一个区间 `newInterval = [start, end]` 表示另一个区间的开始和结束。

在 `intervals` 中插入区间 `newInterval`，使得 `intervals` 依然按照 `starti` 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 `intervals`。

**注意** 你不需要原地修改 `intervals`。你可以创建一个新数组然后返回它。

**示例 1：**

<pre><strong>输入：</strong>intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>输出：</strong>[[1,5],[6,9]]
</pre>

---

## 题解：分类讨论与动态边界合并算法

### 1. 核心思路：分治处理与区间融合

这道题是“合并区间”的变体。不同之处在于，输入的 `intervals` 已经是**有序且不重叠**的，这为我们提供了线性处理（$O(N)$）的机会，而不需要重新排序。

你的代码采用了**分类讨论**的策略，将新区间 `newInterval` 与原序列中每个区间 $[l, r]$ 的关系拆解为几种状态，并动态维护一个待插入的“融合区间” `[insert_l, insert_r]`。

---

### 2. 执行逻辑的详细拆解

我们将处理过程分为三个逻辑阶段，这在你的代码中通过 `if-elif` 链体现：

#### A. 第一阶段：新区间左侧（无重叠）

`if r < insert_l:`

- 当前区间完全在待插入区间的左侧。

- **处理**：直接将当前区间加入结果集。

#### B. 第二阶段：重叠与融合（核心逻辑）

`elif l <= insert_r and r >= insert_l:`（对应你代码中处理重叠的多个 `elif`）

- 只要当前区间与待插入区间有交集，就进行“融合”。

- **处理**：更新融合区间的边界。
  
  - `insert_l = min(insert_l, l)`
  
  - `insert_r = max(insert_r, r)`

- 你的代码中通过 `elif l < insert_l <= r` 和 `elif insert_r >= l` 分别细化了左侧重叠和右侧重叠的情况。

#### C. 第三阶段：新区间右侧（无重叠）

`elif insert_r < l:`

- 待插入区间（或融合后的区间）已经处理完毕，且完全在当前区间的左侧。

- **处理**：
  
  1. 如果还没插入融合区间（`if not flag`），先将 `[insert_l, insert_r]` 放入结果集。
  
  2. 再将当前区间加入结果集。
  
  3. 标记 `flag = True`，表示任务已完成。

---

### 3. 逻辑亮点：Flag 位控制插入时机

由于 `newInterval` 可能会被插入到数组中间、开头或末尾，你的代码引入了 `flag` 变量：

- **中间插入**：在遇到第一个完全位于融合区间右侧的元素时插入，并封死后续重复插入的可能。

- **末尾插入**：如果遍历结束 `flag` 仍为 `False`（说明没有遇到比融合区间更靠右的元素），则在循环外补充插入。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。只需一次遍历 `intervals` 数组，所有操作均为常数时间。

- **空间复杂度**：$O(N)$。需要创建一个新数组 `newintervals` 来存储结果。

---

### 5. 实现代码

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        l, r = newInterval

        # 1. 处理左侧不重叠
        while i < n and intervals[i][1] < l:
            res.append(intervals[i])
            i += 1

        # 2. 处理重叠部分，不断吞并
        while i < n and intervals[i][0] <= r:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1
        res.append([l, r])

        # 3. 处理右侧不重叠
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```