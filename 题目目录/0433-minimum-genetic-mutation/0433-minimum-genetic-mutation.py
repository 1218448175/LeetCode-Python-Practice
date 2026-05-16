class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        bank = set(bank)
        if endGene not in bank:
            return -1
        q = deque([(startGene, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == endGene:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
        