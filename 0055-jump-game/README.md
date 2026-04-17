<h2><a href="https://leetcode.cn/problems/jump-game">55. 跳跃游戏</a></h2>
<h3>中等</h3>
<hr>
<p>给你一个非负整数数组&nbsp;<code>nums</code> ，你最初位于数组的 <strong>第一个下标</strong> 。数组中的每个元素代表你在该位置可以跳跃的最大长度。</p>
<p>判断你是否能够到达最后一个下标，如果可以，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>
<p>&nbsp;</p>
<p><strong>示例&nbsp;1：</strong></p>
<pre><strong>输入：</strong>nums = [2,3,1,1,4]
<strong>输出：</strong>true
<strong>解释：</strong>可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
</pre>

---

### 解题思路

使用贪心策略，对于每一个可达的位置`i`，它将贡献一个最远可达下标`i+nums[i]`，只需维护一个最远可达下标即可。

### 算法步骤

- 初始化，最远可达下标`max_len`为`0`

- 从`0`开始遍历数组，对于下标为`i`的元素，如果：
  
  - `max_len`大于`i`，则更新`max_len=max(max_len,i+nums[i])`
  
  - `max_len`小于`i`，则`break`

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)