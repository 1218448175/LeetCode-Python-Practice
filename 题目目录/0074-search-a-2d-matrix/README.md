<h2><a href="https://leetcode.cn/problems/search-a-2d-matrix">74. 搜索二维矩阵</a></h2>
<h3>中等</h3>
<hr>
<p>给你一个满足下述两条属性的 <code>m x n</code> 整数矩阵：</p>
<ul>
<li>每行中的整数从左到右按非严格递增顺序排列。</li>
<li>每行的第一个整数大于前一行的最后一个整数。</li>
</ul>
<p>给你一个整数 <code>target</code>，如果 <code>target</code> 在矩阵中，返回 <code>true</code>；否则，返回 <code>false</code>。</p>
<p>你必须设计一个时间复杂度为 <code>O(log(m * n))</code> 的算法。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>输出：</strong>false
</pre>

---

### 解题思路

将二维矩阵视为一个有序的一维数组，直接使用二分查找。矩阵按行展开后完全有序（每行从左到右递增，且下一行首元素大于上一行末元素），因此可以将一维索引映射到二维坐标：`row = mid // n`，`col = mid % n`，其中 `n` 为列数。

### 算法步骤

- 获取矩阵行数 `m` 和列数 `n`。
- 定义递归二分搜索函数 `binarySearch(l, r)`：
  - 若 `l > r`，搜索区间为空，返回 `False`。
  - 计算中点 `mid = (l + r) // 2`。
  - 将一维索引 `mid` 映射到二维坐标：`cur = matrix[mid // n][mid % n]`。
  - 若 `cur == target`，命中目标，返回 `True`。
  - 若 `cur < target`，目标在右半区，递归搜索 `[mid + 1, r]`。
  - 若 `cur > target`，目标在左半区，递归搜索 `[l, mid - 1]`。
- 调用 `binarySearch(0, m * n - 1)` 返回结果。

### 复杂度分析

- 时间复杂度：O(log(m * n))，将 m×n 个元素视为一个有序数组进行二分查找。
- 空间复杂度：O(log(m * n))，递归调用栈深度为二分查找的递归深度。
