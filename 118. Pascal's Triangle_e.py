class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            total=[]
        if numRows==1:
            total=[[1]]
        if numRows==2:
            total=[[1],[1,1]]
        if numRows>2: 
            total=[[1],[1,1]]
            for i in range(2,numRows):
                temp=[]
                temp.append(1)
                for j in range(1,numRows):
                    if j>i-1:
                        temp.append(1)
                        break
                    temp.append(total[i-1][j-1]+total[i-1][j])
                total.append(temp)
        return total
        
   #better v
   class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1],[1,1]]
        k = numRows
        if k < 2:
            return nums[:k]
        
        for i in range(2,k):
            nums.append([1])
            for j in range(0,len(nums[i-1])-1):
                nums[i].append(nums[i-1][j] + nums[i-1][j+1])
            nums[i].append(1)
        return nums
