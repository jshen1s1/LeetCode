class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [1]
        res, num = 0, 0
        sign = 1

        for c in s+"+":
            if c == ' ':
                continue
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-':
                res += num * sign * stack[-1]
                sign = 1 if c == "+" else -1
                num = 0
            elif c == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif c == ')':
                res += num * sign * stack.pop()
                num = 0

        return res