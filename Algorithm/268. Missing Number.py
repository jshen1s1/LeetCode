class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # math
        n = len(nums)
        return sum(range(n+1)) - sum(nums)
        
        """
        # bitwise
        result = 0
        for i, val in enumerate(nums):
            result ^= i+1
            result ^= val

        return result
        """