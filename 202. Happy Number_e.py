class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while True:
            n = sum(int(d)**2 for d in str(n))
            if n == 1:
                return True
            if n in seen:
                return False
            seen.append(n)
