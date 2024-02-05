class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lPtr = 0
        profit = 0
        for rPtr in range(1, len(prices)):
            if prices[lPtr] < prices[rPtr]:
                profit = max(profit, prices[rPtr] - prices[lPtr])
            else:
                lPtr = rPtr
        return profit