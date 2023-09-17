class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We only need to know the profit is available compared to previous day
        
        len_prices = len(prices)
        total_profit = 0
        idx = 0
        while idx < len_prices-1:
            profit = prices[idx+1] - prices[idx]
            if profit > 0:
                total_profit += profit
            idx += 1
        return total_profit
                
        
        
        