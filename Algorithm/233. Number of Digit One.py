class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=0 :
            return 0

        res = 0
        cur = n
        pos = 1
        
        # starting from the one's position
        # if current digit == 0: res += prefix * pos
        # if current digit == 1: res += prefix * pos + postfix + 1
        # if current digit > 1: res += prefix * pos + pos
        while cur > 0:
            digit = cur % 10
            cur /= 10
            res += cur * pos
            if digit == 1:
                res += n % pos + 1
            elif digit > 1:
                res += pos
            pos *= 10
        
        return res