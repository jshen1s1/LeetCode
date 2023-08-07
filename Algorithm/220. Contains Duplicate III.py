class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        bucket = {}
        # use valueDiff + 1 to avoid divided by 0 
        b_size = valueDiff + 1
        for i, num in enumerate(nums):
            key = num / b_size
            if key in bucket:
                return True
            if key - 1 in bucket and abs(num - bucket[key-1]) <= valueDiff:
                return True
            if key + 1 in bucket and abs(num - bucket[key+1]) <= valueDiff:
                return True
            bucket[key] = num
            # remove first added bucket, maintaining indexDiff number of buckets
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] / b_size]

        return False
    