class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x = bin(n)[2:]
        return x.count('1')
        
        """
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt
        """