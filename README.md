# LeetCode-Python-Practice

记录leetcode刷题记录

## 🎯 精选题解 (Highly Recommended)

这里记录了我对核心高频面试题（top150）的解题和优化思路

### 🔗 数组与字符串

* [0088-合并两个有序数组](./题目目录/0088-merge-sorted-array) —— 重点：逆向双指针优化空间至 O(1)
* [0027-移除元素](./题目目录/0027-remove-element) —— 重点：双向双指针优化时间复杂度
* [0026-移除有序数组中的重复项](./题目目录/0026-remove-duplicates-from-sorted-array)
* [0080-移除有序数组中的重复项 II](./题目目录/0080-remove-duplicates-from-sorted-array-ii)
* [0169-多数元素](./题目目录/0169-majority-element) —— 重点：投票法（相异相消）优化空间至O(1)
* [0189-轮转数组](./题目目录/0169-majority-element)
* [0055-跳跃游戏](./题目目录/0055-jump-game)
* [0055-跳跃游戏 II](./题目目录/0055-jump-game-ii) —— 重点：贪心中的边界处理
* [0274-H 指数](./题目目录/0274-h-index) —— 重点：计数排序优化时间至O(n)
* [0380-O(1) 时间插入、删除和获取随机元素](./题目目录/0380-insert-delete-getrandom-o1) —— 重点：变长数组+HashMap
* [0238-除了自身以外数组的乘积](./题目目录/0238-product-of-array-except-self) —— 重点：动态构建右乘积列表优化空间为O(1)
* [0134-加油站](./题目目录/0134-gas-station)
* [0135-分发糖果](./题目目录/0135-candy) —— 重点：贪心算法实现 O(n) 一次遍历
* [0042-接雨水](./题目目录/0042-trapping-rain-water) —— 重点：双指针实现O(n)一次遍历
* [0013-罗马数字转整数](./题目目录/0013-roman-to-integer)
* [0012-整数转罗马数字](./题目目录/0012-integer-to-roman)
* [0058-最后一个单词的长度](./题目目录/0058-length-of-last-word)
* [0014-最长公共前缀](./题目目录/0014-longest-common-prefix)
* [0151-反转字符串中的单词](./题目目录/0151-reverse-words-in-a-string)
* [0006-Z 字形变换](./题目目录/0006-zigzag-conversion)
* [0028-找出字符串中第一个匹配项的下标](./题目目录/0028-find-the-index-of-the-first-occurrence-in-a-string) —— 重点：经典KMP算法
* [0068-文本左右对齐](./题目目录/0068-text-justification)

### 🔗 双指针

- [0125-验证回文串](./题目目录/0125-valid-palindrome)
- [0392-判断子序列](./题目目录/0392-is-subsequence)
- [0167-两数之和 II - 输入有序数组](./题目目录/0167-two-sum-ii-input-array-is-sorted)
- [0011-盛最多水的容器](./题目目录/0011-container-with-most-water)
- [0015-三数之和](./题目目录/0015-3sum)

### 🔗 滑动窗口

- [0209-长度最小的子数组](./题目目录/0209-minimum-size-subarray-sum)
- [0003-无重复字符的最长子串](./题目目录/0003-longest-substring-without-repeating-characters)
- [0030-串联所有单词的子串](./题目目录/0030-substring-with-concatenation-of-all-words) —— 重点：计数溢出监控策略
- [0076-最小覆盖子串](./题目目录/0076-minimum-window-substring)

### 🔗 矩阵

- [0036-有效的数独](./题目目录/0036-valid-sudoku)
- [0054-螺旋矩阵](./题目目录/0054-spiral-matrix) —— 重点：向量控制方向
- [0048-旋转矩阵](./题目目录/0048-rotate-image) —— 重点：矩阵分块处理
- [0073-矩阵置零](./题目目录/0048-rotate-image) —— 重点：首列复用与标志位
- [0289-生命游戏](./题目目录/0289-game-of-life) —— 重点：复合状态编码

### 🔗 哈希表

