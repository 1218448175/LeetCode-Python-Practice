## [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)

### 中等

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;">

<pre><strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[3],[20,9],[15,7]]
</pre>

---

#### 题解：层序遍历（BFS）配合方向旗标实现锯齿形输出

### 1. 核心思路：分层处理 + 结果翻转

锯齿形层序遍历本质上还是 **广度优先搜索（BFS）**。它的核心在于：在逐层遍历二叉树的同时，利用一个“方向旗标”来控制每一层结果的存储顺序。

- **标准探索**：无论输出方向如何，每一层节点的探索（即从左到右寻找子节点）顺序保持不变，这保证了队列逻辑的稳定性。

- **锯齿转换**：引入 `direction` 变量。当处于“左往右”层时，直接存储结果；当处于“右往左”层时，将该层的结果列表进行翻转。

- **按层封装**：你的实现中通过将每一层的节点整体存入一个列表 `ls`，并在队列中处理这些列表，清晰地界定了层的边界。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化

- 创建一个双端队列 `queue`，初始存入包含根节点的列表 `[root]`。

- 设定 `direction = 1`，表示初始方向为从左向右。

#### B. 外层循环：层级切换

- 只要当前层列表 `ls` 中存在有效节点，就继续处理。

- 每次从队列中弹出一整层的节点列表。

#### C. 内层循环：节点处理与子代收集

- **提取值**：遍历当前层的所有节点，忽略 `None`，将有效节点的 `val` 存入 `tmp_list`。

- **扩散**：将每个节点的左、右子节点按序加入 `sub_list`，作为下一层的候选。

- **方向控制**：如果 `direction == -1`（即偶数层，从 0 开始计），则调用 `reverse()` 翻转当前层的数值列表 `tmp_list`。

- **状态更新**：将 `tmp_list` 加入最终结果，将 `sub_list` 送入队列，并执行 `direction *= -1` 切换下一层的方向。

---

### 3. 与双端队列直接插入的对比（可选思路）

另一种做法是在处理每一层时，根据方向决定是将 `node.val` 插入到结果列表的尾部（`append`）还是头部（`appendleft`）。这种做法可以省去 `reverse()` 的操作，但在 Python 中，对 `tmp_list` 进行一次性翻转的效率也非常出色，逻辑更加直观。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。每个节点被访问一次，虽然有翻转操作，但所有层翻转的总代价与节点总数成线性关系。

- **空间复杂度**：$O(n)$。主要空间消耗在于队列中存储的节点以及最终返回的列表。

---

### 5. 代码回顾

```python
from collections import deque
from typing import List, Optional

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 初始判断，处理空树情况
        if not root:
            return []

        queue = deque([[root]])
        res_list = []
        direction = 1 # 1: 左->右, -1: 右->左

        while queue:
            ls = queue.popleft()
            sub_list = []
            tmp_list = []

            for t in ls:
                if not t:
                    continue
                # 始终按从左到右的顺序收集下一层节点
                tmp_list.append(t.val)
                sub_list.append(t.left)
                sub_list.append(t.right)

            if tmp_list:
                # 根据当前方向决定是否翻转结果
                if direction == -1:
                    tmp_list.reverse()
                res_list.append(tmp_list)

                # 只有当前层有效时，才将下一层列表入队并切换方向
                queue.append(sub_list)
                direction *= -1
            else:
                # 如果 tmp_list 为空，说明已经到叶子节点之下，结束循环
                break

        return res_list
```