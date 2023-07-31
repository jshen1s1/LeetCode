class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        '''
        # sliding window approach O(n)
        if sum(nums) < target:
            return 0

        shortest = len(nums)
        total = 0
        left = right = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                total -= nums[left]
                shortest = min(shortest, right-left+1)
                left += 1
            right += 1

        return shortest
        '''

        # binary search approach O(nlogn)
        if sum(nums) < target:
            return 0

        def slidingWin(mid):
            cur = 0
            maxSum = 0
            left = 0
            for i in range(len(nums)):
                cur += nums[i]
                if i > mid - 1:
                    cur -= nums[left]
                    left += 1
            
                maxSum = max(cur, maxSum)

            return maxSum >= target
            
        res = 0
        left = 1
        right = len(nums)
        while left <= right:
            mid = (right + left) // 2
            if slidingWin(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        
        return res