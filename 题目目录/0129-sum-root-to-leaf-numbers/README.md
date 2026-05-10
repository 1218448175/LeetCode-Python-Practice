## [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/)

### 中等

给你一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

- 例如，路径 `1 -> 2 -> 3` 表示数字 `123` 。

返回这些数字之和。

**叶子节点**是指没有任何子节点的节点。

**示例 1：**

<pre><strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>25
<strong>解释：</strong>从根到叶的路径 1→2 表示 12，路径 1→3 表示 13，12 + 13 = 25。
</pre>

**示例 2：**

<pre><strong>输入：</strong>root = [4,9,0,5,1]
<strong>输出：</strong>1026
<strong>解释：</strong>路径 4→9→5 表示 495，4→9→1 表示 491，4→0 表示 40，495 + 491 + 40 = 1026。
</pre>

---

## 题解：自顶向下 DFS 累乘累加

### 1. 核心思路：把路径当成十进制数构造

从根走到叶，每向下一层，相当于在已有高位数字后面补一位：  
**新值 = 上一层累计值 × 10 + 当前节点数字**。

- 到达**叶子**时，这一条根到叶的路径恰好对应一个完整整数，返回 `prevTotal * 10 + root.val`。
- **内部节点**先把当前位并入 `prevTotal`，再对左右子树递归，**答案 = 左子树贡献 + 右子树贡献**（一侧为空时该侧 DFS 遇到空节点返回 `0`）。
- **空节点**不参与任何路径，返回 `0`。

这与 [112. 路径总和](../0112-path-sum) 类似，都是根到叶的 DFS，只是本题的「状态」是已构造的数值而非目标和。

---

### 2. 执行逻辑详细拆解

#### A. 空节点：无路径可算

Python

```
if not root:
    return 0
```

- 递归到空指针时，对总和没有贡献，返回 `0`。

#### B. 叶子节点：形成完整数字

Python

```
if not root.left and not root.right:
    return prevTotal * 10 + root.val
```

- 左右孩子都为空，说明当前节点是叶子；此时从根到这里的十进制数就是 `prevTotal` 左移一位（×10）再加上本位的 `root.val`。

#### C. 非叶子：更新前缀和并分治

Python

```
prevTotal = prevTotal * 10 + root.val
return dfs(root.left, prevTotal) + dfs(root.right, prevTotal)
```

- 先把自己并入「从根到当前节点」的前缀数字，再在相同 `prevTotal` 下递归左右子树。
- 左右返回值相加，即所有根到叶路径所代表数字之和。

---

### 3. 算法可视化

以 `root = [1,2,3]` 为例：

1. **根 1**：非叶，`prevTotal = 0×10+1 = 1`，递归左右。

2. **节点 2**：叶子，返回 `1×10+2 = 12`。

3. **节点 3**：叶子，返回 `1×10+3 = 13`。

4. **汇总**：`12 + 13 = 25`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点访问常数次。

- **空间复杂度**：$O(H)$。$H$ 为树高，主要来自递归栈；链状树时 $H = N$，平衡树约为 $O(\log N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, prevTotal):
            if not root:
                return 0
            if not root.left and not root.right:
                return prevTotal * 10 + root.val
            prevTotal = prevTotal * 10 + root.val
            return dfs(root.left, prevTotal) + dfs(root.right, prevTotal)
        return dfs(root, 0)
```
