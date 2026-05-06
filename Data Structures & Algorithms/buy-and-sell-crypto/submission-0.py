class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        n=len(prices)
        bp=prices[0]
        for i in range(n):
            cp=prices[i]
            if (prices[i]<bp):
                bp=prices[i]
            maxprofit=max(maxprofit,cp-bp)
        return maxprofit
        