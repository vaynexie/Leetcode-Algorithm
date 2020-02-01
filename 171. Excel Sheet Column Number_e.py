class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums=0
        leng=len(s)
        for i in range(leng):
            nums+=(ord(s[i])-64)*26**(leng-i-1)
        return nums

#alter v
#dict
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {chr(ord('A') + i):i+1 for i in range(27)}
        total = 0
        for i in range(len(s)):
            total += dic[s[i]]*(26**(len(s)-1-i))
        return total
		```
