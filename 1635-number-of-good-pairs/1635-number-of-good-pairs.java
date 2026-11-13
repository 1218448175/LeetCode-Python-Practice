class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        int goodPairsCount = 0;
        for (int num: nums) {
            int count = countMap.getOrDefault(num, 0);
            goodPairsCount += count;
            countMap.put(num, count + 1);
        }
        return goodPairsCount;
    }
}