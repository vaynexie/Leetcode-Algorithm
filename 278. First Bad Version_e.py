"""
In our case, we indicate leftleft and rightright as the boundary of our search space (both inclusive). 
This is why we initialize left = 1left=1 and right = nright=n. How about the terminating condition? 
We could guess that leftleft and rightright eventually both meet and it must be the first bad version, but how could you tell for sure?

"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while(left+1<right):
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        if isBadVersion(left):
            return left
        else:
            return left+1
