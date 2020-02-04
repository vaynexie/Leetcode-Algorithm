class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic={}
        for i in magazine:
            if i in dic:
                dic[i]+=1
            if i not in dic:
                dic[i]=1
        for j in ransomNote:
            if j not in dic:
                return False
                break
            if j in dic:
                dic[j]-=1
                if dic[j]<0:
                    return False
                    break
        return True
