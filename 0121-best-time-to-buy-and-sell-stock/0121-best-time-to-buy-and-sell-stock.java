class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int lPtr = 0;
        
        for (int rPtr = 0; rPtr < prices.length; rPtr++) {
            if (prices[lPtr] < prices[rPtr]) {
                max = Math.max(prices[rPtr] - prices[lPtr], max);
            } else {
                lPtr = rPtr;
            }
        }
        return max;
    }
}