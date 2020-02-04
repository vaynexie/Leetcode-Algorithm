class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            if i not in dic:
                dic[i]=1
        flag=-1
        for index,item in enumerate(s):
            if dic[item]==1:
                flag=1
                a=index
                break
        if flag==1:return a
        else:return -1
 
 #alter v
 class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        myset = dict()
        for ch in s:
            myset[ch] = myset[ch] - 1 if ch in myset else 1
        
        for i,ch in enumerate(s):
            if myset[ch] > 0:
                return i
        return -1
