## [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)

### 中等

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>s = "PAYPALISHIRING", numRows = 3
<strong>输出：</strong>"PAHNAPLSIIGYIR"
</pre>

---

## 题解：周期模运算模拟法

### 1. 核心思路：寻找“规律周期”

Z 字形变换本质上是在 `numRows` 个列表（行）中循环填充字符。

观察排列规律：字符先从第一行走到最后一行（下行），再从倒数第二行折返向上走到第二行（上行）。

这种“折返”形成了一个循环周期。周期的长度 $T$ 的计算公式为：

$$T = 2 \times \text{numRows} - 2$$

- 例如，当 `numRows = 3` 时，$T = 4$（下行 3 步，回升 1 步）。

- 当 `numRows = 4` 时，$T = 6$（下行 4 步，回升 2 步）。

### 2. 代码逻辑拆解

- **计算周期**：设置 $T = 2 \times \text{numRows} - 2$。如果 $T=0$（即 `numRows=1`），意味着不需要变换，直接返回原字符串。

- **模拟放置**：
  
  - 通过 `loc = i % T` 计算当前字符在周期内的位置。
  
  - **下行阶段**：如果 `loc < numRows`，说明当前字符正在向下走，直接放入 `matrix[loc]`。
  
  - **折返阶段**：如果 `loc >= numRows`，说明字符正在斜向上方走。此时它应该存放的行数是 `numRows - (loc - numRows) - 2`，简化后即为你代码中的 `numRows - loc - 2`。

- **合并结果**：最后将 `matrix` 中每一行的字符列表使用 `"".join()` 拼接，再整体合并成结果字符串。

### 3. 复杂度分析

- **时间复杂度**：$O(n)$
  
  我们只对字符串 $s$ 进行了一次遍历，最后合并字符串的时间也是 $O(n)$。

- **空间复杂度**：$O(n)$
  
  我们需要一个二维列表 `matrix` 来存储所有的字符，总空间与字符串长度成正比。