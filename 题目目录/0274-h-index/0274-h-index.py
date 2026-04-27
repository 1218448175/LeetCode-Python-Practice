class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0 for _ in range(n+1)]
        total = 0
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        
        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
        return 0

        