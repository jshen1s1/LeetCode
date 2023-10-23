class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False

        def dfs(path, s):
            if not s:
                return len(path) > 2

            for i in range(len(s)):
                if s[0] == '0' and i > 0:
                    break

                cur = int(s[:i+1])
                if len(path) > 1 and cur != path[-1] + path[-2]:
                    continue

                if dfs(path + [cur], s[i+1:]):
                    return True

            return False

        return dfs([], num)