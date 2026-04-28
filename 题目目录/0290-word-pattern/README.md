## [290. 单词规律](https://leetcode.cn/problems/word-pattern/)

### 简单

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循** 指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。具体来说：

- `pattern` 中的每个字母都 **恰好** 映射到 `s` 中的一个唯一单词。
- `s` 中的每个唯一单词都 **恰好** 映射到 `pattern` 中的一个字母。
- 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

**示例1:**

<pre><strong>输入:</strong> pattern = <code>"abba"</code>, s = <code>"dog cat cat dog"</code>
<strong>输出:</strong> true</pre>

---

## 题解：哈希字典与唯一单词集合的双向映射策略

### 1. 核心思路：字符与单词的“双向连接”

本题要求判断规律 `pattern` 与字符串 `s` 是否满足双射（Bijection）关系。其核心逻辑与“同构字符串”高度一致，但操作对象从字符扩展到了单词。

- **映射约束**：
  
  1. `pattern` 中的每个字母必须唯一对应 `s` 中的一个单词。
  
  2. `s` 中的每个单词必须唯一对应 `pattern` 中的一个字母。

- **数据结构组合**：使用一个字典 `s_dict` 存储 `字母 -> 单词` 的正向映射，同时使用一个集合 `word_set` 确保不同字母不会映射到同一个单词上。

---

### 2. 执行逻辑的详细拆解

#### A. 长度前置检查

代码首先通过 `len(s_list) != len(pattern)` 进行拦截。如果规律的长度与单词的数量不一致，映射关系必然无法建立，直接返回 `False`。

#### B. 映射逻辑与冲突判定

遍历 `pattern`，对于每一个字母 `a` 和对应的单词 `s_list[i]`：

1. **场景 1：已存在映射关系**
   
   - 如果 `a` 已在字典中，检查记录的单词是否与当前单词相同（`word == s_list[i]`）。如果不匹配，则说明规律被打破。

2. **场景 2：尚未建立映射**
   
   - 如果 `a` 不在字典中，需进一步核对当前单词是否已被其他字母“占坑”（`s_list[i] not in word_set`）。
   
   - **合法则记录**：如果单词是全新的，则在字典中建立映射，并将单词加入集合。
   
   - **不合法则跳出**：如果单词已被占用，则违反了唯一性，逻辑失败。

#### C. 异常逻辑捕获

代码通过条件判断 `(word is not None and word == s_list[i]) or (word is None and s_list[i] not in word_set)` 精准地区分了合法路径与非法路径。

---

### 3. 逻辑亮点：结构化判定

你的代码逻辑中，`if...else` 的分支设计覆盖了映射关系中可能出现的几种冲突：

- **一码对多词**：同一个字母指向了不同的单词。

- **多码对一词**：不同的字母试图指向同一个已有的单词。
  
  这种双层保护确保了“双向连接”的严格匹配。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N + M)$。其中 $N$ 是 `pattern` 的长度，$M$ 是字符串 `s` 的长度。主要的开销在于 `split(' ')` 分词操作以及单次线性扫描。

- **空间复杂度**：$O(K)$。$K$ 是 `pattern` 中唯一字母的数量或 `s` 中唯一单词的数量。哈希表和集合存储了这些映射关系，空间消耗与唯一元素的规模成正比。

---

### 代码回顾

Python

```
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(s_list) != len(pattern):
            return False

        s_dict = {}     # 正向映射：字母 -> 单词
        word_set = set() # 逆向去重：单词集合

        for i in range(len(pattern)):
            a = pattern[i]
            word = s_dict.get(a)

            # 判断逻辑：如果已有映射且匹配，或者是新字母且单词未被占用
            if (word is not None and word == s_list[i]) or (word is None and s_list[i] not in word_set):
                if word is None: # 建立新映射
                    word_set.add(s_list[i])
                    s_dict[a] = s_list[i]
            else:
                # 任何不满足上述条件的情况即为不遵循规律
                return False

        return True
```