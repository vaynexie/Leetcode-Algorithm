class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        else:
            strg = str(x)
            revst = strg[::-1]
            if int(revst)==x:
                return True
 
 """
   Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
   
 """
