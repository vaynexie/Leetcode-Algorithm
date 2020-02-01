class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        final=False
        s_low=s.lower()
        result=''
        for i in range(len(s_low)):
            if not s_low[i] in string.punctuation + ' ':    
                result += s_low[i]
        if result[::-1]==result:
            final=True
        return final
        
  #better v
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
  
