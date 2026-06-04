class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ma = prices[0]
        maxProfit = 0
        for p in prices:
            if p < mi:
                mi = p
                ma = 0
            else:
                if p > ma:
                    ma = p
                newMaxProfit = ma-mi
                if newMaxProfit > maxProfit:
                    maxProfit = newMaxProfit
        
        return maxProfit
        