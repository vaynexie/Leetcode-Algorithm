class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return True
        a=False
        low=1
        high=num
        while low+1<high:
            mid=(low+high)//2
            if mid*mid==num:
                a=True
                break
            if mid*mid>num:
                high=mid
            else:low=mid
        return a
            
     
