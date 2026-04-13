class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxP = 0
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                temp = prices[r] - prices[l]
                MaxP = max(MaxP, temp)
            else:
                l = r
            r += 1
        return MaxP
            