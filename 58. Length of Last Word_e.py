class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[-1:]==' ':
            num=0
            for i in range(len(s)-1,-1,-1):
                
                if s[i]!=' ':
                    break
                num+=1
            aa=''
            for i in range(len(s)-num-1,-1,-1):
                if s[i]==' ':break
                aa+=s[i]
        else:  
            aa=''
            for i in range(len(s)-1,-1,-1):
                if s[i]==' ':break
                aa+=s[i]
    
        return len(aa)
 
class Solution(object):
    def lengthOfLastWord(self, s):
  #better v
    index = s[::-1].strip().find(' ')
    
    if index != -1:
        return len(s[len(s) - index:])
    
    return len(s.strip())
