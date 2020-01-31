class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        f = [1] * n
        if n < 2:
            return 1
        f[1] = 2
        for i in range(2,n):
            f[i] = f[i-1] + f[i-2]
        return f[-1]


  """
  Algorithm

Dynamic Programming
One can reach i^{th} step in one of the two ways:

1. Taking a single step from (i-1)^{th} step.

2. Taking a step of 2 from (i-2)^{th} step.
 
Let dp[i]dp[i] denotes the number of ways to reach on i^{th} step:

dp[i]=dp[i-1]+dp[i-2]

 Similar to Fibonacci Number
  """
