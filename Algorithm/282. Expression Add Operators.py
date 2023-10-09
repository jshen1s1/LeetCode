class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        def backtracking(res, idx, op, last, expre):
            if idx == len(num):
                if res == target and op == 0:
                    ans.append(expre[1:])
                return

            op = op*10 + int(num[idx])

            if op > 0:
                backtracking(res, idx+1, op, last, expre)

            backtracking(res+op, idx+1, 0, op, expre+'+'+str(op))
            if expre:
                backtracking(res-op, idx+1, 0, -op, expre+'-'+str(op))
                backtracking(res-last+last*op, idx+1, 0, last*op, expre+'*'+str(op))

        backtracking(0, 0, 0, 0, '')
        return ans

        '''
        # TLE
        ans = []
        def dfs(idx, path):
            #print(path)
            if idx == len(num)-1:
                path += num[idx]
                if eval(path) == target:
                    ans.append(path)
                return

            dfs(idx+1, path + num[idx] + '+')
            dfs(idx+1, path + num[idx] + '-')
            dfs(idx+1, path + num[idx] + '*')

            if num[idx] != '0' or (path and path[-1] not in ['+', '-', '*']):
                dfs(idx+1, path + num[idx])

        dfs(0, '')
        return ans
        '''