class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        i = 0
        right = len(nums)
        while i < right:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                right -= 1
            else:
                i += 1
        '''
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1