class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<2:
            return 0
        max_profit=0
        curr_profit=0
        for i in range(1,n):
            curr_profit+=prices[i]-prices[i-1]
            max_profit=max(max_profit,curr_profit)
            if curr_profit<0:
                curr_profit=0
        return max_profit