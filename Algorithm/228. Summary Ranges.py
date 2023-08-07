class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        '''

        start = nums[0]
        res = []
        nums.append(float('inf'))

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    res.append(str(start) + '->' + str(nums[i-1]))
                else:
                    res.append(str(start))
                start = nums[i]

        return res
        '''

        start = ''
        res = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                if not start:
                    start = str(nums[i-1]) + '->'
            else:
                res.append(start+str(nums[i-1]))
                start = ''

        res.append(start+str(nums[-1]))
        return res