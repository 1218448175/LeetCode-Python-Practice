<h2><a href="https://leetcode.cn/problems/majority-element">169. 多数元素</a></h2>
<h3>简单</h3>
<hr>
<p>给定一个大小为 <code>n</code><em> </em>的数组 <code>nums</code> ，返回其中的多数元素。多数元素是指在数组中出现次数 <strong>大于</strong> <code>⌊ n/2 ⌋</code> 的元素。</p>
<p>你可以假设数组是非空的，并且给定的数组总是存在多数元素。</p>
<p> </p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [3,2,3]
<strong>输出：</strong>3</pre>

---

### 解题思路

当众数的个数大于 n/2 时，对数组中的元素进行比较，相异相消后，留下来的必然是众数

### 算法步骤

- 维护`num`，`count`，初始化分别为`-1`，`0`，表示候选众数和元素个数

- 遍历数组`num`，对于元素`x`，若`count`为`0`，则先将`num`赋值为`x`：
  
  - 如果`x `与`num`相同，则`count `++
  
  - 否则`count`--

- 遍历完成后，`num`即为众数

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，仅维护常数个变量。