class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(left, start, cur):
            if left == 0 and sum(cur) == n:
                res.append(cur[::])
                return

            if left == 0 or sum(cur) > n:
                return
            
            for i in range(start, 10):
                dfs(left-1, i+1, cur+[i])

        res = []
        dfs(k, 1, [])
        return res