"""
The points of interest are the peaks and valleys in the given graph. 
We need to find the largest peak following the smallest valley. 
We can maintain two variables - minprice and maxprofitcorresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cs, ms, mp = 0, 0, 0 # cummulative sum, min cummulative sum, max profit
        for j in range(len(prices) - 1):
            cs += prices[j+1] - prices[j] # compute daily gain
            mp = max(mp, cs - ms)
            ms = min(cs, ms)
        return mp if mp > 0 else 0
