class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        str_list=str.split(' ')
        pattern_list=list(pattern)
        if len(str_list)!=len(pattern_list):return False
        
        dic={}
        for i in range(len(pattern_list)):
            if pattern_list[i] in dic:
                pattern_list[i]=dic[pattern_list[i]]
            else:
                if str_list[i] not in dic.values():
                    dic[pattern_list[i]]=str_list[i]
                    pattern_list[i]=str_list[i]
                else:return False
        return str_list==pattern_list
                
