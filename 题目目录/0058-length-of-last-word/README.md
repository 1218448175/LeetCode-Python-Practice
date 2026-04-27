## [58. 最后一个单词的长度](https://leetcode.cn/problems/length-of-last-word/)

### 简单

---

<p>给你一个字符串 <code>s</code>，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 <strong>最后一个</strong> 单词的长度。</p>
<p><strong>单词</strong> 是指仅由字母组成、不包含任何空格字符的最大子字符串。</p>
<p> </p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>s = "Hello World"
<strong>输出：</strong>5
<strong>解释：</strong>最后一个单词是“World”，长度为 5。
</pre>

---

### 解题思路

没什么好说的了，pyhton玩家是这样的。

### 复杂度分析

- 时间复杂度：O(n)，split()方法的开销。
- 空间复杂度：O(1)