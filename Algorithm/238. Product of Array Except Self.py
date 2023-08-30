class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        left = [1] * (len(nums)+1)

        for i in range(1, len(nums)+1):
            left[i] = nums[i-1] * left[i-1] 

        right = [1] * (len(nums)+1)

        for i in range(len(nums)-1, -1, -1):
            right[i] = nums[i] * right[i+1] 
        
        res = [left[k]*right[k+1] for k in range(len(nums))]

        return res
        '''
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res