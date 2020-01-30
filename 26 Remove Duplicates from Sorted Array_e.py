class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums!=[]:
            total=1
            k=nums[0]
            for i in nums[1:]: 
                if i==k:
                    nums.remove(i)
                
                if i!=k:
                    k=i
                    total+=1
       
#better solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1,len(nums)):
            if nums[index]!=nums[i]:
                nums[index+1]=nums[i]
                index+=1
        return index+1
    
    """"
    Clarification:

    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
    
    """"
