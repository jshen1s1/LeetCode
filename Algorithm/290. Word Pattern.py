class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_list = s.split(" ")

        if len(pattern) != len(str_list):
            return False
        if len(set(pattern)) != len(set(str_list)):
            return False

        mp = {}
        for word, p in zip(str_list, pattern):
            if word not in mp:
                mp[word] = p
            elif mp[word] != p:
                return False

        return True