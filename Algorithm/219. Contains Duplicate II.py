class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dic:
                if abs(i - dic[num]) <= k:
                    return True
            dic[num] = i

        return False