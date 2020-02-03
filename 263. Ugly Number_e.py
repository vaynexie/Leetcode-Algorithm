class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num==1:
            return True
        
        for factor in [2,3,5]:
            while num%factor==0:
                num/=factor
        #Time complexity O(log(num))
        #Space complexity O(1)
        return num==1
