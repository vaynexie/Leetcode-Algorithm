class Solution(object):
    def check(self,aa):
        tt='1'
        num=1
        seen= {aa[0]: num}
        for i in range(1,len(aa)):
            if aa[i] in seen.keys():
                tt+=str(seen[aa[i]])
            else:
                num+=1
                seen[aa[i]]=str(num)
                tt+=str(seen[aa[i]])
        return tt
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0 and len(t)==0:
            return True
        
        else:
            tt_s=self.check(s)
            tt_t=self.check(t)
            if tt_s==tt_t:return True
            else:return False
            
 #better v
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2tD = dict(); s = list(s); t = list(t)
        for sInd, sChr in enumerate(s):
            tChr = t[sInd]
            if sChr in s2tD: 
                s[sInd] = s2tD[sChr]
            else:
                if tChr not in s2tD.values():
                    s2tD[sChr] = tChr
                    s[sInd] = tChr
                else:
                    return False 
        return (s==t)
