class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]

        res = []

        for i in range(len(expression)):
            if expression[i] in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        res.append(self.helper(l, r, expression[i])) 

        return res

    def helper(self, left, right, op):
        if op == '+':
            return left + right
        elif op == '-':
            return left -  right
        else:
            return left * right