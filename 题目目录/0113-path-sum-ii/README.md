## [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/)

### 中等

给你二叉树的根节点 `root` 和一个整数目标和 `targetSum` ，找出所有 **从根节点到叶子节点** 路径总和等于给定目标和的路径。

**叶子节点** 是指没有子节点的节点。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;">

<pre><strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>输出：</strong>[[5,4,11,2],[5,8,4,5]]
</pre>

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;">

<pre><strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>[]
</pre>

**示例 3：**

<pre><strong>输入：</strong>root = [1,2], targetSum = 0
<strong>输出：</strong>[]
</pre>

---

## 题解：DFS + 回溯（自顶向下递减目标值）

### 1. 核心思路：在 112 题基础上记录路径

本题是 [112. 路径总和](https://leetcode.cn/problems/path-sum/) 的升级版。112 题只需要判断「是否存在」这样一条路径，而本题要求**收集所有满足条件的路径**。

核心思想不变：从根出发，每经过一个节点就在 `targetSum` 中扣减当前节点值；走到叶子时，若剩余值恰好为 `0`，则当前路径合法。

关键区别：需要用 `path` 列表**实时记录**当前走过的路径，并在递归返回时**恢复现场（回溯）**，使得 `path` 始终反映「从根到当前节点」的路径。

---

### 2. 执行逻辑详细拆解

#### A. 全局状态：答案列表 + 当前路径

```python
ans = []
path = []
```

- `ans`：存放所有合法路径（二维列表）。
- `path`：维护 DFS 过程中"从根到当前节点"的路径，是**共享的可变状态**。

#### B. 空节点：直接返回

```python
def dfs(node, left):
    if node is None:
        return
```

- 空树 / 递归到底时什么都不做。此检查统一处理了某一侧子树为空的情况。

#### C. 进入当前节点：加入路径并更新剩余目标

```python
path.append(node.val)
left -= node.val
```

- 进入节点时立即把它加入 `path`，同时从目标值中扣减。
- `left` 表示「以当前节点为根，还需要凑多少值才能到达目标和」。

#### D. 叶子节点：判定是否为合法路径

```python
if node.left is None and node.right is None and left == 0:
    ans.append(path.copy())  # 也可以写 path[:]
```

- **必须同时满足三个条件**：是叶子 + 左右都为空 + 剩余值归零。
- `path.copy()` 创建快照保存：因为 `path` 之后会被回溯修改，必须复制一份。

#### E. 非叶子：继续向下搜索

```python
else:
    dfs(node.left, left)
    dfs(node.right, left)
```

- 左右子树各尝试一次，使用 `else` 避免叶子节点重复探索（叶子节点的左右孩子都是 `None`，会被 A 步直接返回）。

#### F. 回溯：恢复现场

```python
path.pop()
```

- **最关键的步骤**：离开当前节点时，必须把它从 `path` 中移除。
- 这保证了从兄弟分支进入时，`path` 不会残留其他分支的节点。

---

### 3. 算法可视化

以示例 `targetSum = 22` 为例，追踪一条合法路径的 `path` 变化：

| 步骤 | 操作 | 当前节点 | `path` | `left` |
|------|------|----------|--------|--------|
| 1 | enter | 5 | `[5]` | 17 |
| 2 | enter | 4 | `[5, 4]` | 13 |
| 3 | enter | 11 | `[5, 4, 11]` | 2 |
| 4 | enter | 7（叶子） | `[5, 4, 11, 7]` | -5 ≠ 0 → 不保存 |
| 5 | pop | 回到 11 | `[5, 4, 11]` | — |
| 6 | enter | 2（叶子） | `[5, 4, 11, 2]` | 0 → 保存 `[5,4,11,2]` |
| 7 | pop | 回到 11 | `[5, 4, 11]` | — |
| 8 | pop | 回到 4 | `[5, 4]` | — |
| 9 | pop | 回到 5 | `[5]` | — |
| 10 | enter | 8 | `[5, 8]` | …继续探索右子树 |

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点访问一次；但若树退化为链且每条前缀都是答案的组成部分，拷贝路径的代价累积为 $O(N^2)$。一般情况下远小于此。

- **空间复杂度**：$O(H)$。其中 $H$ 为树高，来自递归栈和 `path` 列表；链状树最坏 $H = N$，平衡树约为 $O(\log N)$。`ans` 本身的存储不计入额外空间。

---

### 5. 代码实现回顾

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(node: Optional[TreeNode], left: int) -> None:
            if node is None:
                return
            path.append(node.val)
            left -= node.val
            if node.left is None and node.right is None and left == 0:
                ans.append(path.copy())  # 也可以写 path[:]
            else:
                dfs(node.left, left)
                dfs(node.right, left)
            path.pop()  # 恢复现场

        dfs(root, targetSum)
        return ans
```

---

### 6. 与 112 题的对比

| | 112. 路径总和 | 113. 路径总和 II |
|---|---|---|
| **返回值** | `bool`（是否存在） | `List[List[int]]`（所有路径） |
| **核心结构** | 纯递归，`or` 短路 | DFS + 回溯，维护 `path` |
| **叶子判定** | `剩 0 → True`，无需回溯 | `剩 0 → 保存副本`，必须回溯 |
| **空间** | $O(H)$ 递归栈 | $O(H)$ 递归栈 + `path` |

**延伸思考**：如果不仅要返回路径，还要求返回「所有根到叶的路径上节点值之和」，那就是 112 与 113 的混合 —— 用 113 的回溯结构拿到所有路径，再分别求和判断。而 [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/) 进一步放宽了「路径不必始于根、终于叶」的限制，需要用前缀和 + 哈希表优化。
