class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0

        for i in range(0,len(prices)):
            buying_price = prices[i]
            for j in range(i+1,len(prices)):
                selling_price = prices[j]
                res = max(res, selling_price- buying_price)

        return res