- [0383-赎金信](./题目目录/0383-ransom-note)
- [0205-同构字符串](./题目目录/0205-isomorphic-strings)
- [0290-单词规律](./题目目录/0290-word-pattern)
- [0242-有效的字母异位词](./题目目录/0242-valid-anagram)
- [0049-字母异位词分组](./题目目录/0049-group-anagrams)
- [0001-两数之和](./题目目录/0001-two-sum)
- [0201-快乐数](./题目目录/0202-happy-number) —— 重点：哈希表检测循环
- [0219-存在重复元素 II](./题目目录/0219-contains-duplicate-ii)
- [0128-最长连续序列](./题目目录/0128-longest-consecutive-sequence)
- [0056-合并区间](./题目目录/0056-merge-intervals)

### 🔗 区间

- [0228-汇总区间](./题目目录/0228-summary-ranges)
- [0056-合并区间](./题目目录/0056-merge-intervals)
- [0057-插入区间](./题目目录/0057-insert-interval)
- [0452-用最少数量的箭引爆气球](./题目目录/0452-minimum-number-of-arrows-to-burst-balloons)

### 🔗 栈

- [0020-有效的括号](./题目目录/0020-valid-parentheses)
- [0071-简化路径](./题目目录/0071-simplify-path)
- [0155-最小栈](./题目目录/0155-min-stack) —— 重点：使用辅助栈优化时间复杂度O(N)->O(1)
- [0150-逆波兰表达式求值](./题目目录/0150-evaluate-reverse-polish-notation) —— 重点：双栈法
- [0224-基本计算器](./题目目录/0224-basic-calculator) —— 重点：括号展开，避免双栈法的复杂逻辑

### 🔗 链表

- [0141-环形链表](./题目目录/0141-linked-list-cycle) —— 快慢指针法(Floy算法)优化空间至O(1)
- [0002-两数相加](./题目目录/0002-add-two-numbers)
- [0021-合并两个有序链表](./题目目录/0021-merge-two-sorted-lists)
- [0138-随机链表的复制](./题目目录/0138-copy-list-with-random-pointer) —— 重点：拆分链表优化空间至O(1)
- [0092-反转链表 II](./题目目录/0092-reverse-linked-list-ii)
- [0025-K 个一组翻转链表](./题目目录/0025-reverse-nodes-in-k-group)
- [0082-删除排序链表中的重复元素 II](./题目目录/0082-remove-duplicates-from-sorted-list-ii)
- [0061-翻转链表](./题目目录/0061-rotate-list)
- [0086-分隔链表](./题目目录/0086-partition-list)
- [0146-LRU缓存](./题目目录/0146-lru-cache)

### 🔗 二叉树

- [0104-二叉树的最大深度](./题目目录/0104-maximum-depth-of-binary-tree)
- [0100-相同的树](./题目目录/0100-same-tree)
- [0226-翻转二叉树](./题目目录/0226-invert-binary-tree)
- [0101-对称二叉树](./题目目录/0101-symmetric-tree)
- [0105-从前序与中序遍历序列构造二叉树](./题目目录/0105-construct-binary-tree-from-preorder-and-inorder-traversal) —— 重点：哈希表映射优化时间复杂度至O(1)
- [0106-从中序与后序遍历序列构造二叉树](./题目目录/0106-construct-binary-tree-from-inorder-and-postorder-traversal)
- [0117-填充每个节点的下一个右侧节点指针 II](./题目目录/0117-populating-next-right-pointers-in-each-node-ii)
- [0114-二叉树展开为链表](./题目目录/0114-flatten-binary-tree-to-linked-list)
- [0112-路径总和](./%E9%A2%98%E7%9B%AE%E7%9B%AE%E5%BD%95/0112-path-sum)
- [0129-求根节点到叶节点数字之和](./题目目录/0129-sum-root-to-leaf-numbers)
- [0124-二叉树中的最大路径和](./题目目录/0124-binary-tree-maximum-path-sum) —— 重点：后序 DFS，区分子树全局最优与可向上延伸的单链
- [0173-二叉搜索树迭代器](./题目目录/0173-binary-search-tree-iterator)
- [0222-完全二叉树的节点个数](./题目目录/0222-count-complete-tree-nodes) —— 重点：左右边界等高则满树 2^h-1，否则分治O(log²n)
- [0236-二叉树的最近公共祖先](./题目目录/0236-lowest-common-ancestor-of-a-binary-tree) —— 重点：后序 DFS，左右子树各找到一个目标则当前根为 LCA

