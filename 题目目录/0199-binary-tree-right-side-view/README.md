## [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

### 中等

给定一个二叉树的 **根节点** `root`，想象自己站在树的右侧，返回从顶部到底部看到的节点值序列。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg" style="width: 400px; height: 262px;">

<pre><b>输入：</b>root = [1,2,3,null,5,null,4]
<b>输出：</b>[1,3,4]
</pre>

**示例 2：**

<pre><b>输入：</b>root = [1,null,3]
<b>输出：</b>[1,3]
</pre>

**示例 3：**

<pre><b>输入：</b>[]
<b>输出：</b>[]
</pre>

**提示：**

- 二叉树的节点个数的范围是 `[0,100]`
- `-100 <= Node.val <= 100`

---

## 题解：先右后左 DFS，每层首次访问即「右视」

### 1. 核心思路：站在右边看到的是每一层最靠右的节点

对每一层深度，从右侧看过去只能看到**该层最右边**那个节点。若用**宽度优先（BFS）**逐层扫描，取每层最后一个值即可。

本题代码采用等价思路的 **DFS**：遍历时**先走右子树、再走左子树**。这样第一次到达某一深度 `level` 时，一定是该层从右往左第一个被访问到的节点，也就是站在右边能看到的那个节点。

用 `self.size` 表示「已经记录了多少层」：当 `level == self.size` 时，说明当前节点是**新深度第一次出现**，将其值加入答案，并把 `size` 加一。

---

### 2. 执行逻辑拆解

#### A. 初始化

Python

```
self.ans = []
self.size = 0
```

- `ans`：最终右视图序列。
- `size`：已覆盖的层数（同时也是下一层应匹配的深度下标）。

#### B. DFS：`先右后左` + 按层去重

Python

```
def DFS(root, level):
    if not root:
        return
    if level == self.size:
        self.ans.append(root.val)
        self.size += 1
    DFS(root.right, level + 1)
    DFS(root.left, level + 1)
```

- 空节点直接返回。
- `level == self.size`：当前深度尚未在答案中出现，由于先右后左，此时的 `root` 即为该层最右可见节点。
- 递归顺序**必须先 `right` 再 `left`**，才能保证「每层第一个被访问到的」是最右节点。

#### C. 入口

Python

```
DFS(root, 0)
return self.ans
```

- 从根、深度 `0` 开始。

---

### 3. 算法可视化（示例 1）

树 `[1,2,3,null,5,null,4]`：根在深度 `0`，先访问 `1`，此时 `level == size` → 记录 `1`，`size` 变为 `1`。  
接着**先右后左**：进入右子 `3`（深度 `1`），`level == size` → 记录 `3`，`size` 变为 `2`。  
在 `3` 上继续先右：`4`（深度 `2`），`level == size` → 记录 `4`，`size` 变为 `3`。  
之后回溯再访问左子 `2` 与 `5` 时，深度 `1`、`2` 均已「登记」，不再追加。结果为 `[1,3,4]`。

（同类题也可用 **BFS**：队列逐层弹出，每层最后一个节点的值入答案。）

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点访问一次。
- **空间复杂度**：$O(H)$。$H$ 为树高，递归栈深度；最坏链状 $O(N)$。结果数组另计 $O(H)$ 层数。

---

### 5. 代码实现回顾

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.size = 0
        def DFS(root, level):
            if not root:
                return
            if level == self.size:
                self.ans.append(root.val)
                self.size += 1
            DFS(root.right, level + 1)
            DFS(root.left, level + 1)

        DFS(root, 0)
        return self.ans
```
