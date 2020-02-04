class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        kk=[]
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    kk.append(i)
                    
        else:
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    kk.append(i)
        return kk

#better v
class Solution:
    """
    Runtime: 40 ms, faster than 94.21% of Python3 online submissions for Intersection of Two Arrays II.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        num1Dict = {}
        
        for n in nums1:
            num1Dict[n] = num1Dict[n] + 1 if n in num1Dict else 1
            
        for n in nums2:
            if n in num1Dict and num1Dict[n] > 0:
                intersection.append(n)
                num1Dict[n] = num1Dict[n] - 1
                
        return intersection
