<h2><a href="https://leetcode.cn/problems/merge-sorted-array">80. 删除有序数组中的重复项 II</a></h2>
<h3>简单</h3>
<hr>
<p>给你一个有序数组 <code>nums</code> ，请你<strong><a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a></strong> 删除重复出现的元素，使得出现次数超过两次的元素<strong>只出现两次</strong> ，返回删除后数组的新长度。</p>
<p>不要使用额外的数组空间，你必须在 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组 </strong>并在使用 O(1) 额外空间的条件下完成。</p>

---

### 解题思路

1. **双指针法**：与[0026-移除有序数组中的重复项](./0026-remove-duplicates-from-sorted-array) 类似, 只不过需要考虑的是前面的第二个元素，设置两个双指针，`left`, `right`分别指向某个重复元素串的开头和当前处理 的元素位置
2. **比较与替换**：比较`right`和`left-2`， 不相同则说明`right`为不重复元素，将`left`替换为`right`
3. **边界处理**：当数组长度n<=2时，直接返回n即可。

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，直接在原数组上操作。