### 🔗 二叉树的层次遍历

- [0199-二叉树的右视图](./题目目录/0199-binary-tree-right-side-view) —— 重点：先右后左 DFS，每层首次访问的节点即该层最右可见；亦可用 BFS 取每层最后一个
- [0637-二叉树的层平均值](./题目目录/0637-average-of-levels-in-binary-tree)
- [0102-二叉树的层序遍历](./题目目录/0102-binary-tree-level-order-traversal)
- [0103-二叉树的锯齿形层序遍历](./题目目录/0103-binary-tree-zigzag-level-order-traversal)

### 🔗 二叉树搜索树

- [0530-二叉搜索树的最小绝对差](./题目目录/0530-minimum-absolute-difference-in-bst)
- [0230-二叉搜索树中第 K 小的元素](./题目目录/0230-kth-smallest-element-in-a-bst)
- [0098-验证二叉搜索树](./题目目录/0098-validate-binary-search-tree)

### 🔗 图

- [0200-岛屿数量](./题目目录/0200-number-of-islands)
- [0207-课程表](./题目目录/0207-course-schedule) —— 重点：有向图环检测（三色 DFS）等价于拓扑排序可行性
- [0210-课程表 II](./题目目录/0210-course-schedule-ii) —— 重点：三色 DFS + 后序反转输出拓扑序；有环则返回空
- [0130-被围绕的区域](./题目目录/0130-surrounded-regions)
- [0133-克隆图](./题目目录/0133-clone-graph)
- [0399-除法求值](./题目目录/0399-evaluate-division) —— 重点：带权并查集维护变量间的除法关系

### 🔗 图的广度优先搜索

- [0909-蛇梯棋](./题目目录/0909-snakes-and-ladders) —— 重点：棋盘编号与锯齿坐标映射；掷骰+蛇梯构成隐式图，层序 BFS 求最短路
- [0433-最小基因变化](./题目目录/0433-minimum-genetic-mutation) —— 重点：单点突变生成邻居；`bank` 作合法节点集，BFS + 出队即删库去重
- [0127-单词接龙](./题目目录/0127-word-ladder) —— 重点：单词与通配模式建二分图，一次合法变换对应 2 条边；`dis[end] // 2 + 1` 为序列长度

### 🔗 字典树

- [0208-实现 Trie (前缀树)](./题目目录/0208-implement-trie-prefix-tree) —— 重点：`dict` 子节点 + `end` 标记；`find` 返回 0/1/2 统一支撑 `search` 与 `startsWith`
- [0211-添加与搜索单词 - 数据结构设计](./题目目录/0211-design-add-and-search-words-data-structure) —— 重点：Trie 插入不变；`search` 遇 `.` 对子节点 DFS 回溯匹配

### 🔗 动态规划

- [0121-买卖股票的最佳时机](./题目目录/0121-best-time-to-buy-and-sell-stock)
- [0122-买卖股票的最佳时机 II](./题目目录/0122-best-time-to-buy-and-sell-stock-ii) —— 重点：贪心优化空间至O(1)
- [0019-删除链表的倒数第 N 个结点](./题目目录/0019-remove-nth-node-from-end-of-list)

---

## 📅 全量索引 (Auto-generated by LeetHub)

<!---LeetCode Topics Start-->

# LeetCode Topics

## Array

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0027-remove-element](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0027-remove-element/)         | undefined  |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |

## Two Pointers

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0027-remove-element](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0027-remove-element/)         | undefined  |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |

## Sorting

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |
