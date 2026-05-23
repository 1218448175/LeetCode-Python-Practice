## [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

### 中等

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

---

## 题解：回溯 + 左/右括号计数

### 1. 核心思路：`left` / `right` 控制可选分支

- 目标：生成 `n` 对括号的所有合法组合（任意时刻前缀中 `(` 数量不少于 `)`）。
- 用长度 `2 * n` 的 `path` 数组逐位填字符，最终 `"".join(path)` 得到一条答案。
- `backtrack(left, right)`：`left` 为已放 `(` 个数，`right` 为已放 `)` 个数；当前写入下标为 **`left + right`**（已填字符总数）。
- **`right == n`**：右括号已放满，字符串长度必为 `2n`，收集答案。

---

### 2. 两条递归分支与合法性

1. **`left < n`**：还可放左括号 → 在 `path[left + right]` 写 `'('`，递归 `backtrack(left + 1, right)`。
2. **`right < left`**：右括号数量仍少于左括号 → 在 `path[left + right]` 写 `')'`，递归 `backtrack(left, right + 1)`。

`right < left` 等价于「当前前缀合法且还能补右括号」；若允许 `right == left` 时继续放 `)`，会产生非法前缀，故 **不** 在该条件下放右括号。

---

### 3. 与组合/排列类回溯的对比

- 与 [77. 组合](../0077-combinations)、[39. 组合总和](../0039-combination-sum) 同属回溯枚举，但状态不是「选哪个数」，而是 **两种括号各还能放几个**。
- 无需额外去重：按「先尽量放 `(`，再在合法时放 `)`」的 DFS 顺序，每种合法括号串只生成一次。

---

### 4. 复杂度分析

- **时间复杂度**：答案数为第 `n` 个卡特兰数 $C_n$，约为 $O(4^n / n^{3/2})$；每条路径填 `2n` 个字符并 `join`，总时间与输出规模同阶。
- **空间复杂度**：$O(n)$ 递归栈（`left + right` 最深 `2n` 层，但有效递归深度由括号计数约束）；`path` 固定 `2n`；输出不计入辅助空间。

---

### 5. 代码回顾

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * 2 * n
        def backtrack(left: int, right: int):
            if right == n:
                ans.append("".join(path))
            if left < n:
                path[left + right] = '('
                backtrack(left + 1, right)
            if right < left:
                path[left + right] = ')'
                backtrack(left, right + 1)
        backtrack(0, 0)
        return ans
```

亦可用 `path` 为字符串、`append`/`pop` 写法；固定数组 + 下标 `left + right` 避免频繁拼接，思路与 [46. 全排列](../0046-permutations) 的「固定路径数组回填」类似。
