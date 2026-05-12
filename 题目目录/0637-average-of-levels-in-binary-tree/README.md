## [637. 二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

### 简单

给定一个非空二叉树的根节点 `root`，以数组的形式返回每一层的平均值。与实际计算结果相差不超过 `10^-5` 的答案会被接受。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" style="width: 300px; height: 169px;">

<pre><strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[3.00000,14.50000,11.00000]
<strong>解释：</strong>第 0 层的平均值为 3 ，第 1 层的平均值为 9 和 20 的平均值 14.5 ，第 2 层的平均值为 15 和 7 的平均值 11 。
</pre>

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" style="width: 300px; height: 224px;">

<pre><strong>输入：</strong>root = [3,9,20,15,7]
<strong>输出：</strong>[3.00000,14.50000,20.00000]
</pre>

---

## 题解：层序遍历（BFS）按层求和再取平均

### 1. 核心思路：一层一层处理

题目要的是**每一层**所有节点值的**算术平均**。二叉树按层统计，最自然的做法是 **广度优先搜索（BFS）**：

- 用队列保存**当前层**待访问的节点。
- 每次处理队列时，先记下当前队列长度 `size`，这正好等于当前层的节点个数。
- 连续弹出 `size` 个节点，累加它们的 `val`，并把非空的左右子节点依次入队，即完成一层。
- 该层平均值为 `total / size`，加入答案数组。

这样不需要额外标记深度，**“当前队列长度”** 就界定了层的边界。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化

- 将根节点 `root` 放入 `deque`（双端队列），作为第一层。

#### B. 外层循环：只要队列非空，就还有层要处理

#### C. 内层循环：处理一整层

1. 用 `size = len(queue)` 固定**本层节点数**，避免在处理过程中因入队而改变循环次数。

2. 循环 `size` 次：弹出队首节点，把 `node.val` 累加到 `total`；若左、右子存在，则入队。

3. 内层循环结束后，`total / size` 即本层平均值，追加到结果列表。

---

### 3. 与 DFS 带深度的对比（可选思路）

也可以用 **DFS** 递归，额外传入当前深度 `depth`，用列表按深度累加 `sum` 与 `count`，最后对每个深度做除法。两种写法时间都是 $O(n)$；本题 BFS 更直观，且与“按层输出”的题（如层序遍历模板）一致。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。每个节点入队、出队各一次，每条边各访问一次。

- **空间复杂度**：$O(w)$。其中 $w$ 为树的最大宽度（一层中最多节点数）；最坏情况下接近 $O(n)$（例如满层最后一层）。

---

### 5. 代码回顾

```python
import collections
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root])
        ans = list()
        while queue:
            total = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                total += node.val
                l, r = node.left, node.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
            ans.append(total / size)
        return ans
```
