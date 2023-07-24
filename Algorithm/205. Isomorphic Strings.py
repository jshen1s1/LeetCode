class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp = {}
        mp2 = {}

        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = t[i]
            else:
                if mp[s[i]] != t[i]:
                    return False
            if t[i] not in mp2:
                mp2[t[i]] = s[i]
            else:
                if mp2[t[i]] != s[i]:
                    return False

        return True

        '''
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        '''