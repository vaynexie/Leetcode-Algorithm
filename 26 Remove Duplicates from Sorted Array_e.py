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
       
