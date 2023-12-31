class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        '''
        citations = citations[::-1]
        for i in range(len(citations)):
            if i >= citations[i]:
                return i

        return len(citations)
        '''
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1

        return n - l