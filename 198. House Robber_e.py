class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0,0,0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return nums[len(nums)-1]
        
