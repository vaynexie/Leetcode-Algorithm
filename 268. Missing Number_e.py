class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(i for i in range(1+len(nums)))
        total_r=sum(j for j in nums)
        return total-total_r
