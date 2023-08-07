class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums, op = [], '+'
        total, num = 0, 0

        for c in s+"+":
            if c == ' ':
                continue
            if c.isdigit():
                num = 10*num + int(c)
            else:
                if op == '+':
                    nums.append(num)
                elif op == '-':
                    nums.append(-num)
                elif op == '*':
                    x = nums.pop()
                    nums.append(x * num)
                elif op == '/':
                    x = nums.pop()
                    sign = 1 if x > 0 else -1
                    res = abs(x) // num
                    nums.append(res * sign)
                num = 0
                op = c


        return sum(nums)