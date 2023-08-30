class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        if num // 10 == 0:
            return num

        s = 0
        for i in str(num):
            s += int(i)

        return self.addDigits(s)
        '''
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
