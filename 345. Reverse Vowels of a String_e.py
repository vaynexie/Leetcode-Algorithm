class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=['a','e','i','o','u','A','E','I','O','U']
        index_list=[]
        item_list=[]
        for index,item in enumerate(s):
            if item in vowel:
                index_list.append(index)
                item_list.append(item)
        s_list=list(s)
        for i in index_list:
            s_list[i]=item_list.pop()
      
        return ''.join(s_list)
        
 #better v
 class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=['a','e','i','o','u','A','E','I','O','U']
        index_list=[]
        item_list=[]
        for index,item in enumerate(s):
            if item in vowel:
                index_list.append(index)
                item_list.append(item)
        index_list = index_list[::-1]
        s=list(s)
        for f,d in enumerate(index_list):
            s[d] = item_list[f]
        return(''.join(s))
        
