class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        visited = set()

        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)

        return False
        '''
        visited = {}
        for num in nums:
            if visited.get(num, 0):
                return True
            else:
                visited[num] = 1

        return False