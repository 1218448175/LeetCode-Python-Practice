## [155. 最小栈](https://leetcode.cn/problems/min-stack/)

### 中等

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

**示例 1:**

<pre><strong>输入：</strong>
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>输出：</strong>
[null,null,null,null,-3,null,0,-2]

<strong>解释：</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
</pre>

**提示：**

- `-231 <= val <= 231 - 1`
- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用
- `push`, `pop`, `top`, and `getMin`最多被调用 `3 * 104` 次

---

## 题解：辅助栈（Auxiliary Stack）同步策略

### 1. 核心思路：空间换时间

本题的要求是在 **常数时间 $O(1)$** 内检索到最小元素。普通的栈只能在 $O(1)$ 内完成 `push` 和 `pop`，但找最小值通常需要 $O(N)$。

你的代码采用了经典的 **“辅助栈”** 方案：

- **数据栈 (`self.stack`)**：按正常顺序存储所有元素，负责处理 `top()` 和基本的 `push/pop`。

- **最小栈 (`self.min_st`)**：专门存储“单调非递增”的最小值序列。它的栈顶永远是当前数据栈中所有元素的最小值。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化阶段

`self.min_st = [float(inf)]`

在最小栈中预设一个“正无穷大”作为哨兵值。这非常巧妙，因为它简化了第一次 `push` 时的判断逻辑，确保任何第一个进入的数值都能顺利成为当前的最小值。

#### B. 元素入栈 (`push`)

1. 数据栈正常 `append(val)`。

2. **判定条件**：`if val <= self.min_st[-1]`。
   
   - 只有当新元素 **小于或等于** 当前最小值时，才将其压入最小栈。
   
   - **注意**：使用 `<=` 而不是 `<` 是为了处理重复的最小值（例如先后压入两个 2，如果不重复压入 2，当弹出一个 2 时，最小栈会错误地把唯一的 2 弹掉）。

#### C. 元素出栈 (`pop`)

1. 数据栈执行 `pop()` 获取弹出值 `pop_num`。

2. **同步判定**：`if pop_num == self.min_st[-1]`。
   
   - 如果弹出的数值恰好是当前的最小值，那么辅助栈也必须执行 `pop()`。
   
   - 这保证了辅助栈的栈顶始终与数据栈现存的最小值保持同步。

#### D. 获取最小值 (`getMin`)

直接返回 `self.min_st[-1]`。由于辅助栈的特性，这个操作不需要任何遍历，直接达成了 $O(1)$ 的目标。

---

### 3. 算法可视化

假设执行序列：`push(5), push(3), push(6), push(3), pop()`

| **操作**    | **数据栈 stack**  | **最小栈 min_st**   | **说明**             |
| --------- | -------------- | ---------------- | ------------------ |
| `init`    | `[]`           | `[inf]`          | 初始化                |
| `push(5)` | `[5]`          | `[inf, 5]`       | 5 < inf，入最小栈       |
| `push(3)` | `[5, 3]`       | `[inf, 5, 3]`    | 3 < 5，入最小栈         |
| `push(6)` | `[5, 3, 6]`    | `[inf, 5, 3]`    | 6 > 3，最小栈不动        |
| `push(3)` | `[5, 3, 6, 3]` | `[inf, 5, 3, 3]` | 3 <= 3，入最小栈 (处理重复) |
| `pop()`   | `[5, 3, 6]`    | `[inf, 5, 3]`    | 弹出值 3 == 最小栈顶，同步弹出 |

---

### 4. 复杂度分析

- **时间复杂度**：所有操作（`push`, `pop`, `top`, `getMin`）均为 **$O(1)$**。

- **空间复杂度**：**$O(N)$**。在最坏情况下（元素是降序排列的），辅助栈需要存储和数据栈一样多的元素。

---

### 5. 代码回顾

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_st = [float(inf)]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        pop_num = self.stack.pop()
        if pop_num == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```