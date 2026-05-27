class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        def dfs(r: int, c: int, length: int) -> 'Node':
            # 1. 递归基准：最小单元
            if length == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)
            
            # 2. 递归获取四个子区域
            nxt = length // 2
            tl = dfs(r, c, nxt)
            tr = dfs(r, c + nxt, nxt)
            bl = dfs(r + nxt, c, nxt)
            br = dfs(r + nxt, c + nxt, nxt)
            
            # 3. 合并逻辑：如果四个子节点都是叶子且值相同，则合并
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and 
                tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)
            
            # 4. 如果不能合并，则返回非叶子节点
            return Node(True, False, tl, tr, bl, br)
            
        return dfs(0, 0, n)