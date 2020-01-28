class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        
        else:
            
            if x>0:
                x_str=str(x)
                num=len(x_str)
                x_rev=0
                for j in range(num):
                    x_rev+=int(x_str[j])*(10**(j))
         
            if x<0:
                x_str=str(-x)
                num=len(x_str)
                x_rev=0
                for j in range(num):
                    x_rev+=int(x_str[j])*(10**(j))
                x_rev=-x_rev
           
            if x==0:
                x_rev=0
            
            if x_rev >= 2**31-1 or x_rev <= -2**31: return 0
            else: return x_rev
            
#better version
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
