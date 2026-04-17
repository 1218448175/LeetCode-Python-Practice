<h2><a href="https://leetcode.cn/problems/rotate-array">189. 轮转数组</a></h2>
<h3>中等</h3>
<hr>
<p>给定一个整数数组 <code>nums</code>，将数组中的元素向右轮转 <code>k</code><em> </em>个位置，其中 <code>k</code><em> </em>是非负数。</p>

<p> </p>
<p><strong>示例 1:</strong></p>
<pre><strong>输入:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>输出:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>解释:</strong>
向右轮转 1 步: <code>[7,1,2,3,4,5,6]</code>
向右轮转 2 步: <code>[6,7,1,2,3,4,5]
</code>向右轮转 3 步: <code>[5,6,7,1,2,3,4]</code>
</pre>

---

### 解题思路

直接使用坐标映射，将坐标为`i`的元素映射到坐标为`(i+k) mod n`的位置

### 算法步骤

使用Python内置的列表分割方法，`nums[:] = nums[-k:] + nums[:-k]`

注意，k要先模n

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，原地操作数组。