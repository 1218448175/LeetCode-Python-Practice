class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int n = arr.length;
        int cnt = 0;
        
        // i 从 0 到 n-3
        for (int i = 0; i < n; i++) {
            // j 从 i + 1 开始，天然满足 i < j
            for (int j = i + 1; j < n; j++) {
                // 剪枝 1：如果不满足 |arr[i] - arr[j]| <= a，直接跳过当前 j
                if (Math.abs(arr[i] - arr[j]) > a) {
                    continue;
                }
                
                // k 从 j + 1 开始，天然满足 j < k (即 i < j < k)
                for (int k = j + 1; k < n; k++) {
                    // 剪枝 2：检查另外两个绝对值条件
                    if (Math.abs(arr[j] - arr[k]) > b || Math.abs(arr[i] - arr[k]) > c) {
                        continue;
                    }
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}