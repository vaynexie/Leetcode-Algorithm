class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        aa=''
        for i in digits:
            aa+=str(i)
        aa_num=int(aa)+1
        aa_str=str(aa_num)
        aa_ve=[]
        for j in aa_str:
            aa_ve.append(int(j))
        return aa_ve
        
 
 #alter v
 class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
 
