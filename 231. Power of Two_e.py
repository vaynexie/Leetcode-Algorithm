class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1 or n==2:
            return True
        if n<0:
            return False
        else:
            for i in range(int(n**0.5)+2):
                if 2**i==n:
                    return True
                    break
                if 2**i>n:
                    return False
                    break
                    
 #alter v
 class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            while n%2 == 0:
                n /= 2
            if n == 1:
                return True
        if n == 0 or n != 1:
            return False
            
#bitwise operation v
#If a number is power of 2 then it will always contain 1 set bit.
		if n<=0:
            return False
        if n&(n-1) == 0:
            return True
        else:
            return False
 
