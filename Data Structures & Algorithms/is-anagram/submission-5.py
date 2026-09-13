class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        s_chars = {}
        for char in s:
            if char not in s_chars:
                s_chars[char] = 0
            s_chars[char] += 1
        t_chars = {}
        for char in t:
            if char not in t_chars:
                t_chars[char] = 0
            t_chars[char] += 1
        for char in s_chars:
            if char in t_chars:
                if s_chars[char] != t_chars[char]:
                    return False
            else:
                return False
        return True