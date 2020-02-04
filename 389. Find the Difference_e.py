class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            if i not in dic:
                dic[i]=1
        for j in t:
            if j not in dic:
                return j
                break
            if j in dic:
                dic[j]-=1
                if dic[j]<0:
                    return j
                    break
  
  #alter v
  class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.defaultdict()
        li_t = list(t)
        
        for ele in li_t:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        print(dic)
        
        # check s:
        li_s = list(s)
        for item in li_s:
            if item in dic:
                dic[item]-=1
        
        return ''.join([key for key, value in dic.items() if value!=0])
        
        
  
  #alter v
  class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_s = list(s)
        new_t = list(t)
        for alpha in new_s:
            new_t.remove(alpha)
        return new_t[0]
        
 #alter v2
  class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = collections.Counter(list(s))
        tCounter = collections.Counter(list(t))
        #print(sCounter, tCounter)
        for tk, tv in tCounter.items():
            if tk not in sCounter.keys():
                return tk
            else:
                sv = sCounter[tk]
                if tv !=  sv: return tk
  
  
