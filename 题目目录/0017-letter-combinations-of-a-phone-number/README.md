## [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

### 中等

给定一个仅包含数字 `2-9` 的字符串 `digits`，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

数字到字母的映射与手机按键相同（`2`→`abc`，`3`→`def`，…）。`0` 和 `1` 不映射任何字母。

**示例 1：**

```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
输入：digits = ""
输出：[]
```

**示例 3：**

```
输入：digits = "2"
输出：["a","b","c"]
```

---

## 题解：回溯枚举每一位上的字母

### 1. 核心思路：按位选择，路径即当前组合

- 将 `digits` 看作长度为 $n$ 的 **多叉树**：第 `index` 层对应第 `index` 个数字，该层有 3～4 个分支（该键上的字母）。
- 用 `combination` 列表记录当前路径，DFS 到 `index == len(digits)` 时，用 `"".join(combination)` 得到一条完整组合并加入 `combinations`。
- 这是典型的 **回溯**：`append` → 递归下一层 → `pop` 恢复，尝试同一层上的其他字母。

---

### 2. `phones` 映射与 `back(index)`

- `phones` 字典把 `'2'`…`'9'` 映射到对应字母列表，避免在递归里写一长串 `if-elif`。
- `back(index)`：
  - **终止**：`index == len(digits)` → 收集当前路径；
  - **扩展**：取 `num = digits[index]`，遍历 `phones[num]` 中每个 `letter`，压入、递归 `back(index + 1)`、弹出。

---

### 3. 复杂度分析

设 `digits` 长度为 $n$，每位平均约 3～4 个字母，组合总数上界约为 $O(4^n)$（最坏每位 4 个字母）。

- **时间复杂度**：$O(4^n \cdot n)$，要生成每个组合并 `join` 成长度 $n$ 的字符串。
- **空间复杂度**：$O(n)$ 递归栈与 `combination` 路径；输出数组不计入额外空间分析时常说的「辅助空间」。

---

### 4. 代码回顾

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phones = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def back(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                num = digits[index]
                for letter in phones[num]:
                    combination.append(letter)
                    back(index + 1)
                    combination.pop()

        combination = []
        combinations = []

        back(0)
        return combinations
```

（力扣对 `digits == ""` 要求返回 `[]`；若需严格符合，可在 `back(0)` 前增加 `if not digits: return []`。）

同类写法也可用迭代（队列逐层扩展）或 BFS 思想；本题回溯最直观。
