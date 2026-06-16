## [139. 单词拆分](https://leetcode.cn/problems/word-break/)

### 中等

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

**注意：** 不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

<p><strong>示例 1:</strong></p>
<pre><strong>输入:</strong> s = "leetcode", wordDict = ["leet", "code"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
</pre>

<p><strong>示例 2:</strong></p>
<pre><strong>输入:</strong> s = "applepenapple", wordDict = ["apple", "pen"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
</pre>

<p><strong>示例 3:</strong></p>
<pre><strong>输入:</strong> s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
<strong>输出:</strong> false
</pre>

---

## 题解：动态规划 — 前缀匹配 + 剪枝优化

### 1. 核心思路：前缀能否被拆分

这道题是字符串动态规划的经典问题。定义 `f[i]` 表示字符串 `s[0:i]`（前 i 个字符组成的前缀）能否被字典中的单词拆分。

状态转移思路：

- 对于每个位置 `i`，向前扫描位置 `j`（`j < i`）
- 如果 `s[0:j]` 可拆分（`f[j] == True`），且 `s[j:i]` 是字典中的单词，则 `s[0:i]` 也可拆分

由此推导出状态转移方程：

$$f[i] = \bigvee_{j < i} \left( f[j] \land s[j:i] \in \text{wordDict} \right)$$

其中 $f[0] = \text{True}$，表示空字符串可以被拆分。

---

### 2. 剪枝优化 — max_len 限制内层循环

朴素 DP 的内层 `j` 需要遍历 `[0, i-1]`，总复杂度为 $O(n^2)$。本题解引入 **max_len 剪枝**：

- 记录字典中最长单词的长度 `max_len`
- 内层 `j` 只需从 `i-1` 遍历到 `max(i - max_len - 1, -1)`
- 因为 `s[j:i]` 的长度超过 `max_len` 时，不可能匹配任何字典单词

这一优化在字典单词较短时将复杂度从 $O(n^2)$ 降到近似 $O(n \cdot L)$，其中 $L$ 为最大单词长度（本题 $L \le 20$）。

---

### 3. 变量设计与迭代推演

| 变量 | 含义 | 初始值 |
|------|------|--------|
| `max_len` | 字典中最长单词的长度，用于剪枝 | `max(map(len, wordDict))` |
| `words` | 字典的集合形式，O(1) 查询 | `set(wordDict)` |
| `f` | DP 数组，`f[i]` 表示 `s[:i]` 是否可拆分 | `[True] + [False] * n` |

以 `s = "leetcode", wordDict = ["leet", "code"]` 为例的推演过程：

| i | s[0:i] | j 扫描范围 | 匹配情况 | f[i] |
|---|--------|-----------|---------|------|
| 0 | ""     | -         | 空串默认 | True |
| 1 | "l"    | [0]       | "l" 不在字典 | False |
| 2 | "le"   | [1,0]     | 均不匹配 | False |
| 3 | "lee"  | [2,1,0]   | 均不匹配 | False |
| 4 | "leet" | [3,2,1,0] | j=0 时 "leet" 在字典 | **True** |
| 5 | "leetc" | [4,3,2,1] | 均不匹配 | False |
| 6 | "leetco" | [5,4,3,2] | 均不匹配 | False |
| 7 | "leetcod" | [6,5,4,3] | 均不匹配 | False |
| 8 | "leetcode" | [7,6,5,4] | j=4 时 "code" 在字典且 f[4]=True | **True** |

最终返回 `f[8] = True`。

---

### 4. 与爬楼梯（70 题）和打家劫舍（198 题）的对比

三道题都使用一维动态规划，但递推结构各不相同：

| 对比维度 | 70. 爬楼梯 | 198. 打家劫舍 | 139. 单词拆分 |
|---------|-----------|-------------|-------------|
| 递推公式 | $f(i) = f(i-1) + f(i-2)$ | $dp[i] = \max(dp[i-2] + nums[i],\ dp[i-1])$ | $f[i] = \bigvee_{j} (f[j] \land s[j:i] \in \text{dict})$ |
| 决策类型 | 确定性累加（路径数求和） | 最优化选择（偷或不偷取最大） | 存在性判断（是否存在合法拆分） |
| 内层结构 | 固定两个前驱 | 固定两个前驱 | 可变范围扫描（依赖 max_len 剪枝） |
| 空间优化 | $O(1)$ 双变量 | $O(1)$ 双变量 | $O(n)$（依赖所有前缀状态，无法滚动） |

爬楼梯和打家劫舍都可以用双变量滚动到 $O(1)$ 空间，但单词拆分需要访问任意 `f[j]`，无法做同样的空间优化。

---

### 5. 复杂度分析

- **时间复杂度**：$O(n \cdot L)$，其中 $n$ 为字符串长度，$L = \min(n, \text{max\_len})$ 为内层循环的最大次数。本题 $L \le 20$，近似线性。

- **空间复杂度**：$O(n + m)$，DP 数组占用 $O(n)$，字典集合占用 $O(m)$，其中 $m$ 为字典单词数。
