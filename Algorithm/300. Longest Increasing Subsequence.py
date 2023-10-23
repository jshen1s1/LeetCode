class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        # O(n^2)
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            
        return max(dp)
        '''
        '''
        # bisect approach
        arr = [nums.pop(0)]

        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n

        return len(arr)
        '''

        tails = [0] * len(nums)
        size = 0

        for n in nums:
            l, r = 0, size
            while l < r:
                m = (l + r) // 2
                if tails[m] < n:
                    l = m + 1
                else:
                    r = m

            tails[l] = n
            size = max(size, l+1)

        return size
