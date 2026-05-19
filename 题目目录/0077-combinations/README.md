## [77. 组合](https://leetcode.cn/problems/combinations/)

### 中等

给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 **k 个数的组合** 。

你可以按 **任何顺序** 返回答案。

**示例 1：**

```
输入: n = 4, k = 2
输出: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**示例 2：**

```
输入: n = 1, k = 1
输出: [[1]]
```

---

## 题解：回溯 + 倒序枚举剪枝

### 1. 核心思路：从大到小选数，保证组合不重复

- 在 `[1, n]` 中选 `k` 个数，顺序无关（`[1,2]` 与 `[2,1]` 视为同一组合）。
- 用 `path` 记录当前已选数字，`back(num)` 表示下一步只能从 **不超过 `num`** 的数里继续选（倒序 `i = num, num-1, ...`），自然保证组合内 **严格递减**，避免 `[2,1]` 与 `[1,2]` 重复。
- 当 `len(path) == k` 时，将 `path.copy()` 加入 `ans`（必须拷贝，否则后续 `pop` 会改掉已收集的列表）。

---

### 2. 剪枝：`d = k - len(path)`

还需再选 `d` 个数。当前从 `num` 往下枚举，若 `i` 太小则后面不够 `d` 个可选数。

循环 `for i in range(num, d - 1, -1)`：当 `i < d` 时，即使把 `1..i` 全选上也不足 `d` 个，更大范围的 `i` 更不必试，故下界为 `d`（`range` 右端 `d-1` 即最后一项为 `d`）。

---

### 3. 回溯三步

1. `path.append(i)`  
2. `back(i - 1)` — 下一层只能从比 `i` 更小的数里选  
3. `path.pop()`  

入口 `back(n)`：第一个数最大可从 `n` 开始。

---

### 4. 复杂度分析

- **时间复杂度**：共 $\binom{n}{k}$ 种组合，每种复制长度 $k$ 的列表，约为 $O(k \cdot \binom{n}{k})$。
- **空间复杂度**：$O(k)$ 递归栈与 `path`；输出不计入辅助空间。

---

### 5. 代码回顾

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def back(num: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return

            for i in range(num, d - 1, -1):
                path.append(i)
                back(i - 1)
                path.pop()

        back(n)
        return ans
```

亦可正序 `for i in range(start, n+1)` 并传 `start`，思想相同；倒序 + 下界剪枝写法更紧凑。
