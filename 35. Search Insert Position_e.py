class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        output=-1
        for i in range(len(nums)):
            if target-nums[i]<=0:
                output=i
                break
        if output==-1:
            output=len(nums)
        return output
        
  #alternative1
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    nums.append(target)
    return sorted(nums).index(target)
    
  #2
  class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
                            if target not in nums:
                                  return bisect.bisect(nums,target)
                            for i in range(len(nums)):
                                     if nums[i]==target:
                                          return i
 
 #3
 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        x = len(nums)
        while(i < x and nums[i] < target):
            i += 1
        return i
 
 #binary search
 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while(l<r):
            m = (l+r)//2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return l
