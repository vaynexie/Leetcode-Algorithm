class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
       
        Duplicate=False
        dictory={}
        for index,num in enumerate(nums):
            if num not in dictory:
                dictory[num]=index
            else:
                if index-dictory[num]<=k:
                    Duplicate=True
                    break
                else:
                    dictory[num]=index
        
        return Duplicate
