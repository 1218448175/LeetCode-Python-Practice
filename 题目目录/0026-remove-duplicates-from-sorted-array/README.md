<h2><a href="https://leetcode.cn/problems/merge-sorted-array">26. 删除有序数组中的重复项</a></h2>
<h3>简单</h3>
<hr>
<p>给你一个 <strong>非严格递增排列</strong> 的数组 <code>nums</code> ，请你<strong><a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a></strong> 删除重复出现的元素，使每个元素 <strong>只出现一次</strong> ，返回删除后数组的新长度。元素的 <strong>相对顺序</strong> 应该保持 <strong>一致</strong> 。然后返回 <code>nums</code> 中唯一元素的个数。</p>
<p>考虑 <code>nums</code> 的唯一元素的数量为 <code>k</code>。去重后，返回唯一元素的数量 <code>k</code>。</p>
<p><code>nums</code> 的前 <code>k</code> 个元素应包含 <strong>排序后</strong> 的唯一数字。下标 <code>k - 1</code> 之后的剩余元素可以忽略。</p>

---

### 解题思路https://leetcode.cn/problems/remove-duplicates-from-sorted-array

1. **双指针法**：设置两个双指针，`left`, `right`分别指向某个重复元素串的开头和当前处理 的元素位置
2. **比较与替换**：比较`right`和`left-1`， 不相同则说明`right`为不重复元素，将`left`替换为`right`

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，直接在原数组上操作。