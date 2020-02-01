class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        old=[]
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==0:
                old.append(nums[i])
        c=sum(set(nums))-sum(set(old))
        return c
 
 """
 better v 
 math:
2∗(a+b+c)−(a+a+b+b+c)=c

 """
 
 class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
