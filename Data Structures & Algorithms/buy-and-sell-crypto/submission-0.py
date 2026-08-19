class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        profit = 0
        
        for sell in prices:
            cost = sell - min_price
            profit = max(profit, cost)
            min_price = min(min_price, sell)
            
        return profit
        