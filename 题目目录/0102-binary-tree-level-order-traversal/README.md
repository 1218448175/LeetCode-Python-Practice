## [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

### 中等

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;">

<pre><strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[3],[9,20],[15,7]]
</pre>

---

## 题解：层序遍历（BFS）计算层级均值

### 1. 核心思路：利用队列进行分层统计

本题是**二叉树层序遍历**的直接变体。核心目标是计算每一层节点的算术平均值。

- **分层界定**：使用广度优先搜索（BFS），通过在每一层开始前记录队列的长度 `size`，我们可以精确地知道当前层有多少个节点。

- **均值计算**：在处理当前层的 `size` 个节点时，累加它们的值 `total`。该层处理完毕后，平均值即为 `total / size`。

- **结果存储**：将每一层的平均值按顺序存入结果数组。

---

### 2. 执行逻辑详细拆解

#### A. 初始化

- 使用 `collections.deque`（双端队列）存储节点，初始将根节点 `root` 入队。

- 由于题目规定树是非空的，因此无需处理 `root` 为空的情况。

#### B. 外层循环：层级迭代

- `while queue`：只要队列中还有节点，说明树还没遍历完，继续处理下一层。

#### C. 内层循环：节点累加与扩散

- **固定窗口**：`size = len(queue)`。这一步至关重要，它“捕获”了当前层的所有节点，确保后续入队的子节点（属于下一层）不会干扰当前层的均值计算。

- **处理节点**：通过 `for` 循环运行 `size` 次，弹出队首节点并累加其 `val`。

- **准备下一层**：在弹出节点的同时，将其非空的左右子节点放入队尾。

#### D. 计算并记录

- 内层循环结束后，当前层所有节点已处理完毕，计算 `total / size` 并存入 `ans`。

---

### 3. 算法可视化

以 `root = [3, 9, 20, 15, 7]` 为例：

1. **第 0 层**：队列 `[3]`，`size=1`。
   
   - 弹出 `3`，`total=3`。
   
   - 加入子节点 `9, 20`。
   
   - 均值：$3 / 1 = 3.0$。

2. **第 1 层**：队列 `[9, 20]`，`size=2`。
   
   - 依次弹出 `9` 和 `20`，`total=29`。
   
   - 加入子节点 `15, 7`。
   
   - 均值：$29 / 2 = 14.5$。

3. **第 2 层**：队列 `[15, 7]`，`size=2`。
   
   - 依次弹出 `15` 和 `7`，`total=22`。
   
   - 均值：$22 / 2 = 11.0$。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点入队和出队各一次，总访问次数与节点数呈线性关系。

- **空间复杂度**：$O(M)$。其中 $M$ 是树的最大宽度（即同一层节点数最多的一层）。在最坏情况下（满二叉树），最后一层节点数约为 $N/2$。

---

### 5. 代码实现回顾

```pyt
import collections
from typing import List, Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 1. 初始化队列，将根节点放入
        queue = collections.deque([root])
        ans = []

        while queue:
            total = 0
            # 2. 获取当前层的节点个数
            size = len(queue)

            # 3. 遍历当前层的所有节点
            for _ in range(size):
                node = queue.popleft()
                total += node.val

                # 4. 将下一层的子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 5. 计算本层平均值并保存
            ans.append(total / size)

        return ans
```