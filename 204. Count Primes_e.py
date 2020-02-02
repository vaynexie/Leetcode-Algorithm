class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n < 2):
            return 0
        
        primelist = [1] * n

        primelist[0] = 0
        primelist[1] = 0
        
        for x in range(2, int(n ** 0.5)+1):
            if(primelist[x] == 1):
                for y in range(x*x, n, x):
                    primelist[y] = 0
        return sum(primelist)
        
  
  """
  hint:
  We start off with a table of n numbers. Let's look at the first number, 2. We know all multiples of 2 must not be primes, so we mark them off as non-primes. T
  hen we look at the next number, 3. Similarly, all multiples of 3 such as 3 × 2 = 6, 3 × 3 = 9, ... must not be primes, so we mark them off as well. 
  Now we look at the next number, 4, which was already marked off. What does this tell you? Should you mark off all multiples of 4 as well?
  
  4 is not a prime because it is divisible by 2, which means all multiples of 4 must also be divisible by 2 and were already marked off. 
  So we can skip 4 immediately and go to the next number, 5. 
  Now, all multiples of 5 such as 5 × 2 = 10, 5 × 3 = 15, 5 × 4 = 20, 5 × 5 = 25, ... can be marked off. 
  There is a slight optimization here, we do not need to start from 5 × 2 = 10. Where should we start marking off?
  
  In fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3. 
  Therefore, if the current number is p, we can always mark off multiples of p starting at p^2, then in increments of p: p^2 + p, p^2 + 2p, ... 
  Now what should be the terminating loop condition?
  
  the terminating loop condition can be p < √n, as all non-primes ≥ √n must have already been marked off. When the loop terminates, all the numbers in the table that are non-marked are prime.
  
  """
