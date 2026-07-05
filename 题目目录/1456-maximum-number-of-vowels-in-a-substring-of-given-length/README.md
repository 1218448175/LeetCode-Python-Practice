## [1456. 定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

### 中等

给你一个字符串 `s` 和一个整数 `k`，请你返回长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母** 为（`a`、`e`、`i`、`o`、`u`）。

**示例 1：**
<pre><strong>输入：</strong>s = "abciiidef", k = 3
<strong>输出：</strong>3
<strong>解释：</strong>子字符串 "iii" 包含 3 个元音字母。
</pre>

**示例 2：**
<pre><strong>输入：</strong>s = "aeiou", k = 2
<strong>输出：</strong>2
<strong>解释：</strong>任意长度为 2 的子字符串都包含 2 个元音字母。
</pre>

**示例 3：**
<pre><strong>输入：</strong>s = "leetcode", k = 3
<strong>输出：</strong>2
<strong>解释：</strong>"lee"、"eet" 和 "ode" 都包含 2 个元音字母。
</pre>

---

## 题解：定长滑动窗口 + 提前终止优化

### 1. 问题分析

本题是**定长滑动窗口**的经典模板题。不同于变长窗口需要收缩左边界来满足条件，定长窗口的长度 `k` 是固定的，只需维护一个长度为 `k` 的窗口从左滑到右，在滑动过程中记录元音字母数量的最大值。

---

### 2. 核心思路：三步循环法

你的代码使用 `enumerate(s)` 枚举窗口右端点 `i`，在同一个循环中完成三个动作：

```python
ans = vowel = 0
for i, c in enumerate(s):       # 枚举窗口右端点 i
    # 1. 右端点进入窗口
    if c in "aeiou":
        vowel += 1

    left = i - k + 1             # 计算窗口左端点
    if left < 0:                 # 窗口长度不足 k → 继续扩展
        continue

    # 2. 更新答案
    ans = max(ans, vowel)

    # 3. 左端点离开窗口（为下一次滑动做准备）
    if s[left] in "aeiou":
        vowel -= 1
```

**窗口滑动示意图（s = "abciiidef", k = 3）：**

| 步 | 窗口 (i) | 左端点 | 窗口内容 | 元音数 | 动作 |
|----|----------|--------|----------|--------|------|
| 0 | i=0, 'a' | -2 (未形成) | — | vowel=1 (仅进入) | continue |
| 1 | i=1, 'b' | -1 (未形成) | — | vowel=1 (仅进入) | continue |
| 2 | i=2, 'c' | 0 | "abc" | vowel=1, ans=1 | 移除 s[0]='a' → vowel=0 |
| 3 | i=3, 'i' | 1 | "bci" | vowel=1, ans=1 | 移除 s[1]='b' → vowel=1 |
| 4 | i=4, 'i' | 2 | "cii" | vowel=2, ans=2 | 移除 s[2]='c' → vowel=2 |
| 5 | i=5, 'i' | 3 | "iii" | vowel=3, ans=3 | 移除 s[3]='i' → vowel=2 |
| 6 | i=6, 'd' | 4 | "iid" | vowel=2, ans=3 | 移除 s[4]='i' → vowel=1 |
| 7 | i=7, 'e' | 5 | "ide" | vowel=2, ans=3 | 移除 s[5]='i' → vowel=1 |
| 8 | i=8, 'f' | 6 | "def" | vowel=2, ans=3 | 移除 s[6]='d' → vowel=1 |

最终答案：**3**（子串 "iii" 包含 3 个元音）。

---

### 3. 亮点分析

#### 3.1 统一的单循环结构

传统滑动窗口常将"初始化第一个窗口"单独写一个循环，而你的代码将所有逻辑统一在一个 `for` 循环中：

- **未形成窗口（left < 0）**：只让右端点进入窗口，不更新答案，不移除左端点 → `continue`
- **形成窗口后**：进入 → 更新答案 → 移除左端点

这种写法避免了第一个窗口的二次循环，代码更紧凑。

#### 3.2 提前终止（ans == k 剪枝）

```python
ans = max(ans, vowel)
if ans == k:   # 答案已经等于理论最大值
    break      # 无需再循环
```

长度为 `k` 的子串最多包含 `k` 个元音字母，所以 `ans == k` 时即可提前终止。对于全元音字符串（如 `s = "aeiou"`），可以在窗口刚形成时就退出，避免后续无用遍历。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。每个字符被"进入窗口"和"离开窗口"各处理一次，单次遍历完成。提前终止优化在最佳情况下可减少遍历次数（但不影响大 O）。
- **空间复杂度**：$O(1)$，仅使用 `ans`、`vowel`、`left` 三个额外变量。

---

### 延伸思考

- 本题是定长滑动窗口的入门模板，核心在于用**单一循环**处理进入/更新/移除三步，避免额外维护初始窗口的代码。
- 变长滑动窗口（如 [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)）则需要动态收缩左边界以满足窗口内的约束条件，两者的代码结构有显著差异。
- Python 的 `c in "aeiou"` 是 $O(1)$ 操作（查找 5 个字符），比 `set` 更简洁高效。
