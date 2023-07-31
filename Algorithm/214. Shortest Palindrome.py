class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s[::-1]
        if res == s:
            return s

        for i in range(1, len(s)):
            if s[:-i] == res[i:]:
                return res[:i] + s
