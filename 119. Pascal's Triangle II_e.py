class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1,]
        elif rowIndex == 1:
            return [1,1]
        else:
            last_row = self.getRow(rowIndex-1)
            temp=[1]
            for j in range(0,len(last_row)-1):
                temp.append(last_row[j] + last_row[j+1])
            temp.append(1)
            return temp
        
        
