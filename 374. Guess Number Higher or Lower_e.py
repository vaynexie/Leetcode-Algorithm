# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        if guess(n)==0:
            return n
        
        while low+1<=high:
            mid=(low+high)//2
            g=guess(mid)
            if g==0:
                return mid
                break
            if g==-1:
                high=mid
            if g==1:
                low=mid
