class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_of_5 = 0
    
        while n > 4 :
            count_of_5 +=  n // 5 
            n = n // 5
        return count_of_5
