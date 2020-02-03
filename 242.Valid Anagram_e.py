class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter={}
        if len(s)==0 and len(t)==0:
            return True 
        if len(s)!=len(t):return False
        
        for i in s:
            if i not in letter:
                letter[i]=0
            if i in letter:
                letter[i]=letter[i]+1
        for j in t:
            if j not in letter:
                return False
            if j in letter:
                letter[j]-=1
        rest=list(letter.values())
        empty=[0]*len(rest)
        return rest==empty
                
#alter v
def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        
