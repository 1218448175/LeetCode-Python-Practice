## [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

### 中等

请你设计并实现一个满足  [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

**示例：**

<pre><strong>输入</strong>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>输出</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>解释</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
</pre>

---

## 题解：哈希表 + 双向链表的完美结合

### 1. 核心思路：为什么要用这两种结构？

LRU (Least Recently Used) 缓存的核心要求是：**查询 $O(1)$** 且 **更新 $O(1)$**。

- **哈希表 (Hash Table)**：负责 **“快找”**。通过 `key` 可以在 $O(1)$ 时间内定位到数据在内存中的位置。

- **双向链表 (Doubly Linked List)**：负责 **“快排”**。链表可以记录访问的时序。最近访问的移到头部，最久未访问的留在尾部。双向结构使得删除任意节点的操作达到 $O(1)$。

---

### 2. 执行逻辑的详细拆解

#### A. 节点设计与初始化

你定义了 `DLinkNode` 类，包含 `key` 和 `value`。

- **为什么要存 key？** 当缓存满时，我们需要通过链表尾节点找到 `key`，从而在哈希表中删除对应的条目。

- **哨兵节点**：初始化时创建了 `head` 和 `tail` 两个虚拟节点。这是一种非常优雅的技巧，它可以保证在添加或删除节点时，**无需判断节点是否为空**，极大简化了边界逻辑。

#### B. 获取数据 (`get`)

1. 如果在 `cache` 中找不到，返回 `-1`。

2. 如果找到了，说明该节点被“激活”了。调用 `moveToHead(node)`：
   
   - 先从当前位置删除。
   
   - 插入到 `head` 之后。

#### C. 写入数据 (`put`)

1. **Key 不存在**：
   
   - 创建新节点并存入哈希表。
   
   - 将新节点添加到链表头部。
   
   - 如果超过 `capacity`，调用 `removeTail()` 删除最久未使用的节点，并同步从哈希表中 `pop` 掉该键。

2. **Key 已存在**：
   
   - 更新节点的值。
   
   - 调用 `moveToHead(node)` 将其移至头部，代表最新访问。

---

### 3. 关键函数逻辑分析

- **`addToHead(node)`**：典型的“穿针引线”。先修改新节点的 `prev/next`，再修改原链表节点的指向，防止断链。

- **`removeNode(node)`**：由于是双向链表，可以直接通过 `node.prev.next = node.next` 这种方式将自己从链中“抹除”。

- **`moveToHead` 和 `removeTail`**：这两个高层函数封装了底层逻辑，使 `get` 和 `put` 的代码意图非常清晰。

---

### 4. 复杂度分析

- **时间复杂度**：
  
  - `get(key)`：$O(1)$。哈希表查找 $O(1)$，链表移动 $O(1)$。
  
  - `put(key, value)`：$O(1)$。哈希表插入/更新 $O(1)$，链表操作 $O(1)$。

- **空间复杂度**：$O(capacity)$。哈希表和双向链表最多各存储 `capacity` 个元素。

---

### 5. 代码回顾

```pyt
class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 虚拟头尾节点，简化逻辑
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node) # 每次访问都移到头部
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 淘汰策略：删除最久未使用的尾部节点
                removed_node = self.removeTail()
                self.cache.pop(removed_node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
```