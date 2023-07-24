class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        # O(n) space solution
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]
        '''
        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

            return arr

        k = k % len(nums)
        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)