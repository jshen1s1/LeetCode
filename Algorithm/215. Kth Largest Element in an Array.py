import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # quick select O(n)-O(n**2)
        def quickSelect(nums, k):
            p = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > p:
                    left.append(num)
                elif num < p:
                    right.append(num)
                else:
                    mid.append(num)

            if len(left) >= k:
                return quickSelect(left, k)
            if len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))

            return p

        return quickSelect(nums, k)

        
        '''
        # heap1 O(nlogk)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)

        return heap[0]

        # heap2 O(nlogk)
        heap = nums[:k]
        heapify(heap)
        for num in nums[k:]:
            heapq.heappushpop(heap, num)

        return heap[0]
        '''