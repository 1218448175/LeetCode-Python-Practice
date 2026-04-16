<h2><a href="https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions">121. 买卖股票的最佳时机</a></h2>
<h3>简单</h3>
<hr>
<p>给定一个数组 <code>prices</code> ，它的第 <code>i</code> 个元素 <code>prices[i]</code> 表示一支给定股票第 <code>i</code> 天的价格。</p>
<p>你只能选择 <strong>某一天</strong> 买入这只股票，并选择在 <strong>未来的某一个不同的日子</strong> 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>
<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 <code>0</code> 。</p>
<p> </p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>[7,1,5,3,6,4]
<strong>输出：</strong>5
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
</pre>

---

### 解题思路

基于动态规划和贪心策略，分情况（不购买股票，持有股票，股票售出三种状态）讨论并维护最大值

### 算法步骤

- 维护三个值，`dp0, dp1, dp2`，分别表示不购买股票，持有股票，股票售出三种状态。

- 遍历数组`prices`，第`i`天对应的三种状态动态转移方程如下：
  
  - 未购股票：`dp0 = dp0`
  
  - 持有股票：`dp1 = max(dp1, dp0 - prices[i])`
  
  - 卖出股票：`dp2 = max(dp2, dp1 + prices[i])`

- 遍历完成后，返回dp0与dp2的较大值。

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(1)，仅维护常数个变量。