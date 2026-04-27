<h2><a href="https://leetcode.cn/problems/h-index">274. H 指数</a></h2>
<h3>中等</h3>
<hr>
<p>给你一个整数数组 <code>citations</code> ，其中 <code>citations[i]</code> 表示研究者的第 <code>i</code> 篇论文被引用的次数。计算并返回该研究者的 <strong><code>h</code><em> </em>指数</strong>。</p>
<p>根据维基百科上 <a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：<code>h</code> 代表“高引用次数” ，一名科研人员的 <code>h</code><strong> 指数 </strong>是指他（她）至少发表了 <code>h</code> 篇论文，并且 <strong>至少 </strong>有 <code>h</code> 篇论文被引用次数大于等于 <code>h</code> 。如果 <code>h</code><em> </em>有多种可能的值，<strong><code>h</code> 指数 </strong>是其中最大的那个。</p>
<p> </p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong><code>citations = [3,0,6,1,5]</code>
<strong>输出：</strong>3 
<strong>解释：</strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 <code>3, 0, 6, 1, 5</code> 次。
     由于研究者有 <code>3 </code>篇论文每篇 <strong>至少 </strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用 <strong>不多于</strong> <code>3</code> 次，所以她的 <em>h </em>指数是 <code>3</code>。</pre>

---

##### 题解：基于计数排序的 H 指数计算

### 1. 核心思路

H 指数的定义是：有 $h$ 篇论文至少被引用了 $h$ 次。

由于一名研究者总共有 $n$ 篇论文，那么其 $h$ 指数**最高不会超过 $n$**。即便某篇论文被引用了 1000 次，如果总共只有 5 篇论文，那这 1000 次也只能按 5 次来计算贡献。

利用这个特性，我们可以通过统计每个引用次数出现的频率来快速求解。

### 2. 算法步骤

1. **初始化计数器**：
   
   创建一个长度为 $n+1$ 的数组 `counter`。`counter[i]` 表示引用次数**等于** $i$ 的论文篇数。对于引用次数大于 $n$ 的论文，我们统一将其计入 `counter[n]`。

2. **填充计数器**：
   
   遍历输入的 `citations` 数组：
   
   - 如果引用次数 $c \ge n$，则 `counter[n] += 1`。
   
   - 否则，`counter[c] += 1`。

3. **逆向累加找 $h$**：
   
   我们需要找到最大的 $h$，使得“引用次数 $\ge h$ 的论文总数 $\ge h$”。
   
   - 我们从 $i = n$ 开始逆向遍历 `counter` 数组。
   
   - 使用变量 `total` 记录当前“引用次数**至少**为 $i$”的论文总篇数。
   
   - 每走一步，`total += counter[i]`。
   
   - **判定条件**：当我们第一次遇到 `total >= i` 时，当前的 $i$ 就是我们要找的最大 $h$ 指数。

---

### 3. 示例图解

假设 `citations = [3, 0, 6, 1, 5]`，此时 $n=5$。

- **步骤 1 & 2（计数）**：
  
  - 3 -> `counter[3]=1`
  
  - 0 -> `counter[0]=1`
  
  - 6 -> `counter[5]=1`（因为 6 > 5）
  
  - 1 -> `counter[1]=1`
  
  - 5 -> `counter[5]=2`（累加后）
  
  - 最终 `counter = [1, 1, 0, 1, 0, 2]`（对应索引 0-5）

- **步骤 3（逆向累加）**：
  
  - $i=5$: `total = 2`。$2 < 5$，继续。
  
  - $i=4$: `total = 2 + 0 = 2`。$2 < 4$，继续。
  
  - $i=3$: `total = 2 + 0 + 1 = 3`。**$3 \ge 3$！满足条件，返回 3。**

---

### 4. 复杂度分析

- **时间复杂度：$O(n)$**
  
  - 遍历一遍 `citations` 数组进行计数：$O(n)$。
  
  - 遍历一遍 `counter` 数组寻找结果：$O(n)$。
  
  - 总时间为 $O(n)$。

- **空间复杂度：$O(n)$**
  
  - 需要一个长度为 $n+1$ 的额外数组来存储计数信息。