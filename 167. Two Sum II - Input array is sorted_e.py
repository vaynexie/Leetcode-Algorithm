#two pointers method
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers)-1
    
        total = numbers[low] + numbers[high]
    
        while total != target:
    
            if total< target:
                low += 1
            elif total > target:
                high -= 1
            total = numbers[low] + numbers[high]
        
        return [low+1, high+1]
