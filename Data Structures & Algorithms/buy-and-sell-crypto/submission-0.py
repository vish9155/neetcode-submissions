class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit=0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                max_Profit=max(max_Profit,profit)
        return max_Profit    
        