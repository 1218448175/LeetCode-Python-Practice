class Solution {
    public int subtractProductAndSum(int n) {
        int mul = 1;
        int sum = 0;
        while (n > 0) {
            int mod = n % 10;
            n /= 10;
            mul *= mod;
            sum += mod;
        }
        return mul - sum;
    }
}