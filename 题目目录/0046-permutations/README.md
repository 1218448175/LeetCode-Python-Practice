## [46. 全排列](https://leetcode.cn/problems/permutations/)

### 中等

给定一个 **不含重复数字** 的数组 `nums` ，返回其 **所有可能的全排列** 。你可以 **按任意顺序** 返回答案。

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**

```
输入：nums = [1]
输出：[[1]]
```

---

## 题解：交换法回溯（原地排列）

### 1. 核心思路：固定前缀，交换枚举每一位

- 全排列即对 `nums` 的 $n!$ 种重排各收集一次。
- 用 `backtrack(first)` 表示：前 `first` 个位置已确定，在 `first … n-1` 中通过 **交换** 依次把每个候选数放到下标 `first`。
- 当 `first == n` 时，当前 `nums` 即一种排列，`ans.append(nums[:])`（切片拷贝，避免后续交换污染已收集结果）。

与 [77. 组合](../0077-combinations) 用 `path` 追加不同：本题 **在原数组上交换**，回溯时再换回来。

---

### 2. 单层循环的含义

```text
for i in range(first, n):
    swap(nums[first], nums[i])
    backtrack(first + 1)
    swap 还原
```

- `i == first`：保持不动，用当前数填第 `first` 位；
- `i > first`：把后面的某个数换到 `first`，再递归填 `first+1` 之后的位置。

这样保证每个数都会在各个「首位」出现一次，且不重复生成相同排列（题目保证元素互不相同）。

---

### 3. 复杂度分析

- **时间复杂度**：$O(n \cdot n!)$，共 $n!$ 种排列，每种拷贝长度 $n$。
- **空间复杂度**：$O(n)$ 递归栈；输出数组另计。

---

### 4. 代码回顾

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(first: int) -> None:
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        backtrack(0)
        return ans
```

也可用 `used` 布尔数组 + `path` 的经典回溯写法；交换法省去 `path`/`used`，代码更短。
