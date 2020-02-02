class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Duplicate=False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                Duplicate=True
                break
        return Duplicate
 
#alter v
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False
