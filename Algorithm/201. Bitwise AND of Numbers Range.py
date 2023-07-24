class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if right == left:
            return left

        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1

        #print(bin(right))
        return right << cnt