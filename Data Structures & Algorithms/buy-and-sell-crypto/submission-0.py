class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        if len(prices) < 2:
            return 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                maxprofit = max(maxprofit, (prices[r] - prices[l]))
                r += 1

        return maxprofit