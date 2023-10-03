class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        num_of_cit = [0] * (n+1)
        for c in citations:
            if c >= n:
                num_of_cit[n] += 1
            else:
                num_of_cit[c] += 1
        
        sum_of_pap = 0
        for i in range(n, -1, -1):
            sum_of_pap += num_of_cit[i]
            if sum_of_pap >= i:
                return i

        return 0
