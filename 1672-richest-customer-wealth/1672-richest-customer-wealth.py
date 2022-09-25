class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for account in accounts:
            total_money = 0
            for money in account:
                total_money += money
            
            if total_money >= max_wealth:
                max_wealth = total_money
        
        return max_wealth