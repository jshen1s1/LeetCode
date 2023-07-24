class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]


        for i in range(1,len(nums)):
            if i < 2:
                dp[i] = max(nums[i], dp[i-1])
            else:
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]