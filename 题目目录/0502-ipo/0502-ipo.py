class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        n = len(profits)
        curr = 0
        heap = []
        arr = [(profits[i], capital[i]) for i in range(n)]
        arr.sort(key = lambda x: x[1])

        for i in range(k):
            while curr < n and arr[curr][1] <= w:
                heapq.heappush(heap, -arr[curr][0])
                curr += 1

            if heap:
                w -= heapq.heappop(heap)
            else:
                break

        return w
        