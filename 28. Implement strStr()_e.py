class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        judge=-1
        length=len(needle)
        if needle!="":
            for i in range(len(haystack)):
                if haystack[i]==needle[0]:
                    if i+length-1<=len(haystack):
                        if haystack[i:i+length]==needle:
                            judge=i
                            break
        if haystack=="":
            judge=-1
        
        if  needle=="":
            judge=0
            
        return judge
