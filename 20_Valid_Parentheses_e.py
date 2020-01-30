#part solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        judge=True
        
        my_dict=['(':1,')':2,'[':3,']':4,'{':5,'}':6]
        
        a=0
        b=0
        c=0
        
        for i in s:
            if i=='(' or i==')':
                a+=my_dict[i]
            if i=='[' or i==']':
                b+=my_dict[i]
            if i=='{' or i=='}':
                c+=my_dict[i]
        
        if a%3!=0 or b%7!=0 or c%11!=0:
            judge=False 





#worked solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_set = {'(','{','['}
        right_set = {')','}',']'}
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for each in s:
            if each in left_set:
                stack.append(each)
            elif each in right_set:
                try:
                    pop_out = stack.pop()
                except:
                    return False
                if mapping[each] ==  pop_out:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
