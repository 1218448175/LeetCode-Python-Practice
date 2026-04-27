<h2><a href="https://leetcode.cn/problems/jump-game-ii">45. 跳跃游戏 II</a></h2>
<h3>中等</h3>
<hr>
<p>给定一个长度为 <code>n</code> 的 <strong>0 索引</strong>整数数组 <code>nums</code>。初始位置在下标 0。</p>
<p>每个元素 <code>nums[i]</code> 表示从索引 <code>i</code> 向后跳转的最大长度。换句话说，如果你在索引&nbsp;<code>i</code>&nbsp;处，你可以跳转到任意 <code>(i + j)</code> 处：</p>
<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code>&nbsp;且</li>
	<li><code>i + j &lt; n</code></li>
</ul> 
<p>返回到达&nbsp;<code>n - 1</code>&nbsp;的最小跳跃次数。测试用例保证可以到达 <code>n - 1</code>。</p>
<p>&nbsp;</p>
<p><strong>示例 1:</strong></p>
<pre><strong>输入:</strong> nums = [2,3,1,1,4]
<strong>输出:</strong> 2
<strong>解释:</strong> 跳到最后一个位置的最小跳跃数是 <code>2</code>。
&nbsp;    从下标为 0 跳到下标为 1 的位置，跳&nbsp;<code>1</code>&nbsp;步，然后跳&nbsp;<code>3</code>&nbsp;步到达数组的最后一个位置。
</pre>

---

### 解题思路

维护三个变量，`max_len, step, end`，分别表示：当前最远可达的下标、当前移动步数、当前所在位置的最远可达下标。

量化表示（对于下标`i`的元素）：

`max_len`：`max([x + nums[x] for x in range(i)])`

`end`：`i+nums[i]`

当`i`遍历到`end`时，说明该移动一次，否则上一步的最大可达下标将小于`i`

注意：`i`只需要遍历到 `n-1`，因为遍历到`n`会多出一步

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)