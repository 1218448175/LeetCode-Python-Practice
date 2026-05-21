## [39. 组合总和](https://leetcode.cn/problems/combination-sum/)

### 中等

给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 **所有不同组合** 。

`candidates` 中的 **同一个数字可以无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合视为不同。

你可以 **按任意顺序** 返回答案。

**示例 1：**

```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。7 本身就是一个候选。
```

**示例 2：**

```
输入：candidates = [2,3,5], target = 8
输出：[[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**

```
输入：candidates = [2], target = 1
输出：[]
```

---

## 题解：排序 + 回溯（可重复选取）

### 1. 核心思路：从 `index` 起选数，保证组合不重复

- 目标：在 `candidates` 中选若干数（可重复），使和为 `target`，收集所有不同组合。
- 用 `path` 记录当前已选数字；`backtrack(index)` 表示下一步只能从 **下标 `index` 及之后** 的候选里继续选。
- 循环 `for i in range(index, n)`：只向右扩展，避免 `[2,3]` 与 `[3,2]` 被当成两种答案。
- 与 [77. 组合](../0077-combinations) 的区别：本题 **允许重复使用同一数字**，因此递归时传入 **`i` 而非 `i + 1`**，同一层可再次选 `candidates[i]`。

---

### 2. 先排序：便于 `sum > target` 时剪枝

- 对 `candidates` 排序后，当前 `path` 的和一旦 **大于** `target`，后面更大的候选只会更超标，可直接 `pop` 并 **结束本层循环**（`return`），不再尝试 `i` 之后的分支。

---

### 3. 回溯分支

每轮循环：

1. `path.append(candidates[i])`，`total = sum(path)`。
2. **`total == target`**：`ans.append(path.copy())`（必须拷贝），`pop` 后 `return`。
3. **`total < target`**：`backtrack(i)` 继续向下选（可再选当前数），回溯 `pop`。
4. **`total > target`**：`pop` 后 `return`（排序剪枝）。

入口 `backtrack(0)`，空 `path` 开始搜索。

---

### 4. 复杂度分析

- **时间复杂度**：与可行组合数量及路径长度相关；排序 $O(n \log n)$，搜索上界约为「和为 `target` 的组合数」乘路径操作，最坏指数级。
- **空间复杂度**：$O(target / \min(candidates))$ 量级的递归栈与 `path`（路径最长约为 `target` 除以最小候选）；输出不计入辅助空间。

---

### 5. 代码回顾

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index: int) -> None:
            for i in range(index, n):
                path.append(candidates[i])
                total = sum(path)
                if total == target:
                    ans.append(path.copy())
                    path.pop()
                    return
                elif total < target:
                    backtrack(i)
                    path.pop()
                else:
                    path.pop()
                    return
        ans = []
        path = []
        n = len(candidates)
        backtrack(0)
        return ans
```

亦可维护 `total` 变量在递归中增减，避免每次 `sum(path)`；正序 `start` + `backtrack(i)` 与倒序枚举写法等价，思想与 [77. 组合](../0077-combinations) 一脉相承。
