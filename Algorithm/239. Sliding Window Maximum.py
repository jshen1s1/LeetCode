from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        res = []

        for i, n in enumerate(nums):
            while queue and n > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if queue[0] == i - k:
                queue.popleft()

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res