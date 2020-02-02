class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int((format(n,'#034b')[2:])[::-1], 2)
        
        
#alter v
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = 1
        result = 0
        for i in range(32):
            b = n & x
            # print(b)
            if b:
                result = (result << 1) + 1
            else:
                result = (result << 1) + 0
            x = x << 1
        return result
        
 """
 &：按位与操作，只有 1 &1 为1，其他情况为0。可用于进位运算。

|：按位或操作，只有 0|0为0，其他情况为1。

~：逐位取反。

^：异或，相同为0，相异为1。可用于加操作（不包括进位项）。

<<：左移操作，2的幂相关

>>：右移操作，2的幂相关

"""
