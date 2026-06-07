class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[_] + nums2[0], _, 0) for _ in range(min(len(nums1), k))]
        ans = []
        for _ in range(k):
            cnt, i, j = heappop(heap)
            ans.append((nums1[i], nums2[j]))
            if j < len(nums2) - 1:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
        