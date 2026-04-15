<h2><a href="https://leetcode.cn/problems/merge-sorted-array">27. 移除元素</a></h2>
<h3>简单</h3>
<hr>
<p>给你一个数组 <code>nums</code><em> </em>和一个值 <code>val</code>，你需要 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong> 移除所有数值等于 <code>val</code><em> </em>的元素。元素的顺序可能发生改变。然后返回 <code>nums</code> 中与 <code>val</code> 不同的元素的数量。</p>
<p>假设 <code>nums</code> 中不等于 <code>val</code> 的元素数量为 <code>k</code>，要通过此题，您需要执行以下操作：</p>
<ul>
    <li>更改 <code>nums</code> 数组，使 <code>nums</code> 的前 <code>k</code> 个元素包含不等于 <code>val</code> 的元素。<code>nums</code> 的其余元素和 <code>nums</code> 的大小并不重要。</li>
    <li>返回 <code>k</code>。</li>
</ul>

---

### 解题思路

1. **双指针法（优化）**：传统的双指针法（从前往后），在遇到只有`nums[0]`为`val`的情况时，需要将索引`1`到`n-1`的元素全部向前移动一位，浪费了时间。将`r`指针的起始位置定在数组末尾，只在`l`指针指向的元素为`val`时移动元素。
2. **比较与放置**：设置两个指针，`l, r`分别指向 `nums` 的当前处理元素、`nums` 的替换元素。

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，直接在原数组上操作。