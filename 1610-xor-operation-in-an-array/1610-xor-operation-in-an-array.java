class Solution {
    public int xorOperation(int n, int start) {
        List<Integer> nums = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            nums.add(start + 2 * i);
        }
        int res = nums.get(0);
        for (int j = 1; j < n; j++) {
            res = res ^ nums.get(j);
        }
        return res;
    }
}