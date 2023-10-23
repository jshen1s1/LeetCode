class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []

        def isValid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append((i, '('))
                elif s[i] == ')':
                    if stack and stack[-1][1] == '(':
                        stack.pop()
                    else:
                        stack.append((i, ')'))

            return len(stack) == 0, stack

        def dfs(s, init, l, r):
            if l == 0 and r == 0 and isValid(s)[0]:
                res.append(s)
                return

            for i in range(init, len(s)):
                if i != init and s[i] == s[i-1]:
                    continue
                if r > 0 and s[i] == ')':
                    dfs(s[:i]+s[i+1:], i, l, r-1)
                elif l > 0 and s[i] == '(':
                    dfs(s[:i]+s[i+1:], i, l-1, r)


        stack = isValid(s)[1]
        l = len([True for (_, v) in stack if v == '('])
        r = len(stack) - l

        res = []
        dfs(s, 0, l, r)
        return res