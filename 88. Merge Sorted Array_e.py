class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and n!=0:
            nums1=nums2
         
            
        elif n==0 and m!=0:
            nums1=nums1 
            
            
        elif m!=0 and n!=0:
            for i in range(m,m+n):
                nums1[i]=nums2[len(nums2)-i]
            nums1.sort()
            
#alter v
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        for i in range((len(nums1)-len(nums2)),len(nums1)):
            nums1[i]=nums2[count]
            count+=1
        return nums1.sort()
        

#alter v2
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        i = j = 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i < m: 
            res.append(nums1[i])
            i+=1
        while j < n: 
            res.append(nums2[j])
            j+=1
        
        for i in range(len(res)):
            nums1[i] = res[i]
