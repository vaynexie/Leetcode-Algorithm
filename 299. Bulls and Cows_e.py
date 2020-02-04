class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret =list(secret)
        guess=list(guess)
        freq = {} 
        for item in secret:
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        A=0
        B=0
        for j in range(len(guess)):
            if secret[j]==guess[j]:
                A+=1
                freq[guess[j]]-=1
        for j in range(len(guess)):
            if secret[j]!=guess[j] and guess[j] in freq and freq[guess[j]]>0:
                freq[guess[j]]-=1
                B+=1
        return str(A)+'A'+str(B)+'B'
        
class Solution:
    def getHint(self, secret: str, guess: str) -> str:       
        na, stk= 0, {str(i):[0, 0] for i in range(10)}         
        for i in range(len(secret)):
            vs, vg = secret[i], guess[i]
            if vs==vg:
                na += 1
            else:
                stk[vs][0] += 1
                stk[vg][1] += 1
        nb = sum(min(stk[i][0], stk[i][1]) for i in stk)
        return "{0:d}A{1:d}B".format(na, nb)

"""
stk=
{'0': [0, 0],
 '1': [0, 0],
 '2': [0, 0],
 '3': [0, 0],
 '4': [0, 0],
 '5': [0, 0],
 '6': [0, 0],
 '7': [0, 0],
 '8': [0, 0],
 '9': [0, 0]}


"""
