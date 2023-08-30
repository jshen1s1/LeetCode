class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # x xor itself = 0
        xor = 0
        for i in nums:
            xor ^= i

        # find the right most non-zero position
        mask = xor & -xor

        # make two separate groups
        sub1, sub2 = 0, 0
        for i in nums:
            # if not zero at that position
            if i & mask != 0:
                sub1 ^= i
            else:
                sub2 ^= i

        return [sub1, sub2]