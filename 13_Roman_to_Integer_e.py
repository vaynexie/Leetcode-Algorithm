class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        my_dict = {'I': 1, 'V': 5, 'X': 10,'L':50,'C':100,'D':500,'M':1000}
        my_dict2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        my_list = str(s)
        summ=0
        
        i=0
        while i+1<=len(my_list)-1:
            
            if my_list[i]+ my_list[i+1] in my_dict2:
                summ+=my_dict2[my_list[i]+ my_list[i+1]]
                my_list = my_list[:i] + my_list[(i+2):]

            else:
                i+=1
                
        for k in my_list:
            summ+=my_dict[k]
        
        return summ

#better solution
class Solution:
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(0, len(s) - 1):
            if self.dict[s[i + 1]] > self.dict[s[i]]: # next numeral is larger than the current numeral
                num -= self.dict[s[i]]
            else:
                num += self.dict[s[i]] # next numeral is smaller
        return num + self.dict[s[-1]]
