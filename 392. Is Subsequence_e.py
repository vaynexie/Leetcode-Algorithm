class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i])+1:]
            else:
                return False
        return True
