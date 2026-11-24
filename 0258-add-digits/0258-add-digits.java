class Solution {
    public int addDigits(int num) {
        int ans = num;
        while (ans >= 10) {
            int total = 0;
            while (ans > 0) {
                total += ans % 10;
                ans /= 10;
            }
            ans = total;
        }
        return ans;
    }
}