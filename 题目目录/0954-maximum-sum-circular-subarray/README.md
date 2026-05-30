<h2><a href="https://leetcode.cn/problems/maximum-sum-circular-subarray">954. 环形子数组的最大和</a></h2>
<h3>中等</h3>
<hr>
<p>给定一个<strong>环形</strong>整数数组 <code>nums</code>，返回这个环的最大子数组和。</p>
<p>环形数组意味着数组的最后一个元素和第一个元素在概念上是相邻的。形式上，当 <code>0 &lt;= i &lt; nums.length - 1</code> 时 <code>nums[i]</code> 和 <code>nums[i + 1]</code> 相邻，当 <code>i == nums.length - 1</code> 时 <code>nums[i]</code> 和 <code>nums[0]</code> 相邻。</p>
<p><strong>子数组</strong> 最多只能包含固定缓冲区 <code>nums</code> 中的每个元素一次。形式上，对于子数组 <code>nums[i], nums[i + 1], ..., nums[j]</code>，不存在 <code>i &lt;= k1, k2 &lt;= j</code> 满足 <code>k1 % nums.length == k2 % nums.length</code>。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [1,-2,3,-2]
<strong>输出：</strong>3
<strong>解释：</strong>从子数组 [3,-2] 得到最大和 3
</pre>

---

### 解题思路

环形子数组的最大和只有两种情况：要么是不跨越首尾边界的普通最大子数组和，要么是「整个数组总和减去最小子数组和」（即把最小子数组从环中挖掉，剩余部分首尾相连）。同时维护 Kadane 的最大/最小子数组和即可。

### 算法步骤

- 初始化 `max_f = 0`、`max_s = -inf` 维护最大子数组；`min_f = 0`、`min_s = 0` 维护最小子数组。

- 遍历每个 `num`：
  
  - 最大子数组：`max_f = max(max_f, 0) + num`，`max_s = max(max_s, max_f)`
  
  - 最小子数组：`min_f = min(min_f, 0) + num`，`min_s = min(min_s, min_f)`

- 若 `max_s < 0`，说明数组全为负数，直接返回 `max_s`。

- 否则返回 `max(max_s, sum(nums) - min_s)`，即在普通最大子数组和与环形最大子数组和中取较大值。

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，仅维护常数个变量。
