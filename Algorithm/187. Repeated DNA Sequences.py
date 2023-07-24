class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        visited = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:i+10] in visited:
                res.add(s[i:i+10])
            else:
                visited.add(s[i:i+10])

        return list(res)