<h2><a href="https://leetcode.cn/problems/maximum-subarray">53. 最大子数组和</a></h2>
<h3>中等</h3>
<hr>
<p>给你一个整数数组 <code>nums</code> ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>
<p><strong>子数组</strong> 是数组中的一个连续部分。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>输出：</strong>6
<strong>解释：</strong>连续子数组 [4,-1,2,1] 的和最大，为 6 。
</pre>

---

### 解题思路

基于动态规划（Kadane 算法），维护「以当前位置结尾的最大子数组和」与「全局最大子数组和」两个状态，逐元素更新即可。

### 算法步骤

- 初始化 `tail = nums[0]`，表示以当前位置结尾的最大子数组和；`middle = nums[0]`，表示全局最大子数组和。

- 从第二个元素开始遍历数组，对每个 `num`：
  
  - 先用当前 `tail` 更新全局最优：`middle = max(tail, middle)`
  
  - 再更新以当前位置结尾的最大和：`tail = max(num, tail + num)`（要么单独成段，要么接在前一段后面）

- 遍历结束后返回 `max(middle, tail)`。

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，仅维护常数个变量